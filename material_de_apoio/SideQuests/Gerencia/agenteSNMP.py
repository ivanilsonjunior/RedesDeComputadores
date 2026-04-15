#
# Agente SNMP - Lembrar de executar:
# $ pip install psutil pysnmp
#
import psutil
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncio.dgram import udp
from pysnmp.entity.rfc3413 import cmdrsp, context
from pysnmp.proto.api import v2c

porta = 12345

# =========================
# 1. SNMP Engine
# =========================
snmpEngine = engine.SnmpEngine()

config.add_transport(
    snmpEngine,
    udp.DOMAIN_NAME,
    udp.UdpTransport().open_server_mode(('0.0.0.0', porta))
)

config.add_v1_system(snmpEngine, 'meu-agente', 'gerencia')

config.add_vacm_user(
    snmpEngine,
    2,
    'meu-agente',
    'noAuthNoPriv',
    (1, 3, 6, 1, 4, 1, 92524)
)

# =========================
# 2. Contexto e MIB
# =========================
snmpContext = context.SnmpContext(snmpEngine)
mibBuilder = snmpContext.get_mib_instrum().get_mib_builder()

MibScalar, MibScalarInstance = mibBuilder.import_symbols(
    'SNMPv2-SMI',
    'MibScalar',
    'MibScalarInstance'
)

# =========================
# 3. Classes dinâmicas
# =========================

class CpuUsageInstance(MibScalarInstance):
    def getValue(self, name, idx, **context):
        return self.getSyntax().clone(int(psutil.cpu_percent(interval=None)))


class RamTotalInstance(MibScalarInstance):
    def getValue(self, name, idx, **context):
        mem = psutil.virtual_memory()
        return self.getSyntax().clone(int(mem.total / (1024 * 1024)))


class RamAvailableInstance(MibScalarInstance):
    def getValue(self, name, idx, **context):
        mem = psutil.virtual_memory()
        return self.getSyntax().clone(int(mem.available / (1024 * 1024)))


class DiskUsageInstance(MibScalarInstance):
    def getValue(self, name, idx, **context):
        disk = psutil.disk_usage('/')
        return self.getSyntax().clone(int(disk.percent))


# =========================
# 4. Registro dos OIDs
# =========================
mibBuilder.export_symbols(
    '__MEU_HARDWARE_MIB',

    # CPU
    MibScalar((1,3,6,1,4,1,92524,1), v2c.Integer32()),
    CpuUsageInstance((1,3,6,1,4,1,92524,1), (0,), v2c.Integer32()),

    # RAM Total
    MibScalar((1,3,6,1,4,1,92524,2), v2c.Integer32()),
    RamTotalInstance((1,3,6,1,4,1,92524,2), (0,), v2c.Integer32()),

    # RAM Disponível
    MibScalar((1,3,6,1,4,1,92524,3), v2c.Integer32()),
    RamAvailableInstance((1,3,6,1,4,1,92524,3), (0,), v2c.Integer32()),

    # Disco
    MibScalar((1,3,6,1,4,1,92524,4), v2c.Integer32()),
    DiskUsageInstance((1,3,6,1,4,1,92524,4), (0,), v2c.Integer32()),
)

# =========================
# 5. Responders SNMP
# =========================
cmdrsp.GetCommandResponder(snmpEngine, snmpContext)
cmdrsp.NextCommandResponder(snmpEngine, snmpContext)

# =========================
# 6. Loop (CORRETO)
# =========================
snmpEngine.transport_dispatcher.job_started(1)

print(f"Agente SNMP rodando na porta {porta}...")

try:
    snmpEngine.transport_dispatcher.run_dispatcher()
except Exception:
    snmpEngine.transport_dispatcher.close_dispatcher()
    raise