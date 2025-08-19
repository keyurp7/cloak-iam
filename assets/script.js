(function () {
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  const savedTheme = localStorage.getItem('theme');
  const isDark = savedTheme ? savedTheme === 'dark' : prefersDark;
  document.documentElement.dataset.theme = isDark ? 'dark' : 'light';
})();

window.addEventListener('DOMContentLoaded', () => {
  const themeToggle = document.getElementById('themeToggle');
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  const yearEl = document.getElementById('year');

  if (yearEl) yearEl.textContent = new Date().getFullYear();

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const current = document.documentElement.dataset.theme || 'light';
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.dataset.theme = next;
      localStorage.setItem('theme', next);
      themeToggle.textContent = next === 'dark' ? '🌙' : '☀️';
    });
  }

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  // Try to hydrate from resume.json if present
  hydrateFromResumeJson();
});

async function hydrateFromResumeJson() {
  try {
    const response = await fetch('assets/resume.json', { cache: 'no-store' });
    if (!response.ok) return;
    const data = await response.json();

    setText('YOUR NAME', data.basics?.name, 'title');
    setBrandName(data.basics?.name);
    setContact(data.basics);
    setStats(data.stats);
    setSummary(data.basics?.summary);
    setSkills(data.skills);
    setExperience(data.work);
    setCerts(data.certifications);
    setProjects(data.projects);
    setWriting(data.writing);

    if (data.basics?.website) document.title = `${data.basics.name} — IAM Specialist`;
  } catch (_) {
    // ignore
  }
}

function setBrandName(name) {
  const brand = document.querySelector('.brand span');
  if (brand && name) brand.textContent = name;
}

function setText(placeholder, value) {
  if (!value) return;
  document.body.innerHTML = document.body.innerHTML.replaceAll(placeholder, value);
}

function setContact(basics) {
  if (!basics) return;
  const emailLink = document.getElementById('contactEmail');
  if (emailLink && basics.email) {
    emailLink.textContent = basics.email;
    emailLink.href = `mailto:${basics.email}`;
  }
  const li = document.getElementById('contactLinkedIn');
  if (li && basics.profiles) {
    const linkedIn = basics.profiles.find(p => /linkedin/i.test(p.network));
    if (linkedIn) { li.textContent = linkedIn.username || linkedIn.url; li.href = linkedIn.url; }
  }
  const gh = document.getElementById('contactGitHub');
  if (gh && basics.profiles) {
    const github = basics.profiles.find(p => /github/i.test(p.network));
    if (github) { gh.textContent = github.username || github.url; gh.href = github.url; }
  }
}

function setStats(stats) {
  if (!stats) return;
  if (stats.yearsInIam) {
    const el = document.getElementById('statYears');
    if (el) el.textContent = stats.yearsInIam;
  }
  if (stats.clouds) {
    const el = document.getElementById('statClouds');
    if (el) el.textContent = stats.clouds.join(' · ');
  }
  if (stats.certs) {
    const el = document.getElementById('statCerts');
    if (el) el.textContent = stats.certs.join(', ');
  }
}

function setSummary(summary) {
  const el = document.getElementById('aboutSummary');
  if (el && summary) el.textContent = summary;
}

function setSkills(skills) {
  const wrap = document.getElementById('skills');
  if (!wrap || !Array.isArray(skills)) return;
  wrap.innerHTML = '';
  skills.forEach(s => {
    const span = document.createElement('span');
    span.className = 'chip';
    span.textContent = s;
    wrap.appendChild(span);
  });
}

function setExperience(work) {
  const list = document.getElementById('experienceList');
  if (!list || !Array.isArray(work)) return;
  list.innerHTML = '';
  work.forEach(item => {
    const article = document.createElement('article');
    article.className = 'timeline-item';
    const header = document.createElement('header');
    const h3 = document.createElement('h3');
    h3.textContent = `${item.position} · ${item.name}`;
    const meta = document.createElement('div');
    meta.className = 'meta';
    meta.textContent = [item.startDate, item.endDate || 'Present'].filter(Boolean).join(' — ');
    header.appendChild(h3);
    header.appendChild(meta);
    const ul = document.createElement('ul');
    (item.highlights || []).forEach(pt => { const li = document.createElement('li'); li.textContent = pt; ul.appendChild(li); });
    article.appendChild(header);
    article.appendChild(ul);
    list.appendChild(article);
  });
}

function setCerts(certs) {
  const ul = document.getElementById('certList');
  if (!ul || !Array.isArray(certs)) return;
  ul.innerHTML = '';
  certs.forEach(c => {
    const li = document.createElement('li');
    li.className = 'card';
    li.textContent = c;
    ul.appendChild(li);
  });
}

function setProjects(projects) {
  const grid = document.getElementById('projectGrid');
  if (!grid || !Array.isArray(projects)) return;
  grid.innerHTML = '';
  projects.forEach(p => {
    const card = document.createElement('article');
    card.className = 'card';
    const h3 = document.createElement('h3');
    h3.textContent = p.name;
    const pEl = document.createElement('p');
    pEl.textContent = p.summary;
    const actions = document.createElement('div'); actions.className = 'card-actions';
    if (p.url) { const a = document.createElement('a'); a.href = p.url; a.className = 'btn btn-ghost'; a.textContent = 'View'; actions.appendChild(a); }
    card.appendChild(h3); card.appendChild(pEl); card.appendChild(actions);
    grid.appendChild(card);
  });
}

function setWriting(posts) {
  const ul = document.querySelector('#writing .list');
  if (!ul || !Array.isArray(posts)) return;
  ul.innerHTML = '';
  posts.forEach(post => {
    const li = document.createElement('li');
    const a = document.createElement('a');
    a.href = post.url; a.textContent = post.title;
    li.appendChild(a); ul.appendChild(li);
  });
}

