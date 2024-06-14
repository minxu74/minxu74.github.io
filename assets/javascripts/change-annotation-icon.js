document$.subscribe(function() {
  /*console.log("Initialize third-party libraries here")*/

  if (document.title.includes("Publications")) {
     const elements = document.getElementsByTagName("aside");
     const icnpath = "<path d=\"M12 2a10 10 0 0 1 10 10 10 10 0 0 1-10 10A10 10 0 0 1 2 12 10 10 0 0 1 12 2m-1 5a2 2 0 0 0-2 2v8h2v-4h2v4h2V9a2 2 0 0 0-2-2h-2m0 2h2v2h-2V9Z\"/>";
     const iconsvg = `<svg xmlns=\"http://www.w3.org/2000/svg\" viewBox=\"0 0 24 24\">${icnpath}</svg>`;
     const iconurl = `url('data:image/svg+xml;charset=utf-8,${iconsvg}')`;
     /*const iconurl = `url('')`;*/

     for (const el of elements) {
         /*console.log("find a aside element");*/
         for (const sp of el.getElementsByTagName("span")) {

             /* console.log(sp.data-md-annotation-id); */
             if (sp.hasAttribute('data-md-annotation-id')){
                 if (sp.getAttribute('data-md-annotation-id')==2) {

                     el.setAttribute('style', "--md-annotation-icon: ".concat(iconurl));
                     /*console.log(el);*/
                 };
             };
         };
     };
  };
});
