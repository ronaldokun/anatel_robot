from selenium.webdriver.common.by import By

class Boleto(object):

    URL = 'http://sistemasnet/boleto/Boleto/ConsultaDebitos.asp?SISQSmodulo=6853'

    B_FISTEL = (By.ID, 'indTipoConsulta0')

    B_CPF = (By.ID, 'indTipoConsulta1')

    INPUT_FISTEL = (By.ID, 'NumFistel')

    INPUT_CPF = (By.ID, 'NumCNPJCPF')

    INPUT_DATA = (By.ID, 'DataPPDUR')

    BUT_CONF = (By.ID, 'botaoFlatConfirmar')

    MRK_TODOS = (By.ID, 'botaoFlatMarcarTodos')

    PRINT = (By.ID, 'botaoFlatImprimirSelecionados')

class Sec(object):

    Base = 'http://sistemasnet/SEC/'

    Consulta = 'http://sistemasnet/SEC/Tela.asp?SISQSmodulo=9336'

    Histor = 'http://sistemasnet/SEC/Chamada/Historico.asp?SISQSmodulo=11380'

    Agenda = 'http://sistemasnet/SEC/Default.asp?SISQSmodulo=7146&SISQSsistema=435'

    Agenda_Alt = 'http://sistemasnet/SEC/Agenda/Tela.asp?OP=a&SISQSmodulo=5817'

    Agenda_Canc = 'http://sistemasnet/SEC/Agenda/Tela.asp?OP=e&SISQSmodulo=5818'

    Agenda_Cons = 'http://sistemasnet/SEC/Agenda/Tela.asp?OP=c&SISQSmodulo=5819'

    Agenda_Incl = 'http://sistemasnet/SEC/Agenda/Tela.asp?OP=i&Acao=i&SISQSmodulo=5813'

    Agenda_TrAval = 'http://sistemasnet/SEC/Morse/AvaliadorAlterar/tela.asp?SISQSmodulo=7851'

    Cert_Alt = 'http://sistemasnet/SEC/Certificado/alterar/tela.asp?SISQSmodulo=12486'

    Cert_Ant = 'http://sistemasnet/SEC/Certificado/Anterior/Tela.asp?SISQSmodulo=10530'

    Cert_Cert = 'http://sistemasnet/SEC/Certificado/Certificar/Tela.asp?SISQSmodulo=4063'

    Cert_Estr_Incl = 'http://sistemasnet/SEC/Certificado/Estrangeiro/Incluir/Tela.asp?SISQSmodulo=11713'

    Cert_Estr_Prorr = 'http://sistemasnet/SEC/Certificado/Estrangeiro/Prorrogar/Tela.asp?SISQSmodulo=11488'

    Cert_Excl = 'http://sistemasnet/SEC/Certificado/Exclusao/Tela.asp?SISQSmodulo=8100'

    Cert_Impr = 'http://sistemasnet/SEC/Certificado/Imprimir/Tela.asp?SISQSmodulo=8370'

    Cert_Mnt = 'http://sistemasnet/SEC/Certificado/Manutencao/Tela.asp?xOp=2&SISQSmodulo=10619'

    Cert_Reat = 'http://sistemasnet/SEC/Certificado/Reativar/Tela.asp?SISQSmodulo=19806'

    Cert_2nVia = 'http://sistemasnet/SEC/Certificado/SegundaVia/Tela.asp?SISQSmodulo=4145'

    Ent_Alt = 'http://sistemasnet/SEC/Chamada/Entidade.asp?OP=A&SISQSmodulo=5263'

    Ent_AltRF = 'http://sistemasnet/SEC/Chamada/CadastroSRFRegularizado.asp?SISQSmodulo=16374'

    Ent_Incl = 'http://sistemasnet/SEC/Chamada/Entidade.asp?OP=I&SISQSmodulo=4150'

    Insc_Canc = 'http://sistemasnet/SEC/Inscricao/Cancelar/Tela.asp?SISQSmodulo=17306'

    Insc_Cons = 'http://sistemasnet/SEC/Consulta/Provamarcada/Tela.asp?SISQSmodulo=4090'

    Insc_Inc = 'http://sistemasnet/SEC/Inscricao/Incluir/Tela.asp?SISQSmodulo=4029'

    Insc_Mnt = 'http://sistemasnet/SEC/Inscricao/Reativar/Tela.asp?SISQSmodulo=18333'

    Prova_Res = 'http://sistemasnet/SEC/Prova/Resultado/Tela.asp?SISQSmodulo=3872'

class Entidade_SEC(object):

    cpf = (By.ID, 'pNumCnpjCpf')

    fistel = (By.ID, 'pNumFistel')

    indicativo = (By.ID, 'pIndicativo')

    nome = (By.ID, 't_NomeEntidade')

    email = (By.ID, 't_EndEletronico')

    rg = (By.ID, 'pf_NumIdentidade')

    orgexp = (By.ID, 'pf_SiglaOrgaoExp')

    nasc = (By.ID, 'pf_DataNascimento')

    ddd = (By.ID, 'tel_NumCodigoNacional0')

    fone = (By.ID, 'tel_NumTelefone0')

    cep = (By.ID, 'CodCep1')

    bt_cep = (By.ID, 'buscarEndereco')

    logr = (By.ID, 'EndLogradouro1')

    num = (By.ID, 'EndNumero1')

    comp = (By.ID, 'EndComplemento1')

    bairro = (By.ID, 'EndBairro1')

    uf = (By.ID, 'SiglaUf1')

    cidade = (By.ID, 'CodMunicipio1')

    confirmar = (By.ID, 'botaoFlatConfirmar')

    bt_dados = (By.ID, 'botaoFlatDadosComplementares')

    bt_fone = (By.ID, 'botaoFlatTelefones')

    bt_end = (By.ID, 'botaoFlatEndereço')

    submit = "submeterTela('http://sistemasnet/SEC/Chamada/Entidade.asp?SISQSModulo=&OP=A')"


class Scpx(object):

    Consulta = 'http://sistemasnet/scpx/Consulta/Tela.asp?SISQSmodulo=12714'

    Entidade.AlterarSituacao = "http://sistemasnet/scpx/Chamada/CadastroSRFRegularizado.asp?SISQSmodulo=16372"

    Entidade.Incluir = "http://sistemasnet/scpx/Chamada/Entidade.asp?OP=I&SISQSmodulo=12721"

    Estacao.Alterar = "http://sistemasnet/scpx/Estacao/Tela.asp?OP=A&SISQSmodulo=12724"

    Estacao.Excluir = "http://sistemasnet/scpx/Estacao/Tela.asp?OP=E&SISQSmodulo=12725"

    Estacao.Incluir = "http://sistemasnet/scpx/Estacao/Tela.asp?OP=I&SISQSmodulo=12723"

    Estacao.Licenciar = "http://sistemasnet/scpx/EstacaoLicenciar/Tela.asp?SISQSmodulo=12730"

    Licenca.Imprimir = "http://sistemasnet/scpx/Licenca/Tela.asp?SISQSmodulo=12727"


class Sigec(object):

    consulta = "http://sistemasnet/sigec/ConsultasGerais/SituacaoCadastral/tela.asp?SISQSmodulo=3748"

    cpf = (By.ID, "NumCNPJCPF")

    fistel = (By.ID, 'NumFistel')







