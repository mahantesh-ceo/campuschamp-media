const {chromium}=require('playwright');const M=process.argv[2];const [w,h]=M==='V'?[1080,1920]:[1920,1080];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:w,height:h}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+__dirname+`/film2.${M}.html`,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
let i=0;for(const t of process.argv.slice(3).map(Number)){await p.evaluate(t=>renderAt(t),t);await p.screenshot({path:__dirname+`/s2${M}-${String(i++).padStart(2,'0')}.jpg`,type:'jpeg',quality:80});}
await b.close();})();
