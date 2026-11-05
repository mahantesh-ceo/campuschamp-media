const fs=require('fs');const QR=require('/home/user/test/node_modules/qrcode');
(async()=>{const tl=fs.readFileSync(__dirname+'/timeline.json','utf8');
const qr=await QR.toDataURL('https://www.campuschamp.in/colleges?utm_source=film&utm_medium=whatsapp&utm_campaign=history-film',{margin:1,width:600,color:{dark:'#1d1d1f',light:'#ffffff'}});
const src=fs.readFileSync(__dirname+'/film.html','utf8').replace('__TIMELINE__',tl).replace('__QR__',qr);
for(const m of ['V','H'])fs.writeFileSync(__dirname+`/film.${m}.html`,src.replaceAll('__MODE__',m));console.log('built');})();
