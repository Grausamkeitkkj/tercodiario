import datetime
import random

data_atual = datetime.datetime.now()

dia_da_semana = data_atual.weekday()

def sorteia_santo():
    santo_sorteados = []
    for _ in range(3):
        santo_sorteado = random.choice(santos)
        santo_sorteados.append(santo_sorteado)
    return santo_sorteados

sinal_cruz = {
    0:['Pelo Sinal da Santa Cruz, livrai-nos,Deus Nosso Senhor, dos nossos, inimigos.\n'
    'Em nome do Pai, do Filhoe do Espiŕito Santo. Amém.\n'],
    1:['Per signum Sanctӕ Crucis de inimicis nostris libera nos, Domine Deus noster.\n'
    'In nomine Patris, et Filii, et Spiritus Sancti. Amen.\n']
}

inicio = {
    0:['Uno-me a todos os santos que estão no Céu, a todos os justos que estão sobre a terra, a todas as almas fiéis que estão nesse lugar.\n' 
    'Uno-me a Vós, meu Jesus, para louvar dignamnete Vossa Santa Mãe, e louvar-Vos a Vós nela e por Ela.\n'
    'Renuncio a todas as distrações que me vierem durante este Terço que quero recitar com modéstia, atenção e devoção, como se fosse o último de minha vida.\n'
    'Ofereço-Vos, Santíssima Trindade, este Credo para honrar os mistérios todos de nossa fé;\n'
    'este Pai Nosso e estas Três Ave Marias, para honrar a unidade de Vossa essência e a trindade de Vossas pessoas.\n'
    'Pedimo-vos uma fé viva, uma esperança firma e uma caridade ardente. Amém.\n'],
    1:['Iúngo me óminibus Sánctis qui sunt in coelo, ómnibus iústis qui sunt in terra, ómnibus ánimis fídis qui sun un hoc lóco. Tíbi me iúngo, mi Iésu\n'
    'ad laudándum Sánctam Mátrem Túam, ut laudándum Te in Ea et per Eam. Renúntio ómnibus distractiónibus quæ míhi veníre in recitatónie vólo cum atentióne\n'
    'et devotioné ut si ésset últimus vít́æ meæ. Tibi offérimus, Sancta Trínitas, hunc Sýmbolum Fídei ad honorádum ómnia mystéria nóstra fídei, hunc Pátrem Nóstrum\n'
    'et has tres Ave Marias ad honorándum unitátem esséntiam Túam et Trinitátem Pérsonas Tuas. Péto Te fídem víviam, firma spem et ardéntem caritátem. Ámen.\n']
}

simbolo_apostolos = {
    0:['Creio em Deus, Pai todo-poderoso, Criador do céu e da terra;\n'
    'E em Jesus Cristo, seu único filho, nosso Senhor\n'
    'que foi concebido pelo poder do Espírito Santo;\n'
    'nasceu da Virgem Maria;\n'
    'padeceu sob Pôncio Pilatos,\n'
    'foi crucificado, morto e sepultado;\n'
    'desceu ao infernos;\n'
    'ressuscitou ao terceiro dia;\n'
    'subiu aos Céus;\n'
    'está sentado à direita de Deus Pai todo-poderoso;\n'
    'de onde há de vir a julgar os vivos e os mortos.\n'
    'Creio no Espírito Santo;\n'
    'na santa Igreja Católica;\n'
    'na comunhão dos Santos,\n'
    'na remissão dos pecados;\n'
    'na ressurreição da carne;\n'
    'e na vida eterna. Amém.\n'],
    1:['Credo in Deum, Patrem Omnipoténtem, Creatórem cæli et terræ.\n'
    'Et in Jesum Christum, Fílium eius únicum, Dóminùm nostrum:\n'
    'qui concéptus est de Spíritu Sancto,\n'
    'natus ex María Vírgine,\n' 
    'passus sub Pontio Piláto,\n'
    'crucifíxus, mórtuus, et sepúltus:\n'
    'descéndit ad ínferos;\n'
    'tértia die resurréxit a mórtuis;\n'
    'ascéndit ad cælos;\n'
    'sedet ad déxteram Dei Patris omnipoténtis:\n'
    'inde ventúrus est judicáre vivos et mórtuos.\n'
    'Credo in Spíritum Sanctum,\n'
    'sanctam Ecclésiam cathólicam,\n'
    'Sanctórum communionem,\n'
    'remissiónem peccatórum,\n'
    'carnis resurrectiónem,\n'
    'vitam ætérnam. Amén.\n']
}

louvemos = (
    '1 Pai Nosso\n' 
    'Louvemos a Maria, Filha bem amada do Pai Eterno.\n'
    '1 Ave Maria\n' 
    'Louvemos a Maria, Mãe admirável de Deus Filho.\n'
    '1 Ave Maria\n'
    'Louvemos a Maria, Esposa fidelíssima de Deus Espírito Santo.\n'
    '1 Ave Maria\n'
)

oferecimento_terco = (
    'Santíssima Virgem, Mãe de Deus, eu Vos ofereço este terço em desagravo do Santíssimo Coração de Nosso Senhor Jesus Cristo,'
    ' Vosso Filho, e em desagravo ao Vosso Coração Imaculado; e pelas intenções que Vos apresento:\n'
    '(Intenções particulares a seguir)\n'
    'Intenções do Santo Padre:\n'
    '●Exaltação da Fé Católica.\n'
    '●Propagação da Fé.\n'
    '●Extirpação das Heresias.\n'
    '●Conversão dos pecadores.\n'
    '●Paz e concórdia entre os paíeses cristãos.\n')

pai_nosso = {
    0:['Pai nosso, que estais no Céu,\n'
    'santificado seja o vosso nome,\n'
    'venha nós ao vosso reino,\n'
    'seja feita a vossa vontade,\n'
    'assim na terra, como no céu.\n'
    'R.O pão nosso de cada dia nos dai hoje,\n'
    'perdoai-nos as nossas dívidas,\n'
    'assim como nós perdoamos os nossos devedores,\n'
    'e não nos deixeis cair em tentação,\n'
    'mas livrai-nos do mal. Amém\n'],
    1:['Pater noster, qui es un cælis,\n'
    'sanctificétur nomem tuum,\n'
    'advéniat regnum tuum,\n'
    'fiat volúntuas tua,\n'
    'sicut in cælo, et in terra.\n'
    'R.Panem nostrum quotidiánum da nobis hódie.\n'
    'Et dimítte nobis débita nostra,\n'
    'sicut et nos demíttumus debitóribus nostris.\n'
    'Et ne nos indúcas in tentatiónem.\n'
    'Sed líbera nos a malo. Amén.\n']
}

ave_maria = {
    0:['Ave Maria cheia de graça,\n'
    'o Senhor é convosco,\n'
    'bendita sois Vós entre as mulheres,\n'
    'e bendito é o fruto do vosso ventre, Jesus\n'
    'R.Santa Maria, Mãe de Deus,\n'
    'rogai por nós pecadores,\n'
    'agora e na hora da nossa morte. Amém\n\n'],
    1:['Ave Maria, grátia plena,\n'
    'Dóminus tecum,\n'
    'benedícta tu in muliéribus,\n'
    'et benedíctus fructus venris tui Iésus.\n'
    'R.Sancta María, Mater Dei,\n'
    'ora pro nobis peccatóribus,\n'
    'nunc et in hora mortis nostræ. Amén.\n']
}

gloria = {
    0:['Glória ao Pai, ao Filho e ao Espírito Santo.\n'
    'R.Assim como era no princípio, agora e sempre, e por todos os séculos dos séculos. Amém.\n'],
    1:['Glória Patri, et Fílio, et Spíritui Sancto.\n'
    'R.Sicut erat in princípio, et nunc, et sempre, et in a sǽcula sæculórum. Ámen.\n']
}

maria_concebida = {
    0:['Ó Maria concebida sem pecado.\n'
    'R.Rogai por nós que recorremos a vós.\n'],
    1:['O Maria sine labe concepta.\n'
    'R.Ora pro nobis qui confugimus ad te.\n']
}

o_meu_jesus = {
    0:['Ó meu Jesus, perdoai-nos e livrai-nos do fogo do inferno,\n'
    'levai as almas todas para o céu\n'
    'e socorrei principalmente as que mais precisarem.\n'],
    1:['Ó mi Iésu. Ignósce nóbis, libera nos ab ígne inferni,\n'
    'ad ad cælum tráhe ómnes ánimas,\n' 
    'præsáertim máxime indigéntes.\n']
    }

oremos = {
    0:['Eu Vos saúdo, Maria, Filha bem-amada do eterno Padre, Mãe admirável do Filho, Esposa mui fiel do Espírito Santo, templo augusto da Santíssima Trindade; eu Vos saúdo, soberana Princesa,\n'
    'na quem tudo está submisso no Céu e na Terra; eu Vos saúdo, seguro refúgio dos pecadores, que jamais repelistes pessoa alguma. Pecador que sou, me prostro a vossos pés, e Vos peço de me obter de Jesus,\n'
    'vosso amado Filho, a contrição e o perdão de todos os meus pecados, e a divina sabedoria. Eu me consagro todo a Vós, com tudo que possuo. Eu Vos tomo, hoje, por minha Mãe e Senhora. Tratai-me, pois,\n'
    'como o último de vossos filhos e o mais obediente de vossos escravos. Atendei, minha Princesa, atendei aos suspiros dum coração que deseja amar-Vos e servir-Vos fielmente. Que ninguém diga que,\n'
    'entre todos que a Vós recorreram, seja eu o primeiro desamparado. Ó minha esperança, ó minha vida, ó minha fiel e Imaculada Virgem Maria, defendei-me, nutri-me, escutai-me, instruí-me, salvai-me. Assim seja.\n'],
    1:['Ave Maria, filia dilectíssima Ætérni Pátris, Mater Admirábilis Fílii, Spónsa fidelíssima Spíritus Sáncti, Templo augústum Sanctissimæ Trinitátis. Ave, Fília Regis! Ómnia tíbi subiécta sunt in coelo et in terra.\n'
    'Ave, refúgium tutum peccatórum, Dómina misericordiæ! Tu númquam a te áliquem repéllis. Etiamsi peccátor coram te prosterno et te precor ut a tuo Dilécto Fílio Iésu obtíneas contritiónem veniamque ómnium meórum peccatórum,\n'
    'atque Divínam Sapiéntiam. Tíbi ex toto me dono et ómnia mea. Te elígo, Mátrem Dominámque méam, ab hódie. Hábe me ínfimum tuórum filiórum et plus oboediéntem mancipórum.\n'
    'Áudi suspiratiónes córdis méi quod vult te amáre et tibi fidéliter servíre. Nin fiat ut ex ómnibus íllis qui ad e venniut ego non exáudiar. O spes mea! O víta mea! O fídelis et Immaculáta Vírgo Maria!\n'
    'Exáudi me, defende me, nútri me, erúdi me et sálva me! Ámen.\n\n']
}

salve_rainha = {
    0:['Salve, Rainha,\n'
    'mãe de misericórdia,\n' 
    'vida, doçura, esperança nossa, salve!\n'
    'A Vós bradamos,\n'
    'os degredados filhos de Eva.\n' 
    'A Vós suspiramos, gemendo e chorando\n' 
    'neste vale de lágrimas.\n'
    'Eia, pois, advogada nossa,\n' 
    'esses Vossos olhos misericordiosos\n' 
    'a nós volvei.\n'
    'E, depois deste desterro,\n'
    'nos mostrai Jesus, bendito fruto\n' 
    'do Vosso ventre.\n'
    'Ó clemente, ó piedosa,\n' 
    'ó doce Virgem Maria.\n\n'
    'Rogai por nós, Santa Mãe de Deus,\n'
    'R.para que sejamos dignos das promessas de Cristo.\n'],
    1:['Salve, Regína,\n'
    'Mater misericórdiæ,\n'
    'vita, dulcédo,\n'
    'et spes nostra, salve.\n'
    'Ad te clamámus,\n'
    'éxsules fílii Hevæ,\n'
    'Ad te suspirámus,\n'
    'geméntes et flentes,\n'
    'in hac lacrimárum valle.\n'
    'Eia, ergo, advocáta nostra,\n'
    'illos tuos misericórdes óculos ad nos convérte.\n'
    'Et Iesum, benedíctum fructum ventris tui,\n'
    'nobis post hoc exílium osténde.\n'
    'O clemens, O pia, O dulcis Virgo Maria.\n\n'
    'Ora pro nobis sancta Dei Génetrix.\n'
    'R.Ut digni efficiámur promissiónibus Christi.\n\n']
}

ladainha = {
    0:['Senhor, tende piedade de nós.\n'
    'Jesus Cristo, tende piedade de nós.\n'
    'Senhor, tende piedade de nós.\n'
    'Jesus Cristo, ouvi-nos.\n'
    'Jesus Cristo, atendei-nos.\n\n'
    '(Repita as frases)'

    'Pai celeste que sois Deus, tende piedade de nós.\n'
    'Filho, Redentor do mundo, que sois Deus, tende piedade de nós.\n'
    'Espírito Santo, que sois Deus, tende piedade de nós.\n'
    'Santíssima Trindade, que sois um só Deus, tende piedade de nós.\n\n'

    'Santa Maria, rogai por nós.\n'
    'Santa Mãe de Deus, rogai por nós.\n'
    'Santa Virgem das Virgens, rogai por nós.\n'
    'Mãe de Jesus Cristo, rogai por nós.\n'
    'Mãe da Igreja, rogai por nós.\n'
    'Mãe da divina graça, rogai por nós.\n'
    'Mãe puríssima, rogai por nós.\n'
    'Mãe castíssima, rogai por nós.\n'
    'Mãe imaculada, rogai por nós.\n'
    'Mãe intacta, rogai por nós.\n'
    'Mãe amável, rogai por nós.\n'
    'Mãe admirável, rogai por nós.\n'
    'Mãe do bom conselho, rogai por nós.\n'
    'Mãe do Criador, rogai por nós.\n'
    'Mãe do Salvador, rogai por nós.\n'
    'Virgem prudentíssima, rogai por nós.\n'
    'Virgem venerável, rogai por nós.\n'
    'Virgem louvável, rogai por nós.\n'
    'Virgem poderosa, rogai por nós.\n'
    'Virgem clemente, rogai por nós.\n'
    'Virgem fiel, rogai por nós.\n'
    'Espelho de justiça, rogai por nós.\n'
    'Sede de sabedoria, rogai por nós.\n'
    'Causa da nossa alegria, rogai por nós.\n'
    'Vaso espiritual, rogai por nós.\n'
    'Vaso honorífico, rogai por nós.\n'
    'Vaso insígne de devoção, rogai por nós.\n'
    'Rosa mística, rogai por nós.\n'
    'Torre de David, rogai por nós.\n'
    'Torre de marfim, rogai por nós.\n'
    'Casa de ouro, rogai por nós.\n'
    'Arca da aliança, rogai por nós.\n'
    'Porta do céu, rogai por nós.\n'
    'Estrela da manhã, rogai por nós.\n'
    'Saúde dos enfermos, rogai por nós.\n'
    'Refúgio dos pecadores, rogai por nós.\n'
    'Consoladora dos aflitos, rogai por nós.\n'
    'Auxílio dos cristãos, rogai por nós.\n'
    'Rainha dos anjos, rogai por nós.\n'
    'Rainha dos patriarcas, rogai por nós.\n'
    'Rainha dos profetas, rogai por nós.\n'
    'Rainha dos apóstolos, rogai por nós.\n'
    'Rainha dos mártires, rogai por nós.\n'
    'Rainha dos confessores, rogai por nós.\n'
    'Rainha das virgens, rogai por nós.\n'
    'Rainha de todos os santos, rogai por nós.\n'
    'Rainha concebida sem pecado original, rogai por nós.\n'
    'Rainha elevada ao céu, rogai por nós.\n'
    'Rainha do sacratíssimo Rosário, rogai por nós.\n'
    'Rainha da paz, rogai por nós.\n\n'
    
    'Cordeiro de Deus, que tirais os pecados do mundo, perdoai-nos Senhor.\n'
    'Cordeiro de Deus, que tirais os pecados do mundo, ouvi-nos Senhor.\n'
    'Cordeiro de Deus, que tirais os pecados do mundo, tende piedade de nós.\n'

    'Rogai por nós, Santa Mãe de Deus,\n'
    'R. Para que sejamos dignos das promessas de Cristo.\n\n'],
    1:['Kyrie, eléison.\n'
    'Christe, eléison.\n'
    'Kyrie, eléison.\n'
    'Christe, áudi nos.\n'
    'Christe, exáudi nos.\n\n'
    
    'Pater de cælis, Deus, miserére nobis.\n'
    'Fili, Redémptor mundi, Deus, miserére nobis.\n'
    'Spíritus Sancte, Deus, miserére nobis.\n'
    'Sancta Trínitas, unus Deus, miserére nobis.\n\n'

    'Sancta Maria, ora pro nobis.\n'
    'Sancta Dei Génitrix, ora pro nobis.\n'
    'Sancta Virgo vírginum, ora pro nobis.\n'
    'Mater Christi, ora pro nobis.\n'
    'Mater Ecclésiæ, ora pro nobis.\n'
    'Mater divinæ grátiæ, ora pro nobis.\n'
    'Mater puríssima, ora pro nobis.\n'
    'Mater castíssima, ora pro nobis.\n'
    'Mater invioláta, ora pro nobis.\n'
    'Mater intemeráta ora pro nobis.\n'
    'Mater amábilis, ora pro nobis.\n'
    'Mater admirábilis, ora pro nobis.\n'
    'Mater boni consilii, ora pro nobis.\n'
    'Mater Creatóris, ora pro nobis.\n'
    'Mater Salvatoris, ora pro nobis.\n'
    'Virgo prudentíssima, ora pro nobis.\n'
    'Virgo veneranda, ora pro nobis.\n'
    'Virgo prædicánda, ora pro nobis.\n'
    'Virgo potens, ora pro nobis.\n'
    'Virgo clemens, ora pro nobis.\n'
    'Virgo fidélis, ora pro nobis.\n'
    'Speculum justitiæ, ora pro nobis.\n'
    'Sedes sapiéntiæ, ora pro nobis.\n'
    'Causa nostræ lætitiæ, ora pro nobis.\n'
    'Vas spirituále, ora pro nobis.\n'
    'Vas honorábile, ora pro nobis.\n'
    'Vas insígne devotiónis, ora pro nobis.\n'
    'Rosa mystica, ora pro nobis.\n'
    'Turris Davídica, ora pro nobis.\n'
    'Turris ebúrnea, ora pro nobis.\n'
    'Domus áurea, ora pro nobis.\n'
    'Fœderis arca, ora pro nobis.\n'
    'Jánua cæli, ora pro nobis.\n'
    'Stella matutina, ora pro nobis.\n'
    'Salus infirmórum, ora pro nobis.\n'
    'Refúgium peccatórum, ora pro nobis.\n'
    'Consolátrix afflictórum, ora pro nobis.\n'
    'Auxílium christianórum, ora pro nobis.\n'
    'Regína angelórum, ora pro nobis.\n'
    'Regína patriarchárum, ora pro nobis.\n'
    'Regína prophetárum, ora pro nobis.\n'
    'Regína apostolórum, ora pro nobis.\n'
    'Regína mártyrum, ora pro nobis.\n'
    'Regína confessórum, ora pro nobis.\n'
    'Regína vírginum, ora pro nobis.\n'
    'Regína sanctórum ómnium, ora pro nobis.\n'
    'Regína sine labe originali concépta, ora pro nobis.\n'
    'Regina in cælum assumpta, ora pro nobis.\n'
    'Regína sacratissimi Rosárii, ora pro nobis.\n'
    'Regína pacis, ora pro nobis.\n\n'
    
    'Agnus Dei, qui tollis peccáta mundi, parce nobis, Dómine.\n'
    'Agnus Dei, qui tollis peccáta mundi, exáudi nos, Dómine.\n'
    'Agnus Dei, qui tollis peccáta mundi, miserére nobis.\n'
    
    'Ora pro nobis, sancta Dei Génitrix.\n'
    'R. Ut digni efficiámur romissiónibus Christi.\n']
}

oremos2 = {
    0:['Senhor Deus, Vos suplicamos, concedei aos Vossos servos o gozo da perpétua saúde da alma e do corpo,\n' 
    'e pela gloriosa intercessão da B. Maria, sempre Virgem, permiti que sejamos livres das tristezas do tempo presente\n' 
    'e alcancemos o gozo da alegria eterna.\n'
    'Por Cristo, nosso Senhor. Amém.\n\n'],
    1:['Concéde nos fámulos tuos, quæsumus, Dómine Deus,\n'
    'perpétua mentis et córporis sanitáte gaudére: et gloriósa beatæ Mariæ semper Virginis intercessióne,\n'
    'a præsénti liberári tristítia, et ætérna pérfrui lætitia.\n'
    'Per Christum Dóminum nostrum. Ámen.\n\n']
}

oracao_sao_jose = {
    0:['Bem-aventurado S. José, a vós\n'
    'recorremos na nossa tribulação, e,\n'
    'havendo implorado da Santíssima\n'
    'Virgem, vossa esposa, pedimos\n'
    'também com toda a confiança a\n'
    'vossa protecção. Por aquele afecto\n'
    'que vos uniu à Imaculada Virgem\n'
    'Mãe de Deus e pelo paternal amor\n'
    'que consagraste ao Menino Jesus,\n'
    'vos rogamos e suplicamos que\n'
    'olheis benigno para a herança que\n'
    'Jesus Cristo nos adquiriu com o Seu\n'
    'sangue, e que nos assistais nas\n'
    'nossas necessidades com o vosso\n'
    'poder e auxílio. Protegei, ó\n'
    'providentíssimo guarda da Sagrada\n'
    'Família, os filhos escolhidos de\n'
    'Jesus Cristo, preservai-nos, ó pai\n'
    'amantíssimo, de todo o contágio\n'
    'das doutrinas erroneas e de\n'
    'corrupção; sede-nos propício e\n'
    'assisti-nos do alto do céu, ó nosso\n'
    'poderoso libertador, neste combate\n'
    'contra o poder das trevas; e, assim\n'
    'como outrora livrastes o Menino\n'
    'Jesus do perigo da morte, assim\n'
    'também, hoje, defendei a santa\n'
    'Igreja de Deus das ciladas dos seus\n'
    'inimigos e de todas as\n'
    'adversidades. E a cada um de nós\n'
    'concedei a vossa constante\n'
    'protecção, a fim de que, imitando-vos\n' 
    'e fortalecidos com o vosso auxílio, possamos\n'
    'viver santamente, morrer piamente e\n'
    'alcançar no céu a bem-aventurança\n'
    'eterna. Amem.\n\n'],
    1:['Ad te beáte Joseph, in tribulatióne\n'
    'nostra confúgimus, atque,\n'
    'imploráto Sponsæ tuæ sanctíssimæ\n'
    'auxílio, patrocínium quoque tuum\n'
    'fidenter expóscimus. Per eam,\n'
    'quæsumus, quæ te cum immaculáta\n'
    'Vírgine Dei Genitríce coniúnxit,\n'
    'caritátem, perque patérnum, quo\n'
    'Púerum Iesum amplexus\n'
    'amórem, súpplices deprecámur, ut\n'
    'ad hereditátem, quam Iesus\n'
    'Christus acquisívit Sánguine suo,\n'
    'benígnus respícias,\n'
    'es, ac necessitatibus nostris tua virtúte et\n'
    'ope succúrras. Tuére, o Custos\n'
    'providentíssime divína Família,\n'
    'Iesu Christi sóbolem eléctam;\n'
    'próhibe a nobis, amantíssime Pater,\n'
    'omnem errórum ac corruptelárum\n'
    'luem; propítius nobis, sospítator\n'
    'noster fortíssime, in hoc cum\n'
    'potestáte tenebrárum certámine e\n'
    'cælo adésto; et sicut olim Púerum\n'
    'Iesum e summo eripuísti vitre\n'
    'discrimine, ita nunc Ecclesiam\n'
    'sanctam Dei ab hostílibus insidiis\n'
    'atque ab omni adversitáte défende:\n'
    'nosque síngulos perpétuo tege\n'
    'patrocínio, ut ad tui exémplar et ope\n'
    'tua suffúlti, sancte vívere, pie émori,\n'
    'sempiternámque\n'
    'in cælis beatitúdinem ássequi possímus. Ámen.\n\n']
}

santos = [
    'Santo Antônio',
    'São Francisco de Assis',
    'Santa Teresa de Ávila',
    'São João Bosco',
    'Santa Clara de Assis',
    'Santo Agostinho',
    'São Tomás de Aquino',
    'São José de Cupertino',
    'Santa Catarina de Sena',
    'São Pedro',
    'São Paulo',
    'Santa Maria Madalena',
    'São João Batista',
    'Santa Cecília',
    'Santo Inácio de Loyola',
    'Santa Teresinha do Menino Jesus',
    'São Sebastião',
    'Santa Rita de Cássia',
    'São Bento',
    'Santo Expedito',
    'Santa Edwiges',
    'São Miguel Arcanjo',
    'São Gabriel Arcanjo',
    'Santa Mônica',
    'São Gregório Magno',
    'São Francisco Xavier',
    'Santa Luzia',
    'Santo André',
    'São Mateus',
    'São Lucas',
    'São Marcos',
    'São João',
    'São Tiago',
    'São Judas Tadeu',
    'Santa Faustina',
    'Santo Eustáquio',
    'Santa Gertrudes',
    'São Vicente de Paulo',
    'São Luís Gonzaga',
    'Santa Isabel da Hungria',
    'São Pedro de Alcântara',
    'São João da Cruz',
    'São Felipe Néri',
    'Santa Teresa de Lisieux',
    'São Camilo de Lélis',
    'São José de Anchieta',
    'Santa Ângela de Foligno',
    'São Luís Beltrão',
    'Santo Afonso Maria de Ligório',
    'Santa Rosa de Lima',
    'São Geraldo Majella',
    'São Roque',
    'São João Maria Vianney',
    'Santa Teresa de Calcutá',
    'São Damião de Molokai',
    'Santo Ambrósio',
    'Santo Atanásio',
    'São Justino',
    'São Bernardo de Claraval',
    'Santa Genoveva',
    'São Patrício',
    'Santa Olímpia',
    'Santo Isidoro de Sevilha',
    'Santa Joana d\'Arc',
    'São Tomé',
    'Santa Bárbara',
    'São Valentim',
    'São Benedito',
    'São Martinho de Tours',
    'Santa Verônica',
    'São Pedro Canísio',
    'Santo Hilário de Poitiers',
    'São Gregório de Narek',
    'São Leão Magno',
    'São Bernardo de Menton',
    'Santa Margarida Maria Alacoque',
    'São Francisco de Sales',
    'Santo Toríbio de Mogrovejo',
    'Santa Juliana de Norwich',
    'São Norberto',
    'São Nuno de Santa Maria',
    'Santo André Corsini',
    'São Pancrácio',
    'Santa Gema Galgani',
    'São Simão Stock',
    'Santa Teresa de Avila',
    'Santo Antônio Maria Zaccaria',
    'São Roque González',
    'Santo Agostinho Zhao Rong',
    'São Francisco Solano',
    'Santo Alberto Hurtado',
    'São Domingos Sávio',
    'Santa Faustina Kowalska',
    'São Maximiliano Kolbe',
    'Santa Teresa Benedita da Cruz',
    'São Padre Pio',
    'São João Paulo II',
    'Santa Irmã Dulce',
    'São Óscar Romero',
    'Santa Teresa de Calcutá',
    'São Francisco Marto',
    'Santa Jacinta Marto',
    'Santa Lúcia dos Santos',
    'Santa Madre Teresa de Calcutá',
    'São João Gabriel Perboyre',
    'Santa Maria Goretti',
    'Santa Teresinha de Lisieux',
    'São Gaspar del Bufalo',
    'Santo Antônio de Sant Anna Galvão',
    'São José de Anchieta',
    'Santo André Kim',
    'São Paulo Miki',
    'Santa Teresa de Calcutá',
    'Santo Estêvão',
    'São Francisco Xavier',
    'Santo Inácio de Loyola',
    'Santa Tereza de Calcutá',
    'São Sebastião',
    'São João Bosco',
    'Santa Bernadette Soubirous',
    'São Francisco de Assis',
    'São Judas Tadeu',
    'Santa Isabel de Portugal',
    'São Martinho de Porres',
    'Santa Teresinha do Menino Jesus',
    'São Vicente Ferrer',
    'Santa Águeda',
    'São Jorge',
    'Santa Inês',
    'São Valentim',
    'Santa Escolástica',
    'São Bento',
    'São Bernardino de Siena',
    'Santa Ana',
    'São Zacarias',
    'Santa Joana d\'Arc',
    'São Matias',
    'Santa Isabel da Hungria',
    'Santo Egídio',
    'Santa Teresa de Ávila',
    'São Luís Beltrão',
    'Santa Mônica',
    'São Maximiliano Kolbe',
    'Santo Isidoro de Sevilha',
    'Santa Genoveva',
    'São João Maria Vianney',
    'Santa Catarina de Alexandria',
    'São Bonifácio',
    'Santa Brígida',
    'São Cipriano',
    'Santa Rita de Cássia',
    'São Jerônimo',
    'Santa Madalena de Canossa',
    'São Teotônio',
    'Santa Brígida da Suécia',
    'São Gregório de Nazianzo',
    'Santa Francisca Romana',
    'São Beda',
    'Santa Anastácia',
    'São Martinho de Tours',
    'Santa Júlia Billiart',
    'São Joaquim',
    'Santa Ana',
    'São Lourenço de Brindes',
    'Santa Catarina Labouré',
    'São Pedro Canísio',
    'Santa Escolástica',
    'São Francisco de Sales',
    'Santa Verônica Giuliani',
    'São José',
    'Santa Margarida de Cortona',
]

misterios_gozosos = {
    0:['Primeiro Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta primeira dezena, em honra a vossa Encarnação no seio de Maria; e vos pedimos, por esse mistério, e por sua intercessão uma profunda humildade. Assim seja.\n'
    '1 Pai Nosso\n'
    '10 Ave Marias, segurando as 10 contas menores que se seguem.\n'
    '1 Glória ao Pai.\n'
    '1 Ó Meu Jesus\n'
    f'{", ".join(sorteia_santo())}\n'
    '(Ao dizer o nome dos santos, responda com "Rogai por nós")'
    '(Seguir da mesma forma nos outros mistérios)\n'
    'Graças ao mistério da Encarnação, descei em nossas almas. Assim seja.\n\n'
    
    'Segundo Mistério\n'
    'Nos vos oferecemos, Senhor Jesus, esta segunda dezena, em honra da visitação de vossa santa Mãe à sua prima santa Isabel e da santificação de São João Batista;\n'
    'e vos pedimos, por esse mistério e pela intercessão de vossa Mãe Santíssima, a caridade para com o nosso próximo. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da visitação, descei em nossas almas. Assim seja.\n\n'
    
    'Terceiro Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta terceira dezena, em honra ao vosso nascimento no estábulo de Belém; e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima,\n'
    'o desapego dos bens terrenos e ao amor a pobreza. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério do nascimento de Jesus, descei em nossas almas. Assim seja.\n\n'
    
    'Quarto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta quarta dezena, em honra a vossa apresentação ao templo, e da purificação de Maria;\n'
    'e vos pedimos, por este mistério e por sua intercessão, uma grande pureza de corpo de alma. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da purificação descei, descei em nossas almas. Assim seja.\n\n'

    'Quinto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta quinta dezena, em honra ao vosso reencontro por Maria; e vos pedimos, por este mistério; e por sua intercessão, a verdadeira sabedoria. Assim Seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério do reencontro de Jesus, descei em nossas almas. Assim seja.\n\n'],

    1:['De annuntoatióne Ángeli Mariæ Vírgini\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honorém Incarnatiónis Tuæ in in sínu Mariæ Vírginis.\n'
    'A te pétimus, hoc mystério et intercessióne Éius, profúndam humilitátem. Amén.'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n' 
    'Grátia mystérii Chrísti Incarnatiónis, descénde in nostras ánimas. Amén\n\n'

    'De visitatióne Mariæ Sanctíssimæ ad sanctam Elisabeth\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Visitatiónis Tuæ Sanctíssimæ Mátris ad Sanctam Elisabeth et sanctificatiónis Sancti Iohanni Batístæ.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, perféctam caritátem ad nóstrum próximum. Amén.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mysterii visitatiónis, descénde in nostras ánimas. Amén.\n\n'

    'De navitáte Iésu in stábulo béthlehem\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ santaæ Nativitátis in stábulo Béthlehem.\n'
    'A te pétimus, hoc mystério et intercessioné Tuæ Sanctíssimæ Mátris, abdúcere me bonórum múndi, despicátum divitiárum et amórem paupertátis. Amén.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Nativitátis Iésu, descénde in nostras ánimas. Amén.\n\n'

    'Maria et Isopeh osténdunt Iésum in témplo\n'
    'Tibi offérimus, Ddómine Iésum, hanc decádem in honórem Præsentatiónis Tuæ in Témplum et Purificatiónis Beatæ Mariæ Vírginis.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, mágnam puritátem ánime et córporis. Amén.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátiæ mysteriórum Presentatiónis et Purificatiónis, descéndite in nostrar ánimas. Amén.\n\n'

    'De inventione Iésu in témplo\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ Inventiónis a Mariæ Vírgine in medio doctórum.\n'
    'A te pétimus, hoc mystério et intercessióne Éius, véram sapiéntiam. Ámen\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Inventiónis Iésu, descénde in nostras ánimas. Ámen.']
}

misterios_dolorosos = {
    0:['Primeiro Mistério\z\n'
    'Nós vos oferecemos, Senhor Jesus, esta primeira dezena, em honra a vossa agonia mortal no Jardim das Oliveiras;'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima, a contrição de nossos pecados. Assim seja.\n'
    '(Pai Nosso, Ave-Maria, Glória, Ó Meu Jesus.)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da agonia de Jesus, descei em nossas almas. Assim seja.\n\n'
    
    'Segundo Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta segunda dezena, em honra a vossa sangrenta flagelação;\n'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe santíssima, a mortificação de nossos sentidos. Assim seja.\n'
    '(Pai Nosso, Ave-Maria, Glória, Ó Meu Jesus.)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da flagelação de Jesus, descei em nossas almas. Assim seja.\n\n'
    
    'Terceiro Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta terceira dezena, em honra de vossa coroação de espinhos;\n'
    'e vos pedimos por este mistério e pela intercessão de vossa Mãe Santíssima, o desprezo do mundo. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da coroação de espinhos, descei em nossas almas. Assim seja.\n\n'
    
    'Quarto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta quarta dezena, em honra do carregamento da Cruz;\n'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima, a paciência em todas as nossas cruzes. Assim seja.\n'
    '(Pai Nosso, Ave-Marias, Glória, Ó Meu Jesus.)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério do carregamento da cruz, descei em nossas almas. Assim seja.\n\n'
    
    'Quinto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta quinta dezena, em honra a vossa crucificação e morte ignominiosa sobre o calvário;\n'
    'e vos pedimos por este mistério e pela intercessão de vossa Mãe Santíssima, a conversão dos pecadores, a perseverança dos justos e o alívio das almas do purgatório. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da crucificação de Jesus descei em nossas almas. Assim seja.\n\n'],

    1:['De Iésu moréntis últimis augústiis in gethsémani\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ agóniæ mortalis in Hórto Olivárum.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, contritónis peccatórum nostrórum. Amén.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Agoniæ Iésu in Gethsémani, descénde in nostras ánimas. Amén.\n\n'

    'De verberatióne Iésu\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ crudélæ Verberatiónis.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, plénam refrenatiónem nostrórum sénsuum. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Verberatiónis Iésu, descénde in nostras ánimas. Amén.\n'

    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ crudélis inductiónis coronæ spinórum.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, mágnam contemptiónem múndi. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii coronatiónis spinórum, descénde in nostras ánimas. Ámen.\n\n'

    'De itínere ad Montem Calvárium\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tui itíneris oneráti cruce ad Móntem Calvárium.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, mágnampatiéntiam in ómnibus nóstris crúcibus. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii itíneris Iésu oneráti cruce ad Calvárium, descénde in nostras ánimas. Ámen.\n\n'

    'De Iésu qui crucifixus, spíritum tráddit\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ crucifixiónis et mórtis ignominósæ in Montem Calvárium.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, perseverántiam iustórum et solácium animárum Purgatórii. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii crucificatiónis et Mórtis Iésu, descénde in nostras ánimas. Ámen.\n\n']
}

misterios_gloriosos = {
    0:['Primeiro Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta primeira dezena, em honra a vossa ressurreição gloriosa;\n'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima, o amor a Deus e o fervor ao vosso serviço. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da ressurreição, descei em nossas almas. Assim seja.\n\n'
    
    'Segundo Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta segunda dezena, em honra a vossa triunfante ascensão;\n'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima, um ardente desejo do céu, nossa cara pátria. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da ascensão descei, em nossas almas. Assim seja.\n\n'
    
    'Terceiro Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta terceira dezena, em honra do mistério de Pentecostes;\n'
    'e vos pedimos, por este mistério e pela intercessão de vossa Mãe Santíssima, a descida do Espírito Santo em nossas almas. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério de Pentecostes, descei em nossas almas. Assim seja.\n\n'
    
    'Quarto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus, esta quarta dezena, em honra da ressurreição e triunfal assunção de vossa Mãe ao céu;\n'
    'e vos pedimos, por este mistério e por sua intercessão, uma terna devoção a tão boa mãe. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças ao mistério da assunção descei em nossas almas. Assim seja.\n\n'
    
    'Quinto Mistério\n'
    'Nós vos oferecemos, Senhor Jesus esta quinta dezena, em honra da coroação gloriosa de vossa Mãe Santíssima no céu;\n'
    'e vos pedimos, por este mistério e por sua intercessão, a perseverança na graça e a coroa da glória. Assim seja.\n'
    '(Pai Nosso, Ave Maria, Glória, Ó Meu Jesus)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Graças aos mistérios da coroação gloriosa de Maria, descei em nossas almas. Assim seja.\n\n'],

    1:['De Iésu Resurrectióne\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ gloriósæ Resurretiónis.\n'
    'A te pétimus, hocmystério et intercessióne Tuæ Sanctíssimæ Mátris, amórem Déi et divínum ardórem Tui sáncti ministérii. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Resurretiónis, descénde in nostras ánimas. Ámen.\n\n'

    'De Iésu ascenttióne in cælum\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem Tuæ Ascentiónis triunphális in coelum.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, férvidum desidérium coeli, nóstræ diléctæ pátriæ. Ámen\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Ascentiónis Iésu, descénde in nostras ánimas. Ámen\n\n'

    'De descénsu spíritus Sancti in Cenáculum\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem mystérii Pentecóstes.\n'
    'A te pétimus, hoc mystério et intercessióne Tuæ Sanctíssimæ Mátris, descénsum Spíritus Sancti in nostras ánimas. Ámen.\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Pentecóstes, descénde in nostras ánimas. Ámen'

    'De assumptióne Mariæ Vírginis in Cælum\n'
    'Tibi offérimus, Dómine Iésu, hanc decádem in honórem resurrectiónis et triumphális Assumptiónis Tuæ Sanctíssimæ Mátris in coelum.\n'
    'A te pétimus, hoc mystério et intercessióne Éius,téneram devotiónis erga tam bónam Mátrem. Ámen\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii Assumptiónis Mariæ, descénde in nostras ánimas. Ámen.'

    'De Coronæ inductióne Mariæ Regínæ cæeli et terræ\n'
    'decádem in honórem corónæ inductiónis glóriæ Tuæ Sanctíssmæ Mátris in coelo.\n'
    'A te pétimus, hoc mystério et intercessióne Éius, perseverántiam in grátia et corónam glóriæ. Ámen\n'
    '(Pater noster, Ave Maria, Gloria Patri, O mi Iésu)\n'
    f'{", ".join(sorteia_santo())}\n'
    'Grátia mystérii gloriósæ inductiónis coronæ Mariæ, descénde in nostras ánimas. Ámen.']
}

def terco_latim():
    print(pai_nosso[1][0])
    print(ave_maria[1][0])
    print(sinal_cruz[1][0])
    print(inicio[1][0])
    print(simbolo_apostolos[1][0])
    print(louvemos[1][0])
    print(gloria[1][0])
    print(o_meu_jesus[1][0])
    print(maria_concebida[1][0])
    print(oferecimento_terco[0][0])
        
    if dia_da_semana in [0, 3]:
        print(misterios_gozosos[1][0])
    elif dia_da_semana in [1, 4]:
        print(misterios_dolorosos[1][0])
    elif dia_da_semana in [2, 5, 6]:
        print(misterios_gloriosos[1][0])
            
    print(oremos[1][0])
    print(salve_rainha[1][0])
    print(ladainha[1][0])
    print(oremos2[1][0])
    print(oracao_sao_jose[1][0])

def terco_portugues():
    
    print(pai_nosso[0][0])
    print(ave_maria[0][0])
    print(sinal_cruz[0][0])
    print(inicio[0][0])
    print(simbolo_apostolos[0][0])
    print(louvemos)
    print(gloria[0][0])
    print(o_meu_jesus[0][0])
    print(maria_concebida[0][0])
    print(oferecimento_terco)
    if dia_da_semana in [0,3]:
        print(misterios_gozosos[0][0])
    elif dia_da_semana in [1,4]:
        print(misterios_dolorosos[0][0])
    elif dia_da_semana in [2,5,6]:
        print(misterios_gloriosos[0][0])
    print(oremos[0][0])
    print(salve_rainha[0][0])
    print(ladainha[0][0])
    print(oremos2[0][0])
    print(oracao_sao_jose[0][0])

while True:
    escolha = int(input('Deseja o terço em latim ou em português?\n'
                        '1 - Latim\n'
                        '2 - Português\n'))
    
    if escolha == 1:
        terco_latim()
        break 
    elif escolha == 2:
        terco_portugues()
        break
    else:
        print("Escolha inválida. Por favor, digite 1 ou 2.")