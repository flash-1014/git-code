#首先对庞大的数据源怎么进行放置，列表还是集合。
data2 = [
 ['王*⻰', '北京市海淀区苏州街⼤恒科技⼤厦南座4层'],
 ['庞*⻜', '北京市昌平区汇德商厦四楼403'],
 ['顾*锐', '江苏省扬州市三垛镇⼯业集中区扬州市⽴华畜禽有限公司'],
 ['王*⻜', '上海市徐汇区上海市徐汇区H88越虹⼴场B座5E'],
 ['华*升', '北京市海淀区杰睿⼤厦'],
 ['朱*锴', '上海市浦东新区川沙新镇华川家园33号楼503'],
 ['陈*盼', '浙江省杭州市闲林街道，⻄溪华东园，⼗幢⼀单元401。'],
 ['司*鹏', '河南省鹤壁市淇滨⼤道310号 鹤壁京⽴医院'],
 ['聂*睿', '河北省⽯家庄市中⼭路勒泰中⼼写字楼b座11层'],
 ['张*', '辽宁省本溪市明兴丽城九号楼四单元'],
 ['冉*晗', '河北省⽯家庄市体育南⼤街385号'],
 ['⾼*杰', '北京市朝阳区⼴渠路42号院3号楼，408'],
 ['李*国', '安徽省合肥市新站区淮合花园'],
 ['常*源', '江苏省南京市⽩下路242号，南京市红⼗字医院，放射科'],
 ['张*⽟', '河北省沧州市新居然家居⼴场'],
 ['王*川', '上海市奉贤区南桥镇 ⻉港七区'],
 ['冀*庆', '河北省保定市河北⼤学坤兴园⽣活区'],
 ['胡*晨', '浙江省宁波市浙江省宁波市江东区中⼭⾸府A座2004室'],
 ['尹*婷', '湖北省武汉市武汉⼤学信息学部'],
 ['李*东', '辽宁省⼤连市⼤关⼀街3号3-3-1'],
 ['张*', '天津市河⻄区隆昌路94号（天津科技馆）'],
 ['刘*', '湖北省⻩冈市城关镇'],
 ['阿*亚', '内蒙古呼和浩特市包头东接⺠望家园1区3号楼2单元1501'],
 ['孙*云', '⼭东省济南市⼭东省济南市历下区祥泰汇东国际，⼀号楼3005室'],
 ['曹*亮', '⿊⻰江省⼤庆市服务外包产业园D1'],
 ['侯*琦', '上海市⻓宁区⾦钟路凌空soho16号楼3楼'],
 ['郭*峰', '河南省商丘市⾼新技术开发区恒宇⻝品⼚'],
 ['赵*⽣', '河北省唐⼭市朝阳道与学院路路⼝融通⼤厦2408室'],
 ['张*', '陕⻄省咸阳市⽂汇东路6号⻄藏⺠族⼤学'],
 ['刘*⺠', '北京市⼤兴区南海家园四⾥7号楼1单元902'],
 ['郭*兰', '湖北省武汉市湖北省'],
 ['张*强', '河北省张家⼝市经开区钻⽯南路11号'],
 ['鞠*⻰', '⼭东省潍坊市⽟清街江⼭帝景B区12号楼⼀单元14楼'],
 ['李*', '北京市海淀区⻄⼆旗智学苑5号楼超市'],
 ['许*康', '北京市⻄城区⻄单北⼤街甲133号'],
 ['叶*⽣', '江苏省扬州市扬⼦江中路756号'],
 ['赵*兴', '北京市海淀区⻄⼆旗上地信息路1号⾦远⻅⼤楼华纬讯301'],
 ['徐*⾰', '北京市海淀区闵庄路3号102栋⼆层206'],
 ['徐*', '安徽省淮南市⾦荷⼩区(⾦格商场旁)'],
 ['雷*', '北京市朝阳区望京街道望京sohoT1C座1201'],
 ['庄*', '浙江省杭州市恒⽣电⼦⼤厦'],
 ['蔡*恩', '湖北省武汉市仁和路沙湖港湾B区1103'],
 ['陈*', '江苏省苏州市巴城镇湖滨北路193号⽜吃蟹庄'],
 ['⻩*', '北京市朝阳区霄云路26号鹏润⼤厦A座33层'],
 ['魏*⻜', '河北省⽯家庄市新⽯北路与红旗⼤街交⼝开元⼤厦502室'],
 ['张*', '⼭东省济南市兴港路三庆城市主⼈'],
 ['段*琪', '⼭⻄省临汾市福利路尧乡⼩区'],
 ['刘*', '北京市昌平区⻰禧三街骊⻰园601'],
 ['王*⽣', '上海市杨浦区邯郸路复旦⼤学遗传学楼319室'],
 ['王*君', '江苏省扬州市叶挺路318号建⾏营业部'],
 ['王*义', '北京市东城区环球贸易中⼼D座'],
 ['李*', '陕⻄省汉中市同沟寺镇晨光村⼆组'],
 ['裴*宇', '吉林省四平市岭⻄新耀豪庭7栋'],
 ['丁*', '⼭东省烟台市⼤季家镇芦洋村'],
 ['刘*铎', '⿊⻰江省佳⽊斯市⽕电⼩区桥头浴池附近惠惠⼲洗店'],
 ['樊*', '浙江省宁波市⽂苑⻛荷201-301'],
 ['陈*瑞', '安徽省宣城市安徽省宣城市宣州区薰化路301合肥⼯业⼤学宣城校区'],
 ['崔*峰', '浙江省台州市福溪街道始丰⻄路43号501室'],
 ['徐*', '湖北省武汉市三⾦雄楚天地1号楼1210'],
 ['王*', '浙江省宁波市浙江⼯商职业技术学院信息中⼼'],
 ['闫*', '上海市浦东新区蓝天路368弄1号301室'],
 ['于*泉', '吉林省四平市⾦星书苑⼩区8号楼5单元102室'],
 ['刘*萌', '河北省秦皇岛市抚宁镇交通局家属院3-2-201'],
 ['⽯*', '安徽省宣城市薰化路301'],
 ['王*雯', '⽢肃省兰州市天⽔南路222号兰州⼤学'],
 ['王*朝', '河南省郑州市嵩⼭南路政通路升⻰城六号院'],
 ['⾦*晶', '吉林省延边州延吉市新兴街⺠安委11'],
 ['蒋*彬', '辽宁省本溪市新城北岸，恒⼤绿洲'],
 ['⽜*鑫', '⿊⻰江省鸡⻄市南⼭路康光⼆号楼中雅发廊'],
 ['陈*宏', '⼭⻄省太原市太原理⼯⼤学'],
 ['刘*', '⼭⻄省运城市卿头镇'],
 ['陈*杰', '浙江省宁波市⾼新区研发园A5幢7楼多维时空科技有限公司'],
 ['郝**', '⼭东省德州市焦庙镇'],
 ['焦*', '⼭⻄省⻓治市太⾏⻄街⾦威超市太⻄店⾦威快购办公室'],
 ['李*旗', '北京市昌平区沙河镇汇德商厦4楼403⽼男孩教育'],
 ['通*⼤都', '北京市丰台区万泉寺东路9号院1栋1单1704'],
 ['孙*川', '浙江省⾦华市佛堂镇雅⻄村双溪⼝便⺠超市'],
 ['宋*', '安徽省合肥市上派镇滨河家园9栋2102'],
 ['李*', '陕⻄省安康市汉滨区新城街道南环东路⼝桃园⼩区⼤⻔⼝'],
 ['李*连', '北京市昌平区⽴汤路北七家威尼斯花园2区2-3'],
 ['籍*旭', '北京市房⼭区良乡鸿顺园⻄区20号楼3单元601'],
 ['韩*嵩', '北京市昌平区⽴汤路威尼斯花园2区2-3'],
 ['曹*', '北京市朝阳区东三环北路28号博瑞⼤厦B座'],
 ['贺*', '上海市徐汇区古美路1515号19号楼1101室'],
 ['关*轩', '⼭⻄省⻓治市⽯哲镇'],
 ['罗*', '河北省廊坊市书⾹苑⼩区四号楼'],
 ['段**', '北京市朝阳区酒仙桥东路M5世纪互联'],
 ['杜*伟', '北京市昌平区汇德商厦⽼男孩教育'],
 ['王*', '北京市昌平区汇德商厦四楼'],
 ['赵*波', '上海市闵⾏区上海市闵⾏区莘庄镇庙泾路⽔清三村52号32弄402室'],
 ['许*', '北京市海淀区⻄北旺镇中海枫涟⼭庄北⻔对⾯中⼼'],
 ['李*成', '北京市昌平区沙河镇于⾟庄村天利合家园'],
 ['刘*', '江苏省南京市兴智路6号兴智科技园A栋7层'],
 ['张*涛', '安徽省合肥市安徽省合肥市庐阳区寿春路156号古井百花⼤厦⼤厦A座2603'],
 ['⾼*', '上海市虹⼝区欧阳路351弄10号楼104室'],
 ['⾕*成', '浙江省杭州市城厢街道 下湘湖路1号'],
 ['王*⽟', '上海市嘉定区南翔镇'],
 ['刘*海', '北京市海淀区⽟渊潭南路3号⽔科院万⽅城科技楼'],
 ['杨*娟', '安徽省合肥市清源路中铁国际城和畅园'],
 ['谢*桥', '北京市海淀区丰秀中路3号院9号楼北京数码⼤⽅科技股份有限公司'],
 ['张*', '陕⻄省咸阳市北上召秦楚汽⻋城别克雪佛兰4s店'],
 ['邵*⻰', '北京市海淀区⻄北旺镇⼤⽜坊社区四期4号楼1单元301'],
 ['耿*涛', '北京市朝阳区三间房东柳巷甲⼀号意菲克⼤厦A座'],
 ['孙*周', '北京市东城区东花市街道便宜坊写字楼10层，恒信通⼤厦。就在崇⽂⻔地铁站⼝旁边'],
 ['于*涵', '⼭东省济南市舜耕路舜耕⼭庄宿舍'],
 ['陈*', '上海市普陀区近铁城市⼴场北座15楼'],
 ['⻢*', '北京市昌平区沙河镇松兰堡村⻄⼝兴业家园6号楼'],
 ['李*宇', '江苏省苏州市⼯业园区苏雅路158号华盛⼴场3楼东北证券304室'],
 ['王*杰', '河北省邯郸市后仓街39号'],
 ['刘*明', '河北省唐⼭市卫国北路305张家⼝银⾏'],
 ['王*凡', '天津市南开区卫津路92号天津⼤学鹏翔公寓'],
 ['郭*军', '上海市浦东新区郭守敬路498号浦东软件园16号3楼'],
 ['宋*东', '北京市丰台区万寿路南⼝288号华信⼤厦'],
 ['江*', '安徽省⾩阳市临海尚城B区2单元，19号楼'],
 ['吴*', '河南省郑州市经三路与东⻛路交汇处⾦城国际⼴场6#东单元2403'],
 ['祁*雄', '湖北省武汉市洪⼭区⽩沙洲⼤道武汉科技⼤学北苑'],
 ['吕*', '上海市嘉定区上海市嘉定区嘉罗公路2019号'],
 ['⻩*', '湖北省武汉市国家光电实验室'],
 ['常*旗', '⼭东省潍坊市林海⽣态博览园'],
 ['陈*', '上海市虹⼝区吴淞路218号宝矿⼤厦2501A'],
 ['郑*琳', '北京市丰台区⻄⻢⾦润家园2区10号楼11单元11-2-1'],
 ['姚*峰', '江苏省⽆锡市江苏省⽆锡市滨湖区⻰⼭龚巷213#'],
 ['徐*', '浙江省杭州市余杭塘路515矩阵国际中⼼2号楼705'],
 ['沈*', '上海市⻓宁区⾦钟路968号凌空SOHO11号楼506室'],
 ['王*', '上海市浦东新区川沙路1666弄79号803'],
 ['徐*', '⼭东省⽇照市安东卫街道汾⽔村'],
 ['路*领', '北京市丰台区四⽅景园⼀区3号楼1006室'],
 ['张*巍', '河南省开封市⻄环路北段⻘年城8号楼3单元302'],
 ['王*俊', '江苏省盐城市新都路29号紫⾦⼤厦19楼'],
 ['姜*波', '北京市朝阳区北京市朝阳区⾩通东⼤街1号望京soho塔三B座17层1707'],
 ['曹*翎', '江苏省苏州市科教新城太和丽都31-1604'],
 ['⻬*', '江苏省南京市天元东路228号莱茵量⼦国际'],
 ['⾼*', '⼭⻄省太原市经济技术开发区⻰盛街2号国药控股'],
 ['刘*', '北京市海淀区中关村丹棱街中国电⼦⼤厦B座1608'],
 ['陈*⼭', '安徽省六安市南港镇'],
 ['赵*', '⿊⻰江省哈尔滨市锦⼭路5号，⿊⻰江省地质科学研究所'],
 ['伍*', '安徽省芜湖市泉塘镇'],
 ['⽩*潮', '上海市浦东新区康桥镇环桥路2585弄⽂怡苑⼀期27号楼301'],
 ['⻩*曦', '北京市朝阳区⻄坝河南路3号2层201室 同创双⼦信息技术股份有限公司'],
 ['牟*强', '⼭东省⽇照市⼭东东路619号 ⼴电⽹络公司'],
 ['李*运', '上海市松江区沪亭南路208弄109号801室'],
 ['杨*', '北京市朝阳区安苑路20号世纪兴源⼤厦304'],
 ['宋*伟', '河北省⽯家庄市⾼头乡⻄⾼村'],
 ['任*鹏', '陕⻄省⻄安市锦业⼀路29号 ⻰旗科技园 6层 ⻄安和利时系统⼯程有限公司'],
 ['孙*洲', '北京市东城区东花市街道便宜坊写字楼10层，恒信通公司。就在崇⽂⻔地铁站旁边'],
 ['张*义', '上海市浦东新区三舒路181弄2号904'],
 ['⻔*意', '⿊⻰江省哈尔滨市⽂昌街238号联通系统集成有限公司'],
 ['陈*维', '上海市虹⼝区欧阳路196号26栋2楼'],
 ['周*涛', '浙江省嘉兴市施家北路陈家浜1号'],
 ['吴*', '江苏省苏州市⼯业园区星湖街328号11栋'],
 ['苏*', '河南省郑州市登封路晨光社区14号院绿⽥￾超市'],
 ['王*', '陕⻄省⻄安市雁塔区雁翔路58号⻄安理⼯⼤学曲江校区'],
 ['赵*⻰', '河北省廊坊市燕郊经济开发区福成⼤酒店东福成⾏政中⼼三楼信息部'],
 ['范*勇', '江苏省苏州市苏州市吴中区⽊渎镇胥⼝镇621号斯莱克精密设备股份有限公司'],
 ['⽩*', '北京市东城区安定⻔外⼤街10号楼415'],
 ['刘*', '北京市昌平区回⻰观镇⼆拨⼦新村东区7号楼1单元402'],
 ['钱*庭', '江苏省江苏省泰州市姜堰区南苑新村58号'],
 ['王*', '北京市朝阳区北京市朝阳区摩托罗拉⼤厦'],
 ['杨*', '北京市朝阳区⾩荣街10号⾸开⼴场5楼'],
 ['姬*⻜', '北京市昌平区宏福创业园15号创昱'],
 ['熊*威', '浙江省杭州市万塘路252号计量⼤厦10楼'],
 ['薛*', '⼭东省济南市⾼新区新泺⼤街888号福瑞达'],
 ['贾*凯', '上海市浦东新区鹤永路751弄汇贤雅苑'],
 ['孟*震', '上海市宝⼭区淞南镇祥腾⽣活⼴场，8栋816室'],
 ['刘*', '河南省洛阳市城关镇⼈⺠路21号'],
 ['杨*凯', '湖北省武汉市中国地质⼤学北区1栋'],
 ['王*', '上海市浦东新区环桥路1137弄秀怡苑31号楼302'],
 ['夏*', '北京市朝阳区垂杨柳东⾥11号楼3单元402'],
 ['张*宇', '北京市海淀区中关村南⼤街6号中电信息⼤厦1207'],
 ['蔡*', '陕⻄省⻄安市凤城⼋路天朗御湖⼀号楼⼆单元（⻄⻔）'],
 ['⾼*', '新疆乌鲁⽊⻬市⺠主路99号建⾏⼤厦12楼审计室'],
 ['孙*园', '陕⻄省⻄安市丈⼋沟街道科技五路8号数字⼤厦'],
 ['王*亚', '北京市朝阳区华盛乐章b座1708'],
 ['李*博', '⼭东省淄博市索镇花园⼩区5#2单元202室'],
 ['⽅*', '北京市海淀区北洼⻄⾥33号清华同⽅研究院'],
 ['杨*东', '上海市闵⾏区梅陇镇⾼兴路⾼兴花园⼀街坊14号501'],
 ['袁*', '陕⻄省⻄安市⾼新四路南窑头东区22排11号'],
 ['王*', '天津市河北区建国道地铁站B⼝旁⻘创中⼼'],
 ['程*磊', '北京市⻄城区北三环中路27号商房⼤厦5楼'],
 ['陈*琦', '安徽省合肥市徽州⼤道与九华⼭路交叉⼝信旺九华国际2419'],
 ['刘*杰', '北京市⼤兴区亦庄经济开发区地盛北街1号35号楼2栋北京如⻛达快递有限公司'],
 ['侯*森', '北京市朝阳区北苑路潮驿178'],
 ['胡*辉', '浙江省杭州市瑞⽴东⽅花城2-2-503'],
 ['杨*平', '北京市昌平区沙河镇于⾟庄村赋腾公寓'],
 ['⻩*', '浙江省杭州市衢江路耀江福村3单元602'],
 ['李*', '上海市⻩浦区⻩浦区北京东路288弄66号甲，后⻔201室'],
 ['邹*', '安徽省淮北市南坪镇⻩沟村邹圩庄'],
 ['刘*', '北京市昌平区沙河镇赋腾公寓E516'],
 ['彭*', '北京市望京SOHOt3 40层'],
 ['张*乾', '河南省周⼝市⼋⼀路⼈⺠路交叉⼝医药局家属楼'],
 ['贺*梦', '北京市通州区永顺镇世纪星城92号楼⼆单元'],
 ['冯*琴', '北京市海淀区⾦澳国际写字楼1115 中汇'],
 ['邓*亮', '湖北省武汉市云林街台北⼀路58号'],
 ['李*沙', '北京市昌平区城南街道北清路珠江摩尔国际⼤厦五号楼⼆单元906'],
 ['徐*瑞', '上海市徐汇区古美路1595号宝⽯园27号楼2楼D区'],
 ['梁*', '陕⻄省⻄安市电⼦⼆路18号(⻄安⽯油⼤学)'],
 ['徐*', '浙江省衢州市⻄区⼴电⼤楼'],
 ['雷*强', '河南省信阳市汪桥镇街道滨河花园A幢6208'],
 ['张*亮', '天津市河⻄区郁江道17号陈塘科技328'],
 ['陈*', '上海市浦东新区东⽅路1217号陆家嘴⾦融服务⼴场15楼'],
 ['郭*', '北京市昌平区北七家镇东三旗365号'],
 ['李*扬', '上海市浦东新区北蔡镇北艾路1500弄6号楼203'],
 ['汝*明', '吉林省⻓春市⻓春光机所研究⽣部D栋'],
 ['朱*懿', '上海市静安区陕⻄北路66号科恩国际中⼼1027室'],
 ['刘*', '上海市浦东新区五莲路 锦河苑'],
 ['任*荣', '陕⻄省⻄安市软件新城软件公寓'],
 ['王*', '上海市闵⾏区莲花路2080弄50号C幢3楼'],
 ['崔*斌', '北京市房⼭区阎村镇焦庄村四⾥'],
 ['王*强', '浙江省杭州市物联⽹街451号芯图⼤厦17楼'],
 ['姬*玲', '⿊⻰江省哈尔滨市⻓江路462号悦⼭国际c座1单元2501'],
 ['T*m', '上海市浦东新区浦东⼤道3040弄丽江锦庭1号楼'],
 ['李*宇', '⿊⻰江省绥化市⼗道街升平⼩区15号楼1单元102室'],
 ['董*', '河南省郑州市崇⾼路与嵩⼭路交叉⼝北⻩河商务酒店'],
 ['杨*辉', '江苏省镇江市江苏⼤学F 区'],
 ['韩*鉴', '北京市⻔头沟区滨河路葡东⼩区七号楼4层D⻔'],
 ['罗*若', '陕⻄省⻄安市⻰⾸北路宫园⼀号5号楼4单元'],
 ['王*', '北京市海淀区上地东路盈创动⼒⼤厦e座801c源清慧虹信息科技'],
 ['⻢*', '湖北省武汉市庙⼭中路10号名湖豪庭7栋1403'],
 ['常*峰', '⼭⻄省太原市迎新街'],
 ['侯*', '浙江省杭州市江陵路1541号'],
 ['许*娟', '上海市宝⼭区殷⾼⻄路⾼境⼆村177号502'],
 ['徐*⻜', '湖北省武汉市潘塘街喻⼤村梅家⼤湾'],
 ['崔*腾', '辽宁省沈阳市虹桥路15号富雅豪临'],
 ['张*俊', '新疆巴⾳郭楞州⽯化⼤道塔指1区25栋403'],
 ['严*', '北京市⼤兴区清源北路16号，校⻓⼤厦'],
 ['李*', '北京市⼤兴区⼗⼋⾥店乡横街⼦村64号柠檬家园B113'],
 ['于*佳', '北京市朝阳区郎园2号A座2层'],
 ['张*江', '北京市海淀区海淀区上地三街9号⾦隅嘉华⼤厦Ｆ座703室'],
 ['萌*', '北京市⻄城区⾦融街邮政集团公司'],
 ['张*宾', '河南省郑州市⽂治路泰祥投资集团楼下新锐⼴告'],
 ['彭*灿', '江苏省苏州市⽟⼭镇印象欧洲17#606'],
 ['王*亮', '北京市朝阳区双营路11号美⽴⽅4号楼4单元602'],
 ['朱*伦', '北京市海淀区⻄三环中路19号海军⼤院⻄⻔顺丰快递'],
 ['杜*', '河北省⽯家庄市河北科技⼤学新校区26号'],
 ['董*', '北京市朝阳区雅宝路华声国际⼤厦'],
 ['朱*', '江苏省镇江市延陵镇'],
 ['段*', '⼭东省临沂市银雀⼭街道万阅城A座1207'],
 ['朱*', '北京市昌平区北京联合⼤学昌平校区'],
 ['陈*章', '北京市昌平区沙河镇⽩沙路汇德商厦⽼男孩教育'],
 ['肖*雅', '北京市昌平区沙河汇德商厦4楼⽼男孩⼉教育'],
 ['赵*明', '北京市昌平区沙河顺沙路汇德商厦⽼男孩教育403'],
 ['邹*', '宁夏银川市上海路福州街⼝云峰盛⼤药房'],
 ['袁*', '辽宁省锦州市辽宁省凌海市国庆路33B号2单元23室'],
 ['陈*', '浙江省杭州市昌化电站⾥56号骏程瓷砖店'],
 ['索*辉', '辽宁省沈阳市浑南区创新路117号东软医疗系统有限公司'],
 ['李*', '北京市⼤兴区天宫院地铁站熙悦春天⼩区'],
 ['张*', '陕⻄省⻄安市电⼦城街道⾼新领域4号楼'],
 ['王*', '⼭⻄省吕梁市⼀家庄⼩区三期五号楼'],
 ['钟*', '陕⻄省商洛市商洛学院'],
 ['薛*', '江苏省泰州市⼝岸街道向阳北路94号农商⾏'],
 ['张*强', '⽢肃省兰州市北滨河⻄路666号（中国移动⽢肃分公司）'],
 ['姚*⻜', '上海市浦东新区成⼭路1728弄88号'],
 ['赵*宁', '浙江省⾦华市光南路898号⾦华移动公司'],
 ['张*昌', '北京市昌平区回⻰观东⼤街 矩阵⼩区 11楼1单元1102室'],
 ['董*亨', '上海市嘉定区曹安公路4800号同济⼤学嘉定校区'],
 ['李*根', '北京市昌平区⻢连店4号楼2单元'],
 ['贾*新', '北京市海淀区学院路29号'],
 ['吕*', '浙江省⾈⼭市⾼亭镇军⺠路106号'],
 ['张*东', '河南省周⼝市⻄华县基城⾼中'],
 ['李*东', '河北省⽯家庄市新⽯中路，物联⽹⼤厦10层'],
 ['韩*泰', '⼭东省⻘岛市⻘岛农业⼤学⻄苑'],
 ['邵*遥', '浙江省杭州市塘栖镇张家墩路65号博乐展具内'],
 ['李*泽', '河南省郑州市郑东新区⻰⼦湖⾼校园区郑州信息科技职业学院'],
 ['沈*蕾', '浙江省杭州市下沙学源街中国计量⼤学'],
 ['冯*明', '上海市浦东新区张江路华夏中路 虹御公寓'],
 ['海*', '浙江省杭州市良渚街道⼤陆村邱家桥桥南3号'],
 ['刘*⻰', '北京市通州区台湖镇次渠嘉园8区1号楼1705号'],
 ['王*宇', '河南省安阳市红旗路天宇国际三号楼四单元'],
 ['宋*波', '北京市海淀区⻰翔路甲1号泰翔商务楼508'],
 ['周*萧', '北京市昌平区回⻰观镇史各庄村176号'],
 ['梁*升', '吉林省吉林市承德街45号吉林化⼯学院'],
 ['陈*⻰', '上海市浦东新区郭守敬路498号23号楼23215'],
 ['张*', '上海市徐汇区桂林路402号 诚达创意园76幢407室 银基科技'],
 ['何*畅', '河南省周⼝市⻄华县箕城⾼中'],
 ['欧*', '北京市丰台区东营⾥5号院8号楼2单元401'],
 ['张*', '陕⻄省⻄安市陕⻄⻄安思源学院'],
 ['曹*', '浙江省宁波市⽩沙街道新⻢路61弄江北区农林⽔利局'],
 ['陈*刚', '宁夏银川市上海东路银佐家园东区11-1-501'],
 ['喻*明', '湖北省武汉市徐东'],
 ['陈*余', '北京市海淀区⽢家⼝街道⾩成路北⼆街⾩光⾥⼩区7号楼⼆单元102'],
 ['刘*博', '⼭⻄省太原市⼩店区平阳路42号⼭⻄省⾃动化研究所'],
 ['王*', '北京市⼤兴区亦庄经济技术开发区⼤族⼴场T5，6层洪泰空间c033'],
 ['褚*⽂', '湖北省武汉市明伦正街明伦⽣鲜市场9号'],
 ['乔**', '河北省衡⽔市⾹榭丽都2号楼1单元 2603'],
 ['貟*杰', '上海市宝⼭区上海市宝⼭区陆翔路678弄62号903'],
 ['⽢*德', '北京市海淀区四季⻘杏⽯⼝路甲18号航天信息园'],
 ['杨*奖', '北京市东城区东单北⼤街1号国旅⼤厦502'],
 ['李*', '北京市海淀区北京市海淀区中关村南⼤街9号理⼯科技⼤厦207'],
 ['刘*', '浙江省杭州市紫荆花路⾦⽉巷嘉⽲花苑'],
 ['刘*亮', '北京市朝阳⻔'],
 ['聂*敏', '上海市浦东新区⾼博路188弄1号楼1903室'],
 ['刘*正', '⼭东省⻘岛市流亭街道洼⾥社区⼋号楼尚美美发'],
 ['杨*强', '陕⻄省⻄安市枣园路万科⾦⾊悦城'],
 ['聂*', '湖北省武汉市台银⼤厦1单位1楼'],
 ['刘*', '上海市闵⾏区闵驰⼀路29弄3号1101'],
 ['郭*', '⻘海省⻄宁市互助东路12号海亮⼤都汇'],
 ['芦*坤', '北京市朝阳区北京⼯⼈体育场3号看台2号楼1706'],
 ['晋*林', '上海市杨浦区隆昌路619号城市概念10号b座'],
 ['董*', '浙江省杭州市丰潭路城⻄银泰E2幢10楼'],
 ['刘*', '湖北省武汉市中国地质⼤学（北区）'],
 ['⻢*', '河北省保定市保定市南市区朝阳南⼤街哈弗技术中⼼2076号包裹站'],
 ['王*超', '⿊⻰江省哈尔滨市永泰城3号楼1单位1304'],
 ['孙*敏', '北京市昌平区北京市昌平区沙河于⾟庄于⾟家园1号楼1单元'],
 ['郑*⻰', '河南省郑州市花园路国基路花园SOHO2栋'],
 ['李*', '北京市昌平区流星花园三区11号楼4单元401室'],
 ['李*', '浙江省杭州市⾦岸提⾹3幢1单元1303'],
 ['庄*峰', '北京市海淀区慧科⼤厦'],
 ['⻢*', '北京市朝阳区惠新东街11号紫光发展⼤厦A座12层'],
 ['朱*', '北京市海淀区东升镇宝盛东路奥北科技园领智中⼼Ｂ座5层'],
 ['吴*峰', '湖北省武汉市幸福路鸿福花园1栋3006'],
 ['付*诚', '北京市海淀区观林园'],
 ['滕*', '江苏省南京市秣周东路11号双⼦楼9号楼15楼君度科技'],
 ['⽯*刚', '辽宁省⼤连市⼤连市经济技术开发区福泉北路20号'],
 ['程*', '北京市昌平区沙河兆丰家园'],
 ['武*', '北京市昌平区回⻰观⻄⼤街⻰腾苑五区16号楼1单元202'],
 ['郭*欣', '北京市⻄城区⾩成⻔ 万通新世界 B座1503'],
 ['⽑*', '陕⻄省⻄安市⾼新六路万象汇B座'],
 ['⻰*宇', '⼭东省⻘岛市⼭东省⻘岛市市南区⻘岛啤酒⼤厦403'],
 ['郅*', '北京市顺义区后沙峪清岚花园⻄区15号楼⼀单元502'],
 ['蔡*芝', '江苏省南京市新模范⻢路五号南京⼯业⼤学国家科技园 A2405'],
 ['王*⻜', '江苏省苏州市⼯业园区雪堂街1号，善⾏楼17栋'],
 ['葛*光', '北京市海淀区复兴路甲23号华能⼤厦'],
 ['胡*鑫', '天津市和平区河南路63号'],
 ['陶*东', '浙江省宁波市杭州湾新区滨海四路777号b-4'],
 ['王*庆', '上海市静安区万荣路700号A1 SINODIS⻝品有限公司'],
 ['刘*闯', '北京市东城区东中街58号美惠⼤厦B座2单元1层MH-Z-0005'],
 ['李*', '上海市闵⾏区航北路228弄142号202'],
 ['林*春', '河南省郑州市河南中医药⼤学⻰⼦湖校区'],
 ['张*春', '陕⻄省延安市李渠镇阳⼭村延安北铁路⼩区'],
 ['李*', '浙江省杭州市⽂三⻄路52号建投⼤厦'],
 ['李*', '河南省郑州市红旗路6号华图教育'],
 ['徐*麒', '河南省洛阳市河南科技⼤学开元校区'],
 ['陈*', '江苏省苏州市伟业迎春华府'],
 ['张*', '北京市北京亦庄经济开发区地泽北街1号朗致集团'],
 ['伍*葵', '新疆阿克苏地区红旗坡⼗⼀队'],
 ['王*操', '上海市浦东新区亮秀路72号X座6楼'],
 ['孙*强', '湖北省宜昌市⼤学路8号三峡⼤学'],
 ['王*军', '⼭东省临沂市九曲街道格瑞斯⼩镇'],
 ['郭*', '天津市⻄⻘区侯台碧⽔家园e区'],
 ['聂*双', '北京市海淀区柳浪家园东⾥5号楼3单元801室'],
 ['安*', '辽宁省沈阳市⻘⼭路亚都名苑3期逸林14号楼1-11-2'],
 ['戴*', '浙江省杭州市乔司街道花漫⾥8幢3单元101'],
 ['⽶*俊', '陕⻄省⻄安市太⽩新苑'],
 ['周*祺', '河南省新乡市新辉路街道建设⻄路保温瓶⼚家属院向⻄100⽶新中批发'],
 ['丁*', '⼭⻄省运城市运城宾馆对⾯北⼤⻘⻦'],
 ['⽂*宇', '湖北省宜昌市三峡⼤学欣苑'],
 ['王*', '北京市海淀区北清路68号⽤友软件园'],
 ['张*君', '⼭东省⻘岛市上清路16号甲，⻘岛东软载波科技股份有限公司'],
 ['正*', '⼭东省济南市经⼗路20188号'],
 ['李*晓', '北京市朝阳区国际电⼦城总部360发票A座收发室'],
 ['丁*涛', '江苏省苏州市⼦胥路新峰⼯业⼩区11栋苏州三川'],
 ['A*yua*', '上海市浦东新区华佗路1号'],
 ['夏*捷', '陕⻄省⻄安市⻄安邮电⼤学'],
 ['郭*坤', '⼭东省济宁市济宁学院男⽣宿舍'],
 ['杨*星', '湖北省武汉市江夏⼤道18号梅兰⼭居碧⽔轩'],
 ['唐*宁', '新疆乌鲁⽊⻬市新疆省乌鲁⽊⻬头屯河区⽕⻋⻄站6街'],
 ['⽥*', '上海市⻩浦区⻢当路388号SOHO复兴⼴场E栋2楼R13A'],
 ['覃*', '湖北省武汉市南李路55号'],
 ['杨*', '北京市朝阳区光华路甲8号和侨⼤厦B座508'],
 ['梁*雷', '北京市海淀区王庄路1号，清华同⽅科技⼴场B2006'],
 ['李*', '湖北省武汉市东湖⾼新南湖⼤道182号'],
 ['曹*伟', '江苏省南京市安德⻔⼤街57号楚翘城1号楼4层'],
 ['郭*铠', '⼭⻄省太原市南中环⻄街万年花城7号楼2单元401'],
 ['李*⽣', '江苏省南京市江⼭路明发3期332栋603室'],
 ['许*⾠', '河南省郑州市丰产路111号河南省国家税务局8楼信息中⼼'],
 ['姚*超', '北京市昌平区TBD云集中⼼1号楼5层'],
 ['张*', '⼭东省⻘岛市⼭东科技⼤学'],
 ['⾼*锐', '⼭东省济南市经⼗路万科⾦域中⼼a座'],
 ['严*', '安徽省合肥市双凤开发区⾩阳北路与魏武路交叉⼝⻄南⻆北部湾⼩区'],
 ['李*春', '⼭东省德州市德州职业技术学院'],
 ['张*豪', '河南省南阳市河南省南阳市宛城区第七⼩学邮政家属院对⾯的楼七⼀搬运站'],
 ['康*', '北京市朝阳区垡头东⾥百斯特⼤厦A663'],
 ['陈*', '江苏省南京市⽂苑路9号南京邮电⼤学'],
 ['柴*⻁', '北京市昌平区北七家镇顺玮阁⼩区'],
 ['韩*', '辽宁省葫芦岛市⼩庄⼦乡宝仓村'],
 ['魏*森', '北京市昌平区于⾟庄路，赋腾国创中⼼，2楼'],
 ['邓*明', '北京市丰台区新华街三⾥1号楼305'],
 ['赵*', '上海市宝⼭区宝⼭区⾼境镇⾼境⼀村11号后3号⻋库'],
 ['徐*亮', '北京市海淀区花园东路11号泰兴⼤厦302'],
 ['张*凡', '北京市昌平区沙河镇松兰堡迎客家园507'],
 ['赵*', '北京市北京市海淀区农⼤国际创业园b区6065'],
 ['顾*天', '北京市海淀区上地东路1号华控⼤厦'],
 ['丁*', '上海市杨浦区安波路533弄硕和商务2号楼1102'],
 ['封*号', '江苏省苏州市陆家镇陆丰东路199号⽔岸⾹堤2#2309'],
 ['王*哲', '上海市静安区曲沃路430弄15号401'],
 ['刘**', '湖北省武汉市左岭镇 武汉华星光电⼀号⻔'],
 ['付*', '安徽省合肥市⻓江⻄路305号电信新技术楼'],
 ['鲁*', '湖北省武汉市武⼤科技园宏业楼C座'],
 ['张*', '北京市朝阳区⼩营路13号亚⾮⼤厦7层8704室'],
 ['⻬*', '湖北省武汉市珞喻路⻢家庄'],
 ['王*', '北京市海淀区北坞嘉园北⾥9号楼三单元D01'],
 ['陈*⻰', '北京市朝阳区北卫新园'],
 ['曹*⽣', '江苏省⽆锡市澄南花苑'],
 ['沈*', '北京市海淀区中关村南⼤街甲18号北京国际⼤厦D座7层'],
 ['续*', '⼭⻄省晋中市中都⼴场12层畅快⻋贷'],
 ['赵*全', '河北省唐⼭市李钊庄镇⼤王庄村'],
 ['成*', '上海市虹⼝区东五⼩区641号楼2007'],
 ['⽅*', '上海市闵⾏区联航路1399弄28号1103室'],
 ['曹*', '上海市浦东新区向城路15号24C'],
 ['韩*德', '北京市⼤兴区枣园北⾥⼩区1号楼8单元202'],
 ['⾦*鹏', '浙江省温州市温州职业技术学院⽣活区快递中⼼'],
 ['陶*明', '浙江省嘉兴市南溪路桂苑⼩区23幢603'],
 ['李*ir', '北京市丰台区南苑乡 德鑫家园9号楼5单元50'],
 ['姜*杰', '⼭东省临沂市凤凰岭⼤街惠⺠早餐'],
 ['l*xq', '辽宁省沈阳市卫⼯南街4-4⽹点2⻔瀚⾠跆拳道'],
 ['赵*', '河北省邯郸市幸福街于联防路交叉⼝北⾏幸福馨苑'],
 ['张*锋', '内蒙古呼和浩特市双河镇莹昱佳苑商铺A段13号（防汛东巷莲爱粮油副⻝⻔市）'],
 ['胡*', '北京市⻄城区鸭⼦桥路24号'],
 ['王*鲲', '北京市延庆区东外⼩区15号楼⼀单元101'],
 ['⻢*闻', '陕⻄省⻄安市⻄安邮电⼤学东⻔'],
 ['许*', '安徽省合肥市宿松路紫⽵苑B区2栋2单元602室'],
 ['范*', '浙江省⾦华市⾦华职业技术学院'],
 ['⻢*铎', '⼭⻄省太原市徐沟镇⼭⻄警察学院'],
 ['武*⽂', '上海市浦东新区浦东新区盛夏路738弄樟盛苑32号楼⼀楼'],
 ['陈*', '江苏省徐州市苏堤北⼩区四号楼三单元702室'],
 ['曹*政', '辽宁省⼤连市⼤连理⼯⼤学软件学院'],
 ['张*超', '⼭东省济南市⼋⼀⽴交桥⻄南⻆联通公司3号楼'],
 ['唐*⽣', '⼭东省济南市⼯业南路鑫苑国际城市花园'],
 ['严*鹏', '上海市杨浦区五⻆场街道 国定路277弄铁村⼩区13号601'],
 ['张**', '⽢肃省兰州市⽢肃省兰州市七⾥河区兰公坪兰州理⼯⼤学校本部'],
 ['麻*肖', '安徽省宿州市⾹格⾥拉108幢'],
 ['刘*仪', '河北省廊坊市燕郊经济开发区 华北科技学院'],
 ['刘*⻰', '河南省洛阳市新⼀中⽂印室'],
 ['李*', '陕⻄省⻄安市临潼区⻄安科技⼤学'],
 ['相**', '北京市昌平区天通公园⾥'],
 ['康*熙', '⼭⻄省忻州市万⼈商厦对⾯联想专卖店'],
 ['张*栋', '⼭东省泰安市安驾庄镇上前'],
 ['陶*', '安徽省宣城市鳌峰东路180号宣城皖南农商银⾏413室'],
 ['艾*⻨提江·拜克热', '浙江省杭州市浦沿街道江畔云卢4幢2单元1202'],
 ['王*', '上海市浦东新区福⼭路455号，全华信息⼤厦，1楼，平安银⾏'],
 ['刘*林', '湖北省宜昌市枝城镇⼤堰村四组'],
 ['罗*', '河南省信阳市⻄关⻩国新城C6'],
 ['莫*', '河南省郑州市⾦⽔区76号9202'],
 ['徐*⻰', '安徽省合肥市⻓江⻄路新加坡花园城4联排'],
 ['杨*杰', '⼭⻄省忻州市京原南路雷神⽹咖'],
 ['朱*北', '海南省海⼝市和平北路三亚上⼆街9号'],
 ['朱*', '浙江省杭州市⻰湖春江郦城'],
 ['常*磊', '北京市海淀区学院南路59号'],
 ['王*阳', '江苏省南京市南京江宁21世纪现代城'],
 ['谢*星', '⽢肃省酒泉市雄关路54号东⻛物流⼗号'],
 ['侯*', '河南省郑州市河南省郑州市⾼新区莲花街牡丹路⻄雅图荣邦城'],
 ['孙*康', '江苏省南京市化⼯园⽅⽔东路9号'],
 ['索*华', '北京市昌平区北七家镇东三旗村委会'],
 ['王*', '陕⻄省⻄安市⼗⾥铺街⻓⼒⼩区北⻔对⾯（王家辣⼦⾯）'],
 ['姜*⽣', '北京市朝阳区东⼤桥宫宵国际1103'],
 ['顾*⽣', '安徽省⾩阳市清河⻄路100号⾩阳师范学院'],
 ['申*伟', '上海市⻘浦区巷佳华苑三期10号楼904室'],
 ['刘*', '湖北省武汉市左岭新城1社区15栋'],
 ['单*成', '⼭东省⽇照市⽇照职业技术学院'],
 ['韩*红', '上海市杨浦区隆昌路619号10号楼⼆楼'],
 ['魏*琪', '北京市丰台区汉威国际⼴场4区12号楼'],
 ['杨*康', '北京市丰台区丰台科技园汉威⼴场12栋'],
]
#筛选信息，对列表中的信息进行筛选。

#首先满足重复筛选，用while+continue效果非常好。
while True :
    #存在问题：1.输入字符需要控制好，可能会出现输入"山"字，会将山东和山西省的信息全打印出来，
    #解决设想：将省会信息全部放入一个列表中，每次输入时进行判断，输入如果不是省会信息，请重新输入
    ShengHui = input(f"请您输入需要分拣快递的省会：")
    #print(ShengHui)
    #列表语句推导式
    # filter_data = [item for item in data2  if ShengHui in ''.join(item)]
    # #''
    # for item in filter_data:
    #     print(item)
    #     continue

    #用循环语句来替代推导语句
    filter_data = []
    for item in data2:
     if ShengHui  in ''.join(item):
      filter_data.append(item)