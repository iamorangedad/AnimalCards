# phase 5 roster: (id, 中文名, Wikipedia title, category, note); numbering 1001.. in this order
P = "宠物"; F = "农场"; G = "高原草原"; W = "森林"; S = "海洋"; B = "鸟类"; Rp = "爬行两栖"; I = "昆虫"
FW = "淡水鱼类"; AR = "蛛形甲壳"; PO = "极地生物"; DP = "深海生物"; EXT = "灭绝动物"
FL = "花卉"; TR = "树木"; CR = "农作物"; FV = "水果蔬菜"; DS = "沙漠植物"; AQ = "水生植物"; HB = "香料草药"
MU = "蘑菇"; MO = "霉菌酵母"; LI = "地衣"
KINGDOM = {FL: "植物", TR: "植物", CR: "植物", FV: "植物", DS: "植物", AQ: "植物", HB: "植物", MU: "真菌", MO: "真菌", LI: "真菌"}
def kingdom(cat): return KINGDOM.get(cat, "动物")
_raw = {
P: """rough-collie 粗毛柯利牧羊犬 Rough Collie 品种
dalmatian 斑点狗 Dalmatian dog 品种
bulldog 英国斗牛犬 Bulldog 品种
yorkie 约克夏梗 Yorkshire Terrier 品种
pomeranian 博美犬 Pomeranian dog 品种
schnauzer 迷你雪纳瑞 Miniature Schnauzer 品种
shih-tzu 西施犬 Shih Tzu 品种
akita 秋田犬 Akita (dog) 品种
greyhound 灵缇 Greyhound 品种
st-bernard 圣伯纳犬 St. Bernard (dog) 品种
abyssinian 阿比西尼亚猫 Abyssinian cat 品种
russian-blue 俄罗斯蓝猫 Russian Blue 品种
norw-forest 挪威森林猫 Norwegian Forest cat 品种
lionhead 狮子兔 Lionhead rabbit 品种
parrotlet 太平洋鹦哥 Pacific parrotlet
society-finch 十姊妹 Society finch
pearl-gourami 珍珠马甲 Pearl gourami
ghost-shrimp 玻璃虾 Palaemonetes paludosus
african-snail 非洲大蜗牛 Achatina fulica
gargoyle-gecko 石像鬼守宫 Rhacodactylus auriculatus""",
F: """gayal 大额牛 Gayal
zebu 瘤牛 Zebu
cochin 交趾鸡 Cochin chicken 品种
tibetan-mastiff 藏獒 Tibetan Mastiff 品种
mud-crab 锯缘青蟹 Scylla serrata
red-seabream 真鲷 Pagrus major
crucian 鲫鱼 Crucian carp
rohu 南亚野鲮 Rohu
iberian-pig 伊比利亚猪 Iberian pig 品种
toulouse-goose 图卢兹鹅 Toulouse goose 品种
italian-bee 意大利蜜蜂 Italian bee
hampshire-pig 汉普夏猪 Hampshire pig 品种
jacob-sheep 雅各布羊 Jacob sheep 品种
nubian-goat 努比亚山羊 Anglo-Nubian goat 品种
brown-swiss 瑞士褐牛 Brown Swiss cattle 品种
percheron 佩尔什马 Percheron 品种
plymouth-rock 芦花鸡 Plymouth Rock chicken 品种
cayuga 卡尤加鸭 Cayuga duck 品种
seabass 欧洲舌齿鲈 European seabass
ayu 香鱼 Ayu sweetfish""",
G: """black-wildebeest 白尾角马 Black wildebeest
roan-antelope 马羚 Roan antelope
blesbok 白纹牛羚 Bontebok
euro-hare 欧洲野兔 European hare
daurian-gs 达乌尔黄鼠 Daurian ground squirrel
patas 赤猴 Common patas monkey
wild-bactrian 野双峰驼 Wild Bactrian camel
lechwe 驴羚 Southern lechwe
oribi 侏羚 Oribi
steenbok 小岩羚 Steenbok
grants-gazelle 格氏瞪羚 Grant's gazelle
dama-gazelle 鹿瞪羚 Dama gazelle
scimitar-oryx 弯角剑羚 Scimitar oryx
jackrabbit 黑尾长耳大野兔 Black-tailed jackrabbit
swift-fox 敏狐 Swift fox
pampas-deer 潘帕斯鹿 Pampas deer
hairy-armadillo 大毛犰狳 Big hairy armadillo
giant-armadillo 大犰狳 Giant armadillo
steppe-polecat 艾鼬 Steppe polecat
sand-cat 沙猫 Sand cat
goitered 鹅喉羚 Goitered gazelle
przewalski-gaz 普氏原羚 Przewalski's gazelle
zokor 中华鼢鼠 Chinese zokor
brown-hyena 棕鬣狗 Brown hyena
common-duiker 灰小羚羊 Common duiker
13-lined 十三条纹黄鼠 Thirteen-lined ground squirrel
mule-deer 黑尾鹿 Mule deer
rhebok 灰羚 Grey rhebok
mountain-zebra 山斑马 Mountain zebra
black-footed-cat 黑足猫 Black-footed cat""",
W: """fisher 渔貂 Fisher (animal)
tree-kangaroo 古氏树袋鼠 Goodfellow's tree-kangaroo
sloth-2 霍氏二趾树懒 Hoffmann's two-toed sloth
black-howler 黑吼猴 Black howler
woolly-monkey 棕绒毛猴 Brown woolly monkey
banteng 爪哇野牛 Banteng
sambar 水鹿 Sambar deer
pere-david 麋鹿 Père David's deer
flying-squirrel 小飞鼠 Siberian flying squirrel
edible-dormouse 肥睡鼠 European edible dormouse
blue-duiker 蓝小羚羊 Blue duiker
black-muntjac 黑麂 Black muntjac
sumatran-orang 苏门答腊猩猩 Sumatran orangutan
eastern-gorilla 东部大猩猩 Eastern gorilla
siamang 合趾猿 Siamang
ruffed-lemur 黑白领狐猴 Black-and-white ruffed lemur
slender-loris 灰细懒猴 Gray slender loris
colugo 斑鼯猴 Sunda flying lemur
treeshrew 普通树鼩 Common treeshrew
large-civet 大灵猫 Large Indian civet
yt-marten 青鼬 Yellow-throated marten
leopard-cat 豹猫 Leopard cat
marbled-cat 云猫 Marbled cat
fishing-cat 渔猫 Fishing cat
tayra 狐鼬 Tayra
paca 斑点无尾刺豚鼠 Lowland paca
agouti 中美刺豚鼠 Central American agouti
bush-dog 薮犬 Bush dog
javan-rhino 爪哇犀 Javan rhinoceros
spectacled-bear 眼镜熊 Spectacled bear""",
S: """n-elephant-seal 北象海豹 Northern elephant seal
sa-fur-seal 南美毛皮海狮 South American fur seal
risso 灰海豚 Risso's dolphin
brydes 布氏鲸 Bryde's whale
blacktip 乌翅真鲨 Blacktip reef shark
lemon-shark 柠檬鲨 Lemon shark
sawfish 小齿锯鳐 Largetooth sawfish
giant-grouper 鞍带石斑鱼 Giant grouper
parrotfish 驼峰大鹦嘴鱼 Green humphead parrotfish
porcupinefish 密斑刺鲀 Diodon hystrix
picasso-trigger 叉斑锉鳞鲀 Picasso triggerfish
flying-fish 翱翔飞鱼 Exocoetus volitans
dwarf-seahorse 侏儒海马 Dwarf seahorse
sea-hare 加州海兔 Aplysia californica
sand-dollar 扁平楯海胆 Echinarachnius parma
sardine 沙丁鱼 European pilchard
mahi-mahi 鲯鳅 Mahi-mahi
albacore 长鳍金枪鱼 Albacore
wahoo 刺鲅 Wahoo
halibut 狭鳞庸鲽 Pacific halibut
wolffish 大西洋狼鱼 Atlantic wolffish
ribbontail 蓝斑条尾魟 Bluespotted ribbontail ray
zebra-shark 豹纹鲨 Zebra shark
wobbegong 叶须鲨 Tasselled wobbegong
cots 长棘海星 Crown-of-thorns starfish
anemone 公主海葵 Heteractis magnifica
brain-coral 迷宫脑珊瑚 Diploria labyrinthiformis
blue-dragon 海神海蛞蝓 Glaucus atlanticus
spanish-dancer 西班牙舞娘 Hexabranchus sanguineus
flamboyant 火焰乌贼 Flamboyant cuttlefish""",
B: """crowned-crane 灰冠鹤 Grey crowned crane
whooping 美洲鹤 Whooping crane
sarus 赤颈鹤 Sarus crane
bf-spoonbill 黑脸琵鹭 Black-faced spoonbill
little-egret 白鹭 Little egret
marabou 非洲秃鹳 Marabou stork
griffon 兀鹫 Griffon vulture
cattle-egret 牛背鹭 Cattle egret
lb-crow 大嘴乌鸦 Large-billed crow
bowerbird 缎蓝园丁鸟 Satin bowerbird
baya 黄胸织雀 Baya weaver
bee-hummer 吸蜜蜂鸟 Bee hummingbird
gannet 北鲣鸟 Northern gannet
great-frigate 白腹军舰鸟 Great frigatebird
grebe 凤头䴙䴘 Great crested grebe
coot 白骨顶 Eurasian coot
green-peafowl 绿孔雀 Green peafowl
nightjar 普通夜鹰 Grey nightjar
bn-oriole 黑枕黄鹂 Black-naped oriole
bird-of-paradise 大极乐鸟 Greater bird-of-paradise
hyacinth-macaw 紫蓝金刚鹦鹉 Hyacinth macaw
keel-toucan 厚嘴巨嘴鸟 Keel-billed toucan
moorhen 黑水鸡 Common moorhen
greylag 灰雁 Greylag goose
pintail 针尾鸭 Northern pintail
wood-duck 林鸳鸯 Wood duck
shelduck 翘鼻麻鸭 Common shelduck
avocet 反嘴鹬 Pied avocet
stilt 黑翅长脚鹬 Black-winged stilt
curlew 白腰杓鹬 Eurasian curlew
godwit 斑尾塍鹬 Bar-tailed godwit
red-knot 红腹滨鹬 Red knot
herring-gull 银鸥 European herring gull
bh-gull 红嘴鸥 Black-headed gull
burrowing-owl 穴小鸮 Burrowing owl
goshawk 苍鹰 Eurasian goshawk
stellers-eagle 虎头海雕 Steller's sea eagle
serpent-eagle 蛇雕 Crested serpent eagle
turkey-vulture 红头美洲鹫 Turkey vulture
wood-pigeon 斑尾林鸽 Common wood pigeon""",
Rp: """pond-turtle 欧洲泽龟 European pond turtle
siamese-croc 暹罗鳄 Siamese crocodile
american-croc 美洲鳄 American crocodile
chuckwalla 叩壁蜥 Common chuckwalla
giant-day-gecko 马岛大守宫 Phelsuma grandis
flying-dragon 飞蜥 Draco volans
five-lined 五线石龙子 Plestiodon fasciatus
glass-lizard 东部玻璃蜥 Eastern glass lizard
coral-snake 东部珊瑚蛇 Micrurus fulvius
sea-krait 蓝灰扁尾海蛇 Laticauda colubrina
bushmaster 南美巨蝮 Lachesis muta
pit-viper 白唇竹叶青 Trimeresurus albolabris
caecilian 环管蚓螈 Siphonops annulatus
firebelly 东方铃蟾 Oriental fire-bellied toad
glass-frog 网纹玻璃蛙 Hyalinobatrachium valerioi
indian-cobra 印度眼镜蛇 Indian cobra
banded-krait 金环蛇 Banded krait
coastal-taipan 太攀蛇 Coastal taipan
tiger-snake 虎蛇 Tiger snake
carpet-python 地毯蟒 Carpet python
rainbow-boa 彩虹蚺 Rainbow boa
leopard-frog 北美豹蛙 Northern leopard frog
wood-frog 北美林蛙 Wood frog
eastern-newt 红东螈 Eastern newt
spotted-sal 斑点钝口螈 Spotted salamander
titicaca-frog 的的喀喀湖蛙 Titicaca water frog
beaded-lizard 墨西哥毒蜥 Mexican beaded lizard
shingleback 松果蜥 Shingleback skink
armadillo-lizard 犰狳蜥 Armadillo girdled lizard
pig-nosed 猪鼻龟 Pig-nosed turtle""",
I: """honeypot 蜜罐蚁 Myrmecocystus mexicanus
weaver-ant 黄猄蚁 Oecophylla smaragdina
bull-dung 公牛嗡蜣螂 Onthophagus taurus
elephant-beetle 象犀金龟 Megasoma elephas
two-spot 二星瓢虫 Adalia bipunctata
jewel-beetle 彩虹吉丁 Chrysochroa fulgidissima
giraffe-weevil 长颈象鼻虫 Giraffe weevil
owl-butterfly 猫头鹰环蝶 Caligo
wild-silkmoth 野桑蚕 Bombyx mandarina
blue-damsel 长叶异痣蟌 Ischnura elegans
devil-mantis 魔花螳螂 Idolomantis diabolica
hissing-roach 马岛发声蟑螂 Gromphadorhina portentosa
backswimmer 仰泳蝽 Notonecta glauca
scorpionfly 蝎蛉 Panorpa communis
emma-cricket 大洋油葫芦 Teleogryllus oceanicus
glow-worm 欧洲萤 Lampyris noctiluca
oriental-hornet 东方胡蜂 Oriental hornet
velvet-ant 牛杀蚁蜂 Dasymutilla occidentalis
garden-tiger 豹灯蛾 Garden tiger moth
cecropia 刻克罗普斯蚕蛾 Hyalophora cecropia
ulysses 天堂凤蝶 Papilio ulysses
small-tortoise 荨麻蛱蝶 Small tortoiseshell
common-blue 普通眼灰蝶 Common blue
black-cicada 斑透翅蝉 Hyalessa maculaticollis
whirligig 豉甲 Whirligig beetle
atlas-beetle 南洋大兜虫 Chalcosoma atlas
dobsonfly 东部巨齿蛉 Corydalus cornutus
thrips 西花蓟马 Western flower thrips
mound-termite 好战大白蚁 Macrotermes bellicosus
thorn-bug 角蝉 Umbonia crassicornis""",
FW: """arapaima 巨骨舌鱼 Arapaima gigas
piranha 红腹食人鲳 Red-bellied piranha
electric-eel 电鳗 Electric eel
pirarucu-ray 南美淡水魟 Potamotrygon motoro
mekong-cat 湄公河巨鲶 Mekong giant catfish
wels 欧洲鲶 Wels catfish
pike 白斑狗鱼 Northern pike
perch 河鲈 European perch
zander 梭鲈 Zander
bass 大口黑鲈 Largemouth bass
bluegill 蓝鳃太阳鱼 Bluegill
trout-brown 河鳟 Brown trout
grayling 茴鱼 Thymallus thymallus
huchen 哲罗鲑 Hucho taimen
sturgeon-chinese 中华鲟 Chinese sturgeon
paddlefish 匙吻鲟 American paddlefish
gar 雀鳝 Alligator gar
bichir 恩氏多鳍鱼 Polypterus endlicheri
lungfish 澳洲肺鱼 Australian lungfish
african-lung 东非肺鱼 Marbled lungfish
archerfish 射水鱼 Banded archerfish
mudskipper 大弹涂鱼 Boleophthalmus pectinirostris
snakehead-giant 小盾鳢 Giant snakehead
tench 丁鱥 Tench
roach-fish 拟鲤 Common roach
barbel 鲃鱼 Common barbel
gudgeon 麦穗鱼 Pseudorasbora parva
medaka 青鳉 Japanese rice fish
killifish 蓝彩鳉 Nothobranchius furzeri
eel-european 欧洲鳗鲡 European eel""",
AR: """black-widow 黑寡妇蜘蛛 Latrodectus mactans
orb-weaver 金蛛 Argiope bruennichi
jumping-spider 孔雀跳蛛 Maratus volans
wolf-spider 狼蛛 Hogna carolinensis
goliath-spider 亚马逊巨人食鸟蛛 Goliath birdeater
huntsman 白额高脚蛛 Heteropoda venatoria
recluse 棕色隐士蜘蛛 Brown recluse spider
diving-bell 水蛛 Diving bell spider
trapdoor 活板门蛛 Ummidia
deathstalker 以色列金蝎 Deathstalker
bark-scorpion 亚利桑那树皮蝎 Arizona bark scorpion
whip-scorpion 鞭蝎 Mastigoproctus giganteus
camel-spider 避日蛛 Solifugae
tick 蓖麻硬蜱 Ixodes ricinus
dust-mite 屋尘螨 House dust mite
coconut-crab 椰子蟹 Coconut crab
red-crab 圣诞岛红蟹 Christmas Island red crab
fiddler 招潮蟹 Fiddler crab
king-crab 堪察加拟石蟹 Red king crab
blue-crab 美洲蓝蟹 Callinectes sapidus
pistol-shrimp 鼓虾 Alpheus heterochaelis
sea-louse 鲑疮痂鱼虱 Lepeophtheirus salmonis
pill-bug 鼠妇 Armadillidium vulgare
barnacle 茗荷 Lepas anatifera
copepod 飞马哲水蚤 Calanus finmarchicus""",
PO: """collared-lemming 环颈旅鼠 Northern collared lemming
stoat 白鼬 Stoat
ringed-seal 环斑海豹 Ringed seal
bearded-seal 髯海豹 Bearded seal
hooded-seal 冠海豹 Hooded seal
ross-seal 罗斯海豹 Ross seal
crabeater 食蟹海豹 Crabeater seal
ant-fur-seal 南极毛皮海狮 Antarctic fur seal
arctic-cod 北极鳕 Arctic cod
icefish 鳄冰鱼 Chionodraco hamatus
toothfish 南极犬牙鱼 Antarctic toothfish
chinstrap 帽带企鹅 Chinstrap penguin
gentoo 巴布亚企鹅 Gentoo penguin
macaroni 长冠企鹅 Macaroni penguin
snow-petrel 雪鹱 Snow petrel
ptarmigan 岩雷鸟 Rock ptarmigan
ivory-gull 白鸥 Ivory gull
gyrfalcon 矛隼 Gyrfalcon
ant-midge 南极摇蚊 Belgica antarctica
ant-minke 南极小须鲸 Antarctic minke whale""",
DP: """anglerfish 深海鮟鱇 Humpback anglerfish
gulper 宽咽鱼 Pelican eel
viperfish 斯氏蝰鱼 Sloane's viperfish
fangtooth 角高体金眼鲷 Common fangtooth
barreleye 后肛鱼 Macropinna microstoma
blobfish 软隐棘杜父鱼 Psychrolutes marcidus
lanternfish 灯笼鱼 Lanternfish
hatchetfish 银斧鱼 Marine hatchetfish
frilled-shark 皱鳃鲨 Frilled shark
goblin-shark 欧氏尖吻鲛 Goblin shark
cookiecutter 雪茄达摩鲨 Cookiecutter shark
vampire-squid 幽灵蛸 Vampire squid
dumbo 小飞象章鱼 Grimpoteuthis
colossal 大王酸浆鱿 Colossal squid
giant-isopod 大王具足虫 Bathynomus giganteus
yeti-crab 基瓦多雪人蟹 Kiwa hirsuta
tube-worm 巨型管虫 Riftia pachyptila
pompeii-worm 庞贝蠕虫 Pompeii worm
sea-spider 海蜘蛛 Colossendeis megalonyx
siphonophore 管水母 Praya dubia""",
EXT: """mammoth 真猛犸象 Woolly mammoth
thylacine 袋狼 Thylacine
passenger-pigeon 旅鸽 Passenger pigeon
steller-cow 大海牛 Steller's sea cow
quagga 斑驴 Quagga
great-auk 大海雀 Great auk
moa 南岛巨恐鸟 South Island giant moa
aurochs 原牛 Aurochs
baiji 白鱀豚 Baiji
golden-toad 金蟾蜍 Golden toad
carolina-parakeet 卡罗来纳鹦哥 Carolina parakeet
elephant-bird 象鸟 Aepyornis maximus
irish-elk 大角鹿 Irish elk
haast-eagle 哈斯特鹰 Haast's eagle
pinta-tortoise 平塔岛象龟 Pinta Island tortoise""",
FL: """lilac 欧丁香 Syringa vulgaris
hyacinth 风信子 Hyacinthus orientalis
gerbera 非洲菊 Gerbera jamesonii
freesia 小苍兰 Freesia
dahlia 大丽花 Dahlia pinnata
gladiolus 唐菖蒲 Gladiolus
anthurium 红掌 Anthurium andraeanum
calla 马蹄莲 Zantedeschia aethiopica
poinsettia 一品红 Poinsettia
bougainvillea 光叶子花 Bougainvillea glabra
wisteria 紫藤 Wisteria sinensis
wintersweet 蜡梅 Chimonanthus praecox
clivia 君子兰 Clivia miniata
cyclamen 仙客来 Cyclamen persicum
petunia 矮牵牛 Petunia
begonia 四季海棠 Begonia cucullata
zinnia 百日菊 Zinnia elegans
cornflower 矢车菊 Centaurea cyanus
forget-me-not 勿忘草 Myosotis scorpioides
lupine 多叶羽扇豆 Lupinus polyphyllus
bleeding-heart 荷包牡丹 Lamprocapnos spectabilis
crocus 番红花 Crocus sativus
amaryllis 孤挺花 Amaryllis belladonna
passionflower 西番莲 Passiflora caerulea
lantana 马缨丹 Lantana camara""",
TR: """white-birch 纸桦 Betula papyrifera
horse-chestnut 欧洲七叶树 Aesculus hippocastanum
ash 欧洲白蜡树 Fraxinus excelsior
elm 欧洲野榆 Ulmus minor
lime-tree 心叶椴 Tilia cordata
euro-aspen 欧洲山杨 Populus tremula
alder 欧洲桤木 Alnus glutinosa
hornbeam 欧洲鹅耳枥 Carpinus betulus
rowan 欧亚花楸 Sorbus aucuparia
juniper 欧洲刺柏 Juniperus communis
cypress 意大利柏木 Cupressus sempervirens
hemlock 加拿大铁杉 Tsuga canadensis
balsam-fir 香脂冷杉 Abies balsamea
ponderosa 西黄松 Pinus ponderosa
red-cedar 北美乔柏 Thuja plicata
s-magnolia 荷花木兰 Magnolia grandiflora
jacaranda 蓝花楹 Jacaranda mimosifolia
flame-tree 凤凰木 Delonix regia
red-cotton 木棉 Bombax ceiba
neem 印楝 Azadirachta indica
ebony 乌木 Diospyros ebenum
rosewood 降香黄檀 Dalbergia odorifera
jp-maple 鸡爪槭 Acer palmatum
cherry-plum 樱桃李 Prunus cerasifera
walnut 胡桃 Juglans regia""",
CR: """safflower 红花 Safflower
jute 黄麻 Jute
hemp 大麻 Hemp
sisal 剑麻 Sisal
teff 苔麸 Teff
spelt 斯佩尔特小麦 Spelt
amaranth 千穗谷 Amaranthus hypochondriacus
yam 山药 Dioscorea polystachya
cowpea 豇豆 Cowpea
pigeon-pea 木豆 Pigeon pea
white-lupin 白羽扇豆 Lupinus albus
stevia 甜叶菊 Stevia rebaudiana
vanilla 香荚兰 Vanilla planifolia
konjac 魔芋 Amorphophallus konjac
oil-camellia 油茶 Camellia oleifera""",
FV: """mangosteen 山竹 Purple mangosteen
rambutan 红毛丹 Rambutan
dragonfruit 火龙果 Pitaya
starfruit 杨桃 Carambola
guava 番石榴 Guava
passionfruit 鸡蛋果 Passiflora edulis
lychee-x 黄皮 Clausena lansium
loquat 枇杷 Loquat
bayberry 杨梅 Myrica rubra
plum 李 Prunus salicina
blackberry 黑莓 Blackberry
raspberry 树莓 Raspberry
cranberry 蔓越莓 Vaccinium macrocarpon
gooseberry 醋栗 Ribes uva-crispa
grapefruit 葡萄柚 Grapefruit
pomelo 柚 Pomelo
kumquat 金柑 Kumquat
quince 榅桲 Quince
broccoli 西兰花 Broccoli
cauliflower 花椰菜 Cauliflower
celery 芹菜 Celery
leek 韭葱 Leek
zucchini 西葫芦 Zucchini
okra 秋葵 Okra
artichoke 洋蓟 Artichoke""",
DS: """desert-willow 沙漠柳 Chilopsis linearis
ironwood 沙漠铁木 Olneya tesota
mesquite 腺牧豆树 Prosopis glandulosa
boojum 观峰玉 Fouquieria columnaris
fishhook 鱼钩仙人球 Ferocactus wislizeni
zygophyllum 霸王 Zygophyllum
calligonum 沙拐枣 Calligonum
camel-thorn 骆驼刺 Alhagi maurorum
pachypodium 非洲霸王树 Pachypodium lamerei
organ-pipe 茶柱仙人掌 Stenocereus thurberi""",
AQ: """hornwort 金鱼藻 Ceratophyllum demersum
hydrilla 黑藻 Hydrilla
elodea 伊乐藻 Elodea canadensis
waterwheel 貉藻 Aldrovanda vesiculosa
frogbit 欧洲水鳖 Hydrocharis morsus-ranae
salvinia 槐叶蘋 Salvinia natans
marsilea 田字蘋 Marsilea quadrifolia
sweet-flag 菖蒲 Acorus calamus
floating-heart 荇菜 Nymphoides peltata
pickerelweed 梭鱼草 Pontederia cordata""",
HB: """basil 罗勒 Basil
mint 薄荷 Mentha canadensis
rosemary 迷迭香 Rosemary
thyme 百里香 Thymus vulgaris
coriander 芫荽 Coriander
cinnamon 锡兰肉桂 Cinnamomum verum
black-pepper 胡椒 Black pepper
clove 丁子香 Syzygium aromaticum
nutmeg 肉豆蔻 Myristica fragrans
star-anise 八角 Illicium verum""",
MU: """parasol 高大环柄菇 Macrolepiota procera
golden-oyster 金顶侧耳 Pleurotus citrinopileatus
shimeji 斑玉蕈 Hypsizygus tessulatus
nameko 滑子菇 Pholiota microspora
jew-ear 毛木耳 Auricularia polytricha
blewit 紫丁香蘑 Lepista nuda
saffron-milk 松乳菇 Lactarius deliciosus
russula 毒红菇 Russula emetica
panther 豹斑鹅膏 Amanita pantherina
dest-angel-eu 鳞柄白鹅膏 Amanita virosa
galerina 纹缘盔孢伞 Galerina marginata
liberty-cap 暗蓝光盖伞 Psilocybe semilanceata
earthstar 尖顶地星 Geastrum triplex
birds-nest 白蛋巢菌 Crucibulum laeve
stinkhorn 白鬼笔 Phallus impudicus
jelly-ear 木耳状胶质菌 Tremella mesenterica
artist-conk 树舌灵芝 Ganoderma applanatum
chaga 桦褐孔菌 Inonotus obliquus
tinder 木蹄层孔菌 Fomes fomentarius
beefsteak 牛排菌 Fistulina hepatica
cordyceps-mil 蛹虫草 Cordyceps militaris
caesar 橙盖鹅膏 Amanita caesarea
hedgehog-m 卷缘齿菌 Hydnum repandum
inkcap-common 墨汁拟鬼伞 Coprinopsis atramentaria
scarlet-cup 红白毛杯菌 Sarcoscypha coccinea""",
MO: """aspergillus-fumi 烟曲霉 Aspergillus fumigatus
neurospora 粗糙脉孢菌 Neurospora crassa
trichoderma 里氏木霉 Trichoderma reesei
fusarium 禾谷镰刀菌 Fusarium graminearum
ergot 麦角菌 Claviceps purpurea""",
LI: """reindeer-lichen 鹿蕊 Cladonia rangiferina
iceland-moss 冰岛衣 Cetraria islandica
old-mans-beard 松萝 Usnea
map-lichen 地图衣 Rhizocarpon geographicum
xanthoria 石黄衣 Xanthoria parietina
lungwort 肺衣 Lobaria pulmonaria
rock-tripe 石耳 Umbilicaria
british-soldiers 英国兵石蕊 Cladonia cristatella
manna-lichen 栎扁枝衣 Oakmoss
dog-lichen 地卷 Peltigera""",
}
R5 = []
for cat, block in _raw.items():
    for line in block.strip().splitlines():
        parts = line.split(" ")
        i, cn = parts[0], parts[1]
        note = ""
        if parts[-1] == "品种": note = "品种"; parts = parts[:-1]
        R5.append((i, cn, " ".join(parts[2:]), cat, note))
N5 = {r[0]: 1001 + k for k, r in enumerate(R5)}
