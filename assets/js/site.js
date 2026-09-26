const menuButton = document.querySelector('.menu-toggle');
const menu = document.querySelector('#main-nav');
if (menuButton && menu) {
  function setMenu(open) {
    menu.classList.toggle('open', open);
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.setAttribute('aria-label', open ? 'Fechar menu' : 'Abrir menu');
  }
  menuButton.addEventListener('click', () => setMenu(!menu.classList.contains('open')));
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') setMenu(false);
  });
  matchMedia('(min-width: 801px)').addEventListener('change', event => {
    if (event.matches) setMenu(false);
  });
}

const form = document.querySelector('#contact-form');
if (form) {
  const status = document.querySelector('#form-status');
  const fields = [...form.querySelectorAll('[required]')];

  fields.forEach(field => field.addEventListener('input', () => {
    field.removeAttribute('aria-invalid');
    status.textContent = '';
  }));

  form.addEventListener('submit', event => {
    event.preventDefault();
    const invalid = fields.filter(field => {
      const empty = !field.value.trim();
      const badEmail = field.type === 'email' && !field.checkValidity();
      const badPhone = field.name === 'whatsapp' && field.value.replace(/\D/g, '').length < 10;
      const bad = empty || badEmail || badPhone;
      field.setAttribute('aria-invalid', String(bad));
      return bad;
    });

    if (invalid.length) {
      status.textContent = 'Confira os campos destacados antes de continuar.';
      invalid[0].focus();
      return;
    }

    const data = Object.fromEntries(new FormData(form).entries());
    const message = [
      'Olá, Duck Flow! Quero agendar uma sessão gratuita de mapeamento.',
      '',
      'Nome: ' + data.nome.trim(),
      'Empresa: ' + data.empresa.trim(),
      'E-mail: ' + data.email.trim(),
      'WhatsApp: ' + data.whatsapp.trim(),
      'Frente de interesse: ' + data.frente,
      data.mensagem.trim() ? 'Gargalo atual: ' + data.mensagem.trim() : ''
    ].filter(Boolean).join('\n');

    const link = document.createElement('a');
    link.href = 'https://wa.me/5554984384244?text=' + encodeURIComponent(message);
    link.target = '_blank';
    link.rel = 'noopener noreferrer';
    document.body.append(link);
    link.click();
    link.remove();
    status.textContent = 'Conversa preparada no WhatsApp. Confirme o envio por lá.';
  });
}


// Branded selection control from design-system-v2.html; the native select keeps form data and no-JS fallback.
const interestSelect = document.querySelector('#interest-select');
if (interestSelect) {
  const trigger = interestSelect.querySelector('.select-trigger');
  const panel = interestSelect.querySelector('.select-panel');
  const value = interestSelect.querySelector('#interest-value');
  const nativeSelect = interestSelect.querySelector('.select-native');
  const options = [...interestSelect.querySelectorAll('.select-option')];

  function setOpen(open, focusOption = false) {
    interestSelect.classList.toggle('open', open);
    trigger.setAttribute('aria-expanded', String(open));
    panel.setAttribute('aria-hidden', String(!open));
    if (open && focusOption) {
      (options.find(option => option.getAttribute('aria-selected') === 'true') || options[0]).focus();
    }
  }

  function choose(option) {
    options.forEach(item => item.setAttribute('aria-selected', String(item === option)));
    value.textContent = option.dataset.value;
    nativeSelect.value = option.dataset.value;
    nativeSelect.dispatchEvent(new Event('change', {bubbles: true}));
    interestSelect.classList.add('has-value');
    setOpen(false);
    trigger.focus();
  }

  trigger.addEventListener('click', () => setOpen(!interestSelect.classList.contains('open'), true));
  options.forEach(option => option.addEventListener('click', () => choose(option)));
  interestSelect.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      if (interestSelect.classList.contains('open')) {
        event.preventDefault();
        setOpen(false);
        trigger.focus();
      }
      return;
    }
    if (event.key === 'ArrowDown' || event.key === 'ArrowUp') {
      event.preventDefault();
      if (!interestSelect.classList.contains('open')) {
        setOpen(true, true);
        return;
      }
      const current = options.indexOf(document.activeElement);
      const step = event.key === 'ArrowDown' ? 1 : -1;
      options[(current + step + options.length) % options.length].focus();
    }
  });
  interestSelect.addEventListener('focusout', event => {
    if (!interestSelect.contains(event.relatedTarget)) setOpen(false);
  });
  document.addEventListener('pointerdown', event => {
    if (!interestSelect.contains(event.target)) setOpen(false);
  });
  document.documentElement.classList.add('custom-select-ready');
}
// Same particle glyph specimen as design-system-v2.html.
  const glyphCanvas=document.querySelector('#glyphCanvas');
  if(glyphCanvas){
    const gctx=glyphCanvas.getContext('2d');const width=glyphCanvas.width,height=glyphCanvas.height;
    const particles=[];let pointer={x:-999,y:-999},running=false,raf=0,selectedGlyph='D';
    const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
    function setGlyph(letter){selectedGlyph=letter;
      const off=document.createElement('canvas');off.width=width;off.height=height;
      const ctx=off.getContext('2d');ctx.fillStyle='#000';ctx.textAlign='center';ctx.textBaseline='middle';ctx.font='500 800px Familjen, Arial, sans-serif';ctx.fillText(letter,width/2,height/2+20);
      const data=ctx.getImageData(0,0,width,height).data;const targets=[];
      for(let y=30;y<height-30;y+=10)for(let x=30;x<width-30;x+=10)if(data[(y*width+x)*4+3]>120)targets.push({x,y});
      targets.forEach((target,index)=>{const p=particles[index]||{x:Math.random()*width,y:Math.random()*height,vx:0,vy:0};p.tx=target.x;p.ty=target.y;p.color=index%37===0?'#b97239':index%13===0?'#176947':index%5===0?'#34413c':'#172127';particles[index]=p});particles.length=targets.length;
      glyphCanvas.setAttribute('aria-label',letter==='✦'?'Estrela formada por partículas escuras':'Letra '+letter+' formada por partículas escuras');
      document.querySelectorAll('[data-glyph]').forEach(button=>button.setAttribute('aria-pressed',button.dataset.glyph===letter?'true':'false'));
      if(reduced)drawGlyph(true)
    }
    function drawGlyph(snap=false){
      gctx.clearRect(0,0,width,height);
      for(const p of particles){
        if(snap){p.x=p.tx;p.y=p.ty}
        else{const dx=p.x-pointer.x,dy=p.y-pointer.y,d=Math.hypot(dx,dy);if(d<65&&d>0){p.vx+=dx/d*1.05;p.vy+=dy/d*1.05}p.vx+=(p.tx-p.x)*.032;p.vy+=(p.ty-p.y)*.032;p.vx*=.8;p.vy*=.8;p.x+=p.vx;p.y+=p.vy}
        gctx.fillStyle=p.color;gctx.beginPath();gctx.arc(p.x,p.y,p.color==='#b97239'?2.8:2.35,0,Math.PI*2);gctx.fill()
      }

    }
    function loop(){raf=0;if(!running)return;drawGlyph();raf=requestAnimationFrame(loop)}
    glyphCanvas.addEventListener('pointermove',event=>{const box=glyphCanvas.getBoundingClientRect();pointer={x:(event.clientX-box.left)*width/box.width,y:(event.clientY-box.top)*height/box.height}});
    glyphCanvas.addEventListener('pointerleave',()=>pointer={x:-999,y:-999});
    document.querySelectorAll('[data-glyph]').forEach(button=>button.addEventListener('click',()=>setGlyph(button.dataset.glyph)));
    document.fonts.ready.then(()=>{setGlyph(selectedGlyph);drawGlyph(true);if(!reduced&&!running){running=true;raf=requestAnimationFrame(loop)}});
    const glyphObserver=new IntersectionObserver(entries=>{if(reduced)return;const visible=entries[0].isIntersecting&&!document.hidden;if(visible&&!running){running=true;if(!raf)raf=requestAnimationFrame(loop)}else if(!visible)running=false},{threshold:.05});glyphObserver.observe(glyphCanvas);
    document.addEventListener('visibilitychange',()=>{if(document.hidden)running=false;else if(!reduced&&!running){running=true;if(!raf)raf=requestAnimationFrame(loop)}})
  }
const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
document.querySelectorAll('.faq-list').forEach(faq => {
  document.documentElement.classList.add('faq-ready');
  const rows = [...faq.querySelectorAll('.faq-row')];

  function setRow(row, open) {
    const button = row.querySelector('.faq-q');
    const answer = row.querySelector('.faq-answer');
    const current = answer.getBoundingClientRect().height;
    answer.style.height = current + 'px';
    row.classList.toggle('open', open);
    button.setAttribute('aria-expanded', String(open));
    answer.setAttribute('aria-hidden', String(!open));
    if (reducedMotion) {
      answer.style.height = open ? 'auto' : '0px';
      return;
    }
    requestAnimationFrame(() => {
      answer.style.height = (open ? answer.scrollHeight : 0) + 'px';
    });
  }

  rows.forEach(row => {
    row.querySelector('.faq-q').addEventListener('click', () => {
      const willOpen = !row.classList.contains('open');
      rows.forEach(other => {
        if (other !== row && other.classList.contains('open')) setRow(other, false);
      });
      setRow(row, willOpen);
    });
    row.querySelector('.faq-answer').addEventListener('transitionend', event => {
      if (event.propertyName === 'height' && row.classList.contains('open')) {
        event.currentTarget.style.height = 'auto';
      }
    });
  });
});
