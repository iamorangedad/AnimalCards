# phase 4 roster: (id, 中文名, Wikipedia title, category, note) ; numbering 401.. in this order
# kingdom by category: animals (8 cats), 植物 (6 cats), 真菌 (2 cats)
P = "宠物"; F = "农场"; G = "高原草原"; W = "森林"; S = "海洋"; B = "鸟类"; Rp = "爬行两栖"; I = "昆虫"
FL = "花卉"; TR = "树木"; CR = "农作物"; FV = "水果蔬菜"; DS = "沙漠植物"; AQ = "水生植物"; MU = "蘑菇"; MO = "霉菌酵母"
KINGDOM = {FL: "植物", TR: "植物", CR: "植物", FV: "植物", DS: "植物", AQ: "植物", MU: "真菌", MO: "真菌"}
def kingdom(cat): return KINGDOM.get(cat, "动物")
_raw = {
P: """golden-retriever 金毛寻回犬 Golden Retriever 品种
labrador 拉布拉多寻回犬 Labrador Retriever 品种
gsd 德国牧羊犬 German Shepherd 品种
poodle 贵宾犬 Poodle 品种
chihuahua 吉娃娃 Chihuahua (dog) 品种
shiba 柴犬 Shiba Inu 品种
husky 西伯利亚哈士奇 Siberian Husky 品种
corgi 彭布罗克柯基犬 Pembroke Welsh Corgi 品种
dachshund 腊肠犬 Dachshund 品种
beagle 比格犬 Beagle 品种
pug 巴哥犬 Pug 品种
frenchie 法国斗牛犬 French Bulldog 品种
samoyed 萨摩耶犬 Samoyed dog 品种
persian 波斯猫 Persian cat 品种
siamese 暹罗猫 Siamese cat 品种
maine-coon 缅因猫 Maine Coon 品种
british-sh 英国短毛猫 British Shorthair 品种
ragdoll 布偶猫 Ragdoll 品种
sphynx 斯芬克斯猫 Sphynx cat 品种
scottish-fold 苏格兰折耳猫 Scottish Fold 品种
bengal-cat 孟加拉猫 Bengal cat 品种
holland-lop 荷兰垂耳兔 Holland Lop 品种
java-sparrow 文鸟 Java sparrow
gouldian 七彩文鸟 Gouldian finch
eclectus 红胁绿鹦鹉 Moluccan eclectus
lorikeet 彩虹吸蜜鹦鹉 Rainbow lorikeet
ringneck 红领绿鹦鹉 Rose-ringed parakeet
molly 茉莉鱼 Poecilia sphenops
swordtail 剑尾鱼 Green swordtail
cardinal-tetra 宝莲灯鱼 Cardinal tetra
arowana 美丽硬仆骨舌鱼 Asian arowana
corydoras 青铜鼠鱼 Corydoras aeneus
dwarf-gourami 丽丽鱼 Dwarf gourami
tiger-barb 虎皮鱼 Tiger barb
white-cloud 唐鱼 White cloud mountain minnow
red-foot 红腿陆龟 Red-footed tortoise
hermann 赫曼陆龟 Hermann's tortoise
blue-tongue 东部蓝舌石龙子 Eastern blue-tongued lizard
kingsnake 加州王蛇 California kingsnake
hognose 西部猪鼻蛇 Western hognose snake
pacman 钟角蛙 Argentine horned frog
whites-frog 老爷树蛙 Australian green tree frog
rose-tarantula 智利红玫瑰蜘蛛 Grammostola rosea
emperor-scorpion 帝王蝎 Emperor scorpion
hermit-crab 加勒比海寄居蟹 Coenobita clypeatus""",
F: """angus 安格斯牛 Angus cattle 品种
jersey 娟姗牛 Jersey cattle 品种
wagyu 和牛 Wagyu 品种
simmental 西门塔尔牛 Simmental cattle 品种
charolais 夏洛来牛 Charolais cattle 品种
duroc 杜洛克猪 Duroc pig 品种
berkshire 巴克夏猪 Berkshire pig 品种
large-white 大白猪 Large White pig 品种
meishan 梅山猪 Meishan pig 品种
leghorn 来航鸡 Leghorn chicken 品种
silkie 丝羽乌骨鸡 Silkie 品种
rir 罗德岛红鸡 Rhode Island Red 品种
brahma 婆罗门鸡 Brahma chicken 品种
pekin 北京鸭 American Pekin 品种
runner 印度跑鸭 Indian Runner duck 品种
suffolk 萨福克羊 Suffolk sheep 品种
dorper 杜泊羊 Dorper 品种
boer 波尔山羊 Boer goat 品种
saanen 萨能山羊 Saanen goat 品种
angora-goat 安哥拉山羊 Angora goat 品种
cashmere 绒山羊 Cashmere goat 品种
angora-rabbit 安哥拉兔 Angora rabbit 品种
nz-rabbit 新西兰兔 New Zealand rabbit 品种
shire 夏尔马 Shire horse 品种
arabian 阿拉伯马 Arabian horse 品种
mongol-horse 蒙古马 Mongolian horse 品种
shetland 设得兰矮马 Shetland pony 品种
thoroughbred 纯血马 Thoroughbred 品种
clydesdale 克莱兹代尔马 Clydesdale horse 品种
pyrenees 大白熊犬 Great Pyrenees 品种
aussie 澳大利亚牧羊犬 Australian Shepherd 品种
yellow-croaker 大黄鱼 Larimichthys crocea
mandarin-fish 鳜鱼 Siniperca chuatsi
wuchang-bream 团头鲂 Megalobrama amblycephala
yellow-catfish 黄颡鱼 Tachysurus fulvidraco
snakehead 乌鳢 Northern snakehead
barramundi 尖吻鲈 Barramundi
turbot 大菱鲆 Turbot
sib-sturgeon 西伯利亚鲟 Siberian sturgeon
gilthead 金头鲷 Gilt-head bream
abalone 皱纹盘鲍 Haliotis discus
scallop 虾夷扇贝 Mizuhopecten yessoensis
blue-mussel 紫贻贝 Blue mussel
manila-clam 菲律宾蛤仔 Venerupis philippinarum
tiger-prawn 斑节对虾 Penaeus monodon""",
G: """fennec 耳廓狐 Fennec fox
gerenuk 长颈羚 Gerenuk
topi 转角牛羚 Topi
hartebeest 狷羚 Hartebeest
waterbuck 水羚 Waterbuck
kudu 大捻角羚 Greater kudu
sable-antelope 黑马羚 Sable antelope
ar-oryx 阿拉伯大羚羊 Arabian oryx
addax 旋角羚 Addax
dikdik 柯氏犬羚 Kirk's dik-dik
klipspringer 山羚 Klipspringer
bat-eared 大耳狐 Bat-eared fox
aardwolf 土狼 Aardwolf
striped-hyena 条纹鬣狗 Striped hyena
bb-jackal 黑背胡狼 Black-backed jackal
golden-jackal 亚洲胡狼 Golden jackal
eth-wolf 埃塞俄比亚狼 Ethiopian wolf
maned-wolf 鬃狼 Maned wolf
dingo 澳洲野犬 Dingo
corsac 沙狐 Corsac fox
hyrax 南非岩蹄兔 Rock hyrax
mole-rat 裸鼹形鼠 Naked mole-rat
mtn-goat 雪羊 Mountain goat
bighorn 加拿大盘羊 Bighorn sheep
ibex 羱羊 Alpine ibex
chamois 臆羚 Chamois
tahr 喜马拉雅塔尔羊 Himalayan tahr
markhor 捻角山羊 Markhor
wl-deer 白唇鹿 White-lipped deer
gelada 狮尾狒 Gelada
hamadryas 阿拉伯狒狒 Hamadryas baboon
wombat 袋熊 Common wombat
grey-kangaroo 东部灰袋鼠 Eastern grey kangaroo
bilby 兔耳袋狸 Greater bilby
viscacha 平原兔鼠 Plains viscacha
mara 巴塔哥尼亚豚鼠 Patagonian mara
bf-ferret 黑足鼬 Black-footed ferret
am-badger 美洲獾 American badger
muskox 麝牛 Muskox
arctic-fox 北极狐 Arctic fox
arctic-hare 北极兔 Arctic hare
lemming 挪威旅鼠 Norway lemming
onager 亚洲野驴 Onager
alp-marmot 阿尔卑斯旱獭 Alpine marmot
porcupine 冠豪猪 Crested porcupine""",
W: """fossa 马岛獴 Fossa (animal)
aye-aye 指猴 Aye-aye
sifaka 维氏冕狐猴 Verreaux's sifaka
lion-tamarin 金狮狨 Golden lion tamarin
marmoset 普通狨 Common marmoset
howler 鬃毛吼猴 Mantled howler
spider-monkey 黑掌蜘蛛猴 Geoffroy's spider monkey
capuchin 白面卷尾猴 White-faced capuchin
squirrel-monkey 松鼠猴 Common squirrel monkey
douc 红腿白臀叶猴 Red-shanked douc
hainan-gibbon 海南长臂猿 Hainan black crested gibbon
guereza 东黑白疣猴 Mantled guereza
bongo 紫羚 Bongo (antelope)
forest-elephant 非洲森林象 African forest elephant
pygmy-hippo 倭河马 Pygmy hippopotamus
river-hog 红河猪 Red river hog
ocelot 虎猫 Ocelot
cougar 美洲狮 Cougar
bobcat 短尾猫 Bobcat
kinkajou 蜜熊 Kinkajou
coati 南美浣熊 South American coati
opossum 北美负鼠 Virginia opossum
na-porcupine 北美豪猪 North American porcupine
grey-squirrel 东部灰松鼠 Eastern gray squirrel
elk 北美马鹿 Elk
pine-marten 松貂 European pine marten
wildcat 欧洲野猫 European wildcat
wisent 欧洲野牛 European bison
dormouse 榛睡鼠 Hazel dormouse
mole 欧洲鼹 European mole
musk-deer 原麝 Siberian musk deer
water-deer 獐 Water deer
dhole 豺 Dhole
binturong 熊狸 Binturong
sloth-bear 懒熊 Sloth bear
gaur 印度野牛 Gaur
sumatran-rhino 苏门答腊犀 Sumatran rhinoceros
tas-devil 袋獾 Tasmanian devil
possum 帚尾袋貂 Common brushtail possum
platypus 鸭嘴兽 Platypus
echidna 短吻针鼹 Short-beaked echidna
raccoon-dog 貉 Common raccoon dog
serow 日本鬣羚 Japanese serow
vampire-bat 普通吸血蝠 Common vampire bat
indian-rhino 印度犀 Indian rhinoceros""",
S: """stingray 美洲魟 Southern stingray
eagle-ray 斑点鹞鲼 Spotted eagle ray
basking-shark 姥鲨 Basking shark
greenland-shark 小头睡鲨 Greenland shark
mako 尖吻鲭鲨 Shortfin mako shark
blue-shark 大青鲨 Blue shark
nurse-shark 铰口鲨 Nurse shark
thresher 弧形长尾鲨 Common thresher
herring 大西洋鲱 Atlantic herring
mackerel 大西洋鲭 Atlantic mackerel
anchovy 欧洲鳀 European anchovy
skipjack 鲣 Skipjack tuna
yellowfin 黄鳍金枪鱼 Yellowfin tuna
coelacanth 矛尾鱼 West Indian Ocean coelacanth
oarfish 皇带鱼 Giant oarfish
moorish-idol 镰鱼 Moorish idol
mandarinfish 花斑连鳍䲗 Mandarinfish
fugu 红鳍东方鲀 Takifugu rubripes
sailfish 平鳍旗鱼 Indo-Pacific sailfish
blue-marlin 大西洋蓝枪鱼 Atlantic blue marlin
barracuda 大鳞魣 Great barracuda
napoleon 波纹唇鱼 Humphead wrasse
goliath-grouper 伊氏石斑鱼 Atlantic goliath grouper
seadragon 叶海龙 Leafy seadragon
box-jelly 澳洲箱水母 Chironex fleckeri
lions-mane 北极霞水母 Lion's mane jellyfish
blue-ring 大蓝环章鱼 Greater blue-ringed octopus
gp-octopus 北太平洋巨型章鱼 Giant Pacific octopus
humboldt 茎柔鱼 Humboldt squid
krill 南极大磷虾 Antarctic krill
staghorn 鹿角珊瑚 Staghorn coral
fin-whale 长须鲸 Fin whale
minke 小须鲸 Common minke whale
gray-whale 灰鲸 Gray whale
bowhead 弓头鲸 Bowhead whale
right-whale 北大西洋露脊鲸 North Atlantic right whale
vaquita 加湾鼠海豚 Vaquita
spinner 长吻原海豚 Spinner dolphin
pilot-whale 长肢领航鲸 Long-finned pilot whale
steller 北海狮 Steller sea lion
elephant-seal 南象海豹 Southern elephant seal
weddell 威德尔海豹 Weddell seal
harp-seal 竖琴海豹 Harp seal
monk-seal 夏威夷僧海豹 Hawaiian monk seal
olive-ridley 太平洋丽龟 Olive ridley sea turtle""",
B: """house-sparrow 家麻雀 House sparrow
blue-jay 冠蓝鸦 Blue jay
am-robin 旅鸫 American robin
blackbird 欧乌鸫 Common blackbird
goldfinch 红额金翅雀 European goldfinch
gh-owl 美洲雕鸮 Great horned owl
tawny-owl 灰林鸮 Tawny owl
carrion-crow 小嘴乌鸦 Carrion crow
eur-jay 松鸦 Eurasian jay
blue-tit 蓝山雀 Eurasian blue tit
nightingale 新疆歌鸲 Common nightingale
skylark 云雀 Eurasian skylark
bulbul 白头鹎 Light-vented bulbul
blue-magpie 红嘴蓝鹊 Red-billed blue magpie
osprey 鹗 Osprey
rt-hawk 红尾鵟 Red-tailed hawk
kestrel 红隼 Common kestrel
harpy 角雕 Harpy eagle
ph-eagle 菲律宾鹰 Philippine eagle
bearded-vulture 胡兀鹫 Bearded vulture
mute-swan 疣鼻天鹅 Mute swan
canada-goose 加拿大黑雁 Canada goose
common-crane 灰鹤 Common crane
black-swan 黑天鹅 Black swan
scarlet-ibis 美洲红鹮 Scarlet ibis
spoonbill 粉红琵鹭 Roseate spoonbill
cormorant 普通鸬鹚 Great cormorant
brown-pelican 褐鹈鹕 Brown pelican
booby 蓝脚鲣鸟 Blue-footed booby
frigatebird 华丽军舰鸟 Magnificent frigatebird
loon 普通潜鸟 Common loon
adelie 阿德利企鹅 Adélie penguin
af-penguin 非洲企鹅 African penguin
kakapo 鸮鹦鹉 Kākāpō
kea 啄羊鹦鹉 Kea
scarlet-macaw 绯红金刚鹦鹉 Scarlet macaw
lyrebird 华丽琴鸟 Superb lyrebird
hornbill 双角犀鸟 Great hornbill
quetzal 凤尾绿咬鹃 Resplendent quetzal
fairywren 华丽细尾鹩莺 Superb fairywren
roadrunner 走鹃 Greater roadrunner
capercaillie 西方松鸡 Western capercaillie
bee-eater 黄喉蜂虎 European bee-eater
swift 普通雨燕 Common swift
dodo 渡渡鸟 Dodo""",
Rp: """box-turtle 卡罗莱纳箱龟 Eastern box turtle
common-snapper 拟鳄龟 Common snapping turtle
bighead-turtle 平胸龟 Big-headed turtle
golden-coin 三线闭壳龟 Golden coin turtle
star-tortoise 印度星龟 Indian star tortoise
leopard-tortoise 豹纹陆龟 Leopard tortoise
gopher 穴居地鼠龟 Gopher tortoise
jacksons 杰克森变色龙 Jackson's chameleon
parsons 国王变色龙 Parson's chameleon
day-gecko 金粉守宫 Gold dust day gecko
horned-lizard 德州角蜥 Texas horned lizard
savannah-mon 草原巨蜥 Savannah monitor
perentie 眼斑巨蜥 Perentie
rhino-iguana 犀牛鬣蜥 Rhinoceros iguana
ctenosaur 黑栉尾蜥 Black spiny-tailed iguana
slowworm 蛇蜥 Slowworm
sand-lizard 捷蜥蜴 Sand lizard
tegu 阿根廷黑白泰加蜥 Argentine black and white tegu
crocodile-lizard 鳄蜥 Chinese crocodile lizard
boa 红尾蚺 Boa constrictor
adder 极北蝰 Vipera berus
brown-snake 东部拟眼镜蛇 Eastern brown snake
puff-adder 鼓腹咝蝰 Puff adder
sidewinder 角响尾蛇 Crotalus cerastes
gt-python 绿树蟒 Green tree python
emerald-boa 翡翠树蚺 Emerald tree boa
russells 圆斑蝰 Russell's viper
flying-snake 天堂金花蛇 Chrysopelea paradisi
spectacled 眼镜凯门鳄 Spectacled caiman
black-caiman 黑凯门鳄 Black caiman
mugger 泽鳄 Mugger crocodile
jp-giant-sal 日本大鲵 Japanese giant salamander
hellbender 美洲大鲵 Hellbender
tiger-sal 虎纹钝口螈 Tiger salamander
smooth-newt 普通欧螈 Smooth newt
crested-newt 欧洲冠欧螈 Northern crested newt
common-frog 林蛙 Common frog
tomato-frog 番茄蛙 Dyscophus antongilii
af-bullfrog 非洲牛蛙 African bullfrog
pipa 负子蟾 Common Surinam toad
wallace-frog 黑蹼树蛙 Wallace's flying frog
darwin-frog 达尔文蛙 Darwin's frog
asiatic-toad 中华蟾蜍 Asiatic toad
strawberry-frog 草莓箭毒蛙 Strawberry poison-dart frog
mudpuppy 泥螈 Common mudpuppy""",
I: """red-admiral 优红蛱蝶 Red admiral
peacock-bfly 孔雀蛱蝶 Aglais io
brimstone 钩粉蝶 Gonepteryx rhamni
glasswing 透翅蝶 Greta oto
qa-birdwing 亚历山大鸟翼凤蝶 Queen Alexandra's birdwing
oakleaf 枯叶蛱蝶 Kallima inachus
zebra-longwing 斑马长翅蛱蝶 Heliconius charithonia
hummingbird-moth 小豆长喙天蛾 Hummingbird hawk-moth
deaths-head 鬼脸天蛾 Acherontia atropos
spongy-moth 舞毒蛾 Lymantria dispar
peppered-moth 桦尺蛾 Peppered moth
rosy-maple 粉红枫蛾 Dryocampa rubicunda
armyworm 草地贪夜蛾 Spodoptera frugiperda
tiger-beetle 绿虎甲 Cicindela campestris
bombardier 气步甲 Bombardier beetle
jp-beetle 日本弧丽金龟 Japanese beetle
alb 光肩星天牛 Asian long-horned beetle
mealworm 黄粉虫 Tenebrio molitor
titan 泰坦天牛 Titanus giganteus
palm-weevil 红棕象甲 Rhynchophorus ferrugineus
rice-weevil 米象 Sitophilus oryzae
diving-beetle 黄缘龙虱 Dytiscus marginalis
harlequin 异色瓢虫 Harmonia axyridis
cerana 东方蜜蜂 Apis cerana
carpenter-bee 紫木蜂 Xylocopa violacea
paper-wasp 欧洲长脚胡蜂 Polistes dominula
german-wasp 德国黄胡蜂 Vespula germanica
tarantula-hawk 蛛鹰 Pepsis grossa
leafcutter 切叶蚁 Atta cephalotes
army-ant 游蚁 Eciton burchellii
orchid-mantis 兰花螳螂 Hymenopus coronatus
walking-leaf 叶䗛 Phyllium giganteum
wandering-glider 黄蜻 Pantala flavescens
demoiselle 条纹色蟌 Calopteryx splendens
bush-cricket 大绿螽斯 Tettigonia viridissima
head-louse 头虱 Head louse
cochineal 胭脂虫 Cochineal
lac-insect 紫胶虫 Kerria lacca
giant-water-bug 田鳖 Lethocerus
hoverfly 黑带食蚜蝇 Episyrphus balteatus
anopheles 冈比亚按蚊 Anopheles gambiae
tiger-mosquito 白纹伊蚊 Aedes albopictus
greenbottle 丝光绿蝇 Lucilia sericata
cn-mantis 中华大刀螳 Tenodera sinensis
bogong 博贡夜蛾 Bogong moth""",
FL: """china-rose 月季 Rosa chinensis
tree-peony 牡丹 Paeonia suffruticosa
herb-peony 芍药 Paeonia lactiflora
chrysanthemum 菊花 Chrysanthemum morifolium
plum-blossom 梅 Prunus mume
spring-orchid 春兰 Cymbidium goeringii
phalaenopsis 蝴蝶兰 Phalaenopsis aphrodite
sunflower 向日葵 Common sunflower
tulip 郁金香 Tulipa gesneriana
easter-lily 麝香百合 Lilium longiflorum
narcissus 水仙 Narcissus tazetta
camellia 山茶 Camellia japonica
azalea 映山红 Rhododendron simsii
osmanthus 桂花 Osmanthus fragrans
jasmine 茉莉花 Jasminum sambac
gardenia 栀子 Gardenia jasminoides
hydrangea 绣球 Hydrangea macrophylla
lavender 狭叶薰衣草 Lavandula angustifolia
carnation 香石竹 Dianthus caryophyllus
daisy 雏菊 Bellis perennis
dandelion 药用蒲公英 Taraxacum officinale
corn-poppy 虞美人 Papaver rhoeas
cosmos 秋英 Cosmos bipinnatus
marigold 万寿菊 Tagetes erecta
morning-glory 牵牛 Ipomoea nil
hibiscus 朱槿 Hibiscus rosa-sinensis
yulan 玉兰 Magnolia denudata
iris 德国鸢尾 Iris × germanica
wild-pansy 三色堇 Viola tricolor
foxglove 毛地黄 Digitalis purpurea
lily-valley 铃兰 Lily of the valley
oleander 夹竹桃 Nerium
rafflesia 大王花 Rafflesia arnoldii
titan-arum 巨魔芋 Amorphophallus titanum
flytrap 捕蝇草 Venus flytrap
pitcher-plant 莱佛士猪笼草 Nepenthes rafflesiana
sundew 圆叶茅膏菜 Drosera rotundifolia
edelweiss 高山火绒草 Leontopodium nivale
snow-lotus 天山雪莲 Saussurea involucrata
strelitzia 鹤望兰 Strelitzia reginae""",
TR: """ginkgo 银杏 Ginkgo biloba
dawn-redwood 水杉 Metasequoia glyptostroboides
coast-redwood 北美红杉 Sequoia sempervirens
giant-sequoia 巨杉 Sequoiadendron giganteum
bristlecone 长寿松 Pinus longaeva
baobab 猴面包树 Adansonia digitata
banyan 孟加拉榕 Ficus benghalensis
bodhi 菩提树 Ficus religiosa
eng-oak 夏栎 Quercus robur
sugar-maple 糖槭 Acer saccharum
yoshino 染井吉野樱 Prunus × yedoensis
weeping-willow 垂柳 Salix babylonica
silver-birch 垂枝桦 Betula pendula
beech 欧洲水青冈 Fagus sylvatica
scots-pine 欧洲赤松 Pinus sylvestris
norway-spruce 欧洲云杉 Picea abies
douglas-fir 花旗松 Pseudotsuga menziesii
dahurian-larch 兴安落叶松 Larix gmelinii
cn-fir 杉木 Cunninghamia lanceolata
camphor 樟 Camphora officinarum
mountain-ash 王桉 Eucalyptus regnans
teak 柚木 Teak
mahogany 大叶桃花心木 Swietenia macrophylla
rubber-tree 橡胶树 Hevea brasiliensis
cork-oak 欧洲栓皮栎 Quercus suber
dragon-blood 索岛龙血树 Dracaena cinnabari
kapok 吉贝 Ceiba pentandra
moso 毛竹 Phyllostachys edulis
sandalwood 檀香 Santalum album
paulownia 毛泡桐 Paulownia tomentosa
plane 二球悬铃木 Platanus × acerifolia
yew 欧洲红豆杉 Taxus baccata
monkey-puzzle 智利南洋杉 Araucaria araucana
wollemi 瓦勒迈杉 Wollemia
rainbow-gum 剥桉 Eucalyptus deglupta
lebanon-cedar 黎巴嫩雪松 Cedrus libani
aspen 美洲颤杨 Populus tremuloides
dove-tree 珙桐 Davidia involucrata
tulip-tree 鹅掌楸 Liriodendron chinense
sago-palm 苏铁 Cycas revoluta""",
CR: """rice 水稻 Oryza sativa
wheat 普通小麦 Common wheat
maize 玉米 Maize
barley 大麦 Barley
sorghum 高粱 Sorghum bicolor
foxtail-millet 粟 Foxtail millet
proso-millet 黍 Proso millet
oat 燕麦 Oat
rye 黑麦 Rye
quinoa 藜麦 Quinoa
buckwheat 荞麦 Buckwheat
soybean 大豆 Soybean
peanut 花生 Peanut
potato 马铃薯 Potato
sweet-potato 番薯 Sweet potato
cassava 木薯 Cassava
sugarcane 甘蔗 Saccharum officinarum
sugar-beet 甜菜 Sugar beet
cotton 陆地棉 Gossypium hirsutum
tea 茶 Camellia sinensis
coffee 小粒咖啡 Coffea arabica
cacao 可可 Theobroma cacao
rapeseed 欧洲油菜 Rapeseed
sesame 芝麻 Sesame
flax 亚麻 Flax
tobacco 烟草 Nicotiana tabacum
oil-palm 油棕 Elaeis guineensis
coconut 椰子 Coconut
alfalfa 紫花苜蓿 Alfalfa
taro 芋 Taro
chickpea 鹰嘴豆 Chickpea
lentil 小扁豆 Lentil
mung-bean 绿豆 Mung bean
broad-bean 蚕豆 Vicia faba
hops 啤酒花 Humulus lupulus""",
FV: """apple 苹果 Apple
nashi 沙梨 Pyrus pyrifolia
peach 桃 Peach
apricot 杏 Apricot
sweet-cherry 欧洲甜樱桃 Prunus avium
grape 葡萄 Vitis vinifera
strawberry 草莓 Garden strawberry
banana 香蕉 Banana
pineapple 菠萝 Pineapple
mango 杧果 Mangifera indica
papaya 番木瓜 Papaya
orange 甜橙 Orange (fruit)
mandarin 柑橘 Mandarin orange
lemon 柠檬 Lemon
kiwifruit 中华猕猴桃 Actinidia chinensis
lychee 荔枝 Lychee
longan 龙眼 Longan
durian 榴梿 Durio zibethinus
jackfruit 菠萝蜜 Jackfruit
watermelon 西瓜 Watermelon
pomegranate 石榴 Pomegranate
persimmon 柿 Diospyros kaki
jujube 枣 Jujube
fig 无花果 Common fig
olive 油橄榄 Olive
avocado 鳄梨 Avocado
blueberry 北高丛蓝莓 Vaccinium corymbosum
tomato 番茄 Tomato
eggplant 茄 Eggplant
chili 辣椒 Capsicum annuum
cucumber 黄瓜 Cucumber
pumpkin 南瓜 Cucurbita moschata
cabbage 甘蓝 Cabbage
napa 大白菜 Napa cabbage
carrot 胡萝卜 Carrot
radish 萝卜 Radish
onion 洋葱 Onion
garlic 大蒜 Garlic
ginger 姜 Ginger
spinach 菠菜 Spinach
lettuce 莴苣 Lettuce
bitter-melon 苦瓜 Momordica charantia
pea 豌豆 Pea
common-bean 菜豆 Phaseolus vulgaris
asparagus 芦笋 Asparagus""",
DS: """saguaro 巨人柱 Saguaro
prickly-pear 梨果仙人掌 Opuntia ficus-indica
golden-barrel 金琥 Echinocactus grusonii
welwitschia 百岁兰 Welwitschia
joshua-tree 短叶丝兰 Yucca brevifolia
aloe 芦荟 Aloe vera
agave 龙舌兰 Agave americana
desert-rose 沙漠玫瑰 Adenium obesum
lithops 生石花 Lithops
jade-plant 燕子掌 Crassula ovata
creosote 三齿拉瑞阿 Larrea tridentata
saxaul 梭梭 Haloxylon ammodendron
euphrates-poplar 胡杨 Populus euphratica
ephedra 草麻黄 Ephedra sinica
tumbleweed 刺沙蓬 Salsola tragus
cistanche 肉苁蓉 Cistanche deserticola
date-palm 海枣 Date palm
ocotillo 墨西哥刺木 Fouquieria splendens
quiver-tree 二歧芦荟 Aloidendron dichotomum
jojoba 希蒙得木 Jojoba""",
AQ: """lotus 莲 Nelumbo nucifera
pygmy-waterlily 睡莲 Nymphaea tetragona
victoria 亚马逊王莲 Victoria amazonica
water-hyacinth 凤眼莲 Pontederia crassipes
duckweed 浮萍 Lemna minor
papyrus 纸莎草 Cyperus papyrus
reed 芦苇 Phragmites australis
cattail 宽叶香蒲 Typha latifolia
water-caltrop 欧菱 Trapa natans
wild-rice 菰 Zizania latifolia
euryale 芡 Euryale ferox
arrowhead 野慈姑 Sagittaria trifolia
water-chestnut 荸荠 Eleocharis dulcis
eelgrass 大叶藻 Zostera marina
mangrove 美洲红树 Rhizophora mangle
water-lettuce 大薸 Pistia
azolla 细叶满江红 Azolla filiculoides
posidonia 波喜荡草 Posidonia oceanica
bladderwort 狸藻 Utricularia vulgaris
water-spinach 蕹菜 Ipomoea aquatica""",
MU: """shiitake 香菇 Shiitake
button-mushroom 双孢蘑菇 Agaricus bisporus
oyster-mushroom 糙皮侧耳 Pleurotus ostreatus
enoki 金针菇 Flammulina filiformis
wood-ear 黑木耳 Auricularia heimuer
snow-fungus 银耳 Tremella fuciformis
lingzhi 灵芝 Ganoderma lingzhi
cordyceps 冬虫夏草 Ophiocordyceps sinensis
chanterelle 鸡油菌 Cantharellus cibarius
porcini 美味牛肝菌 Boletus edulis
morel 羊肚菌 Morchella esculenta
truffle 黑孢块菌 Tuber melanosporum
matsutake 松茸 Tricholoma matsutake
lions-mane-fungus 猴头菇 Hericium erinaceus
maitake 灰树花 Grifola frondosa
straw-mushroom 草菇 Volvariella volvacea
king-oyster 杏鲍菇 Pleurotus eryngii
fly-agaric 毒蝇鹅膏 Amanita muscaria
death-cap 毒鹅膏 Amanita phalloides
amanita-exitialis 致命鹅膏 Amanita exitialis
chlorophyllum 大青褶伞 Chlorophyllum molybdites
shaggy-mane 毛头鬼伞 Coprinus comatus
puffball 大秃马勃 Calvatia gigantea
veiled-lady 长裙竹荪 Phallus indusiatus
mycena 发光小菇 Mycena chlorophos
honey-fungus 奥氏蜜环菌 Armillaria ostoyae
turkey-tail 云芝 Trametes versicolor
chicken-woods 硫磺菌 Laetiporus sulphureus
zombie-ant 偏侧蛇虫草 Ophiocordyceps unilateralis
false-morel 鹿花菌 Gyromitra esculenta""",
MO: """yeast 酿酒酵母 Saccharomyces cerevisiae
penicillium 产黄青霉 Penicillium chrysogenum
roqueforti 娄地青霉 Penicillium roqueforti
koji 米曲霉 Aspergillus oryzae
a-niger 黑曲霉 Aspergillus niger
a-flavus 黄曲霉 Aspergillus flavus
bread-mold 匍枝根霉 Rhizopus stolonifer
candida 白色念珠菌 Candida albicans
botrytis 灰葡萄孢 Botrytis cinerea
chytrid 蛙壶菌 Batrachochytrium dendrobatidis""",
}
R4 = []
for cat, block in _raw.items():
    for line in block.strip().splitlines():
        parts = line.split(" ")
        i, cn = parts[0], parts[1]
        note = ""
        if parts[-1] == "品种": note = "品种"; parts = parts[:-1]
        R4.append((i, cn, " ".join(parts[2:]), cat, note))
N4 = {r[0]: 401 + k for k, r in enumerate(R4)}
if __name__ == "__main__":
    import collections, json, glob, os
    print(len(R4), collections.Counter(r[3] for r in R4))
    ids = [r[0] for r in R4]; dup = [x for x, c in collections.Counter(ids).items() if c > 1]; print("dup ids", dup)
    old = {os.path.basename(p)[:-5] for p in glob.glob("/workspace/animalcards/data/*.json")}
    print("clash with old ids", [i for i in ids if i in old])
    oldcn = {json.load(open(p))["name_cn"] for p in glob.glob("/workspace/animalcards/data/*.json")}
    print("clash cn", [r[1] for r in R4 if r[1] in oldcn])
    cns = [r[1] for r in R4]; print("dup cn", [x for x, c in collections.Counter(cns).items() if c > 1])
    print("long names", [r[1] for r in R4 if len(r[1]) > 11])
