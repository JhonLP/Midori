(function($){$.fn.resizeAndCrop=function(options){var settings={'width':0,'height':0,'crop':true,'center':true,'smart':true,'preserveSize':false,'forceResize':false,'imgClass':'','contClass':'','renderStartDelay':50,'renderBatchSize':10,'renderBatchPause':200};var queue=[];if(options){$.extend(settings,options);}
this.each(function(){queue.push(this);});setTimeout(_run,settings.renderStartDelay||0);return this;function _run(){var max=settings.renderBatchSize||queue.length,i=0;for(;i<max&&queue.length;i++){_bindImage(queue.shift());}
if(queue.length){setTimeout(_run,settings.renderBatchPause||0);}}
function _bindImage(imgEl){var $img=$(imgEl),realSrc=$img.attr("realsrc")||$img.attr("src");if(!realSrc)return;var newImg=$(document.createElement('img'));newImg.bind("load",{img:imgEl},_onload);var altStr,titleStr;if(typeof(altStr=$img.attr('alt'))!=='undefined'){newImg.attr("alt",altStr);}
if(typeof(titleStr=$img.attr('title'))!=='undefined'){newImg.attr("title",titleStr);}
newImg.attr("src",realSrc);}
function _onload(e){var $origImg=$(this),origW=this.width,origH=this.height,curImg=e.data.img,$curImg=$(curImg),reqW=settings.width||curImg.width,reqH=settings.height||curImg.height,cropW=settings.forceResize?reqW:Math.min(origW,reqW),cropH=settings.forceResize?reqH:Math.min(origH,reqH),cont;if(!origW||!origH){return;}
if(!settings.crop&&reqW==origW&&reqH==origH){$curImg.attr("src",$origImg.attr("src"));return;}
if(cropW*origH<cropH*origW){this.width=Math.round(origW*cropH/origH);this.height=cropH;}else{this.width=cropW;this.height=Math.round(origH*cropW/origW);}
if(settings.imgClass){$origImg.addClass(settings.imgClass);}
if(!settings.crop){$curImg.replaceWith($origImg);return;}
cont=$(document.createElement('div'));cont.addClass("resize-and-crop");if(settings.preserveSize){cont.width(reqW).height(reqH);}else{cont.width(cropW).height(cropH);if(settings.center){$origImg.css('left',- Math.max(0,Math.round((this.width- cropW)/ 2 ) ) );
if(settings.smart&&this.height/this.width>1.2){$origImg.css('top',0);}else{$origImg.css('top',- Math.max(0,Math.round((this.height- cropH)/ 2 ) ) );
}}}
if(settings.contClass){cont.addClass(settings.contClass);}
cont.append($origImg);$curImg.replaceWith(cont);}};})(jQuery);