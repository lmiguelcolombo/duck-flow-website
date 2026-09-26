(() => {
  const reduceMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduceMotion || !('IntersectionObserver' in window)) return;

  const headings = [...document.querySelectorAll('[data-text-reveal]')];
  const fadeTargets = [
    ...document.querySelectorAll('[data-text-fade]'),
    ...document.querySelectorAll('.section-heading > p, .dark-intro > p, .region-grid > div:first-child > p, .faq-grid > div:first-child > p, .contact-heading > p')
  ];

  // Retain <em> and <br> so brand colors, line breaks, and heading semantics survive.
  for (const heading of headings) {
    const accessibleText = heading.innerText.replace(/\s+/g, ' ').trim();
    const walker = document.createTreeWalker(heading, NodeFilter.SHOW_TEXT);
    const textNodes = [];
    while (walker.nextNode()) textNodes.push(walker.currentNode);
    let wordIndex = 0;

    for (const node of textNodes) {
      const fragment = document.createDocumentFragment();
      for (const piece of node.textContent.match(/\S+|\s+/g) || []) {
        if (/^\s+$/.test(piece)) {
          fragment.append(document.createTextNode(piece));
          continue;
        }
        const wrap = document.createElement('span');
        wrap.className = 'word-wrap';
        const inner = document.createElement('span');
        inner.className = 'word-inner';
        inner.style.setProperty('--reveal-delay', (wordIndex++ * 40) + 'ms');
        inner.textContent = piece;
        wrap.append(inner);
        fragment.append(wrap);
      }
      node.replaceWith(fragment);
    }
    heading.setAttribute('aria-label', accessibleText);
  }

  const itemTargets = [];
  const itemGroups = [
    '.signal-grid > div',
    '.service-grid > .service-card',
    '.process-list > article',
    '.advantage-list > article',
    '.faq-list > .faq-row',
    '.contact-aside ol > li',
    '.region-card',
    '.contact-form'
  ];

  for (const selector of itemGroups) {
    document.querySelectorAll(selector).forEach((element, index) => {
      element.dataset.itemReveal = '';
      element.style.setProperty('--item-delay', Math.min(index, 5) * 100 + 'ms');
      element.addEventListener('animationend', event => {
        if (event.animationName === 'fadeSlideIn') element.classList.add('reveal-done');
      });
      itemTargets.push(element);
    });
  }

  for (const element of fadeTargets) element.dataset.textFade = '';
  document.documentElement.classList.add('motion-ready');

  const wordObserver = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
      } else if (entry.boundingClientRect.top > window.innerHeight * .88) {
        entry.target.classList.remove('is-visible');
      }
    }
  }, {threshold: .12, rootMargin: '0px 0px -8% 0px'});
  headings.forEach(heading => wordObserver.observe(heading));

  const fadeObserver = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (!entry.isIntersecting) continue;
      entry.target.classList.add('is-visible');
      fadeObserver.unobserve(entry.target);
    }
  }, {threshold: .15, rootMargin: '0px 0px -8% 0px'});
  new Set([...fadeTargets, ...itemTargets]).forEach(element => fadeObserver.observe(element));
  document.documentElement.classList.add('motion-initialized');
})();
