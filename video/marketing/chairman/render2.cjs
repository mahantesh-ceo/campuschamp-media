const {chromium}=require('playwright');const {spawn}=require('child_process');const TL=require('./timeline.json');
const M=process.argv[2],W=+process.argv[3],K=+process.argv[4];const [vw,vh]=M==='V'?[1080,1920]:[1920,1080];
const FPS=30,N=Math.ceil((TL.duration+0.5)*FPS);const a=Math.floor(N*W/K),b=Math.floor(N*(W+1)/K);
(async()=>{const br=await chromium.launch();const p=await br.newPage({viewport:{width:vw,height:vh}});
p.on('pageerror',e=>console.log('ERR',e.message));
await p.goto('file://'+__dirname+`/film2.${M}.html`,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);
const ff=spawn('ffmpeg',['-loglevel','error','-y','-f','image2pipe','-framerate',''+FPS,'-c:v','mjpeg','-i','-','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium',__dirname+`/p2${M}${W}.mp4`]);
for(let f=a;f<b;f++){await p.evaluate(t=>renderAt(t),f/FPS);const buf=await p.screenshot({type:'jpeg',quality:93});if(!ff.stdin.write(buf))await new Promise(r=>ff.stdin.once('drain',r));}
ff.stdin.end();await new Promise(r=>ff.on('close',r));await br.close();console.log('part',M,W);})();
