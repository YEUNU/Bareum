if(!self.define){let e,i={};const n=(n,s)=>(n=new URL(n+".js",s).href,i[n]||new Promise((i=>{if("document"in self){const e=document.createElement("script");e.src=n,e.onload=i,document.head.appendChild(e)}else e=n,importScripts(n),i()})).then((()=>{let e=i[n];if(!e)throw new Error(`Module ${n} didn’t register its module`);return e})));self.define=(s,o)=>{const r=e||("document"in self?document.currentScript.src:"")||location.href;if(i[r])return;let c={};const d=e=>n(e,r),f={module:{uri:r},exports:c,require:d};i[r]=Promise.all(s.map((e=>f[e]||d(e)))).then((e=>(o(...e),c)))}}define(["./workbox-fa446783"],(function(e){"use strict";self.skipWaiting(),e.clientsClaim(),e.precacheAndRoute([{url:"assets/index-1e944da5.css",revision:null},{url:"assets/index-4dcb6ccd.js",revision:null},{url:"index.html",revision:"450afb65c3616f96c5000b9782ee96b6"},{url:"registerSW.js",revision:"1872c500de691dce40960bb85481de07"},{url:"icons/android-chrome-192x192.png",revision:"08df2ad24ef532926ece01b7c317ba9d"},{url:"icons/android-chrome-512x512.png",revision:"3a23a72c96cfc7acb8fdbf19f995f299"},{url:"icons/apple-touch-icon.png",revision:"7de92b5b69eb8a2e7a7886fa127e44a6"},{url:"icons/browserconfig.xml",revision:"68c9044fa4a08749efb85bb2a4edaede"},{url:"icons/favicon-16x16.png",revision:"3890e1a10805a4730a4293468a711fab"},{url:"icons/favicon-32x32.png",revision:"f57e8504c6fbcb050279373b8404804b"},{url:"icons/favicon.ico",revision:"23a5d0ea417b07ad01999728c56914df"},{url:"icons/mstile-150x150.png",revision:"c87c83bf20f83dafd22b56e2e9412ef9"},{url:"icons/pen.png",revision:"eaded72a93647640cf76963eab360a20"},{url:"icons/pen_white.png",revision:"e1fbbf069623f2f35b1f3b496586336a"},{url:"icons/safari-pinned-tab.svg",revision:"b4ed567dd6d376bb6d76b5f3c0a3a058"},{url:"icons/site.webmanifest",revision:"22a36b7df2717d75493d9174d28391be"},{url:"manifest.webmanifest",revision:"cd4d9b4506b3750bc2b4855eb06eff70"}],{}),e.cleanupOutdatedCaches(),e.registerRoute(new e.NavigationRoute(e.createHandlerBoundToURL("index.html")))}));
