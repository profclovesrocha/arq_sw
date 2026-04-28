const pages = ['landing','sobre','locais','categorias','login','dashboard'];
let mapInitialized = false;
let user_id = null; // Variável global de autenticação

function goTo(id) {
  pages.forEach(p => {
    const el = document.getElementById('page-' + p);
    if (el) { el.classList.remove('active'); el.style.display = 'none'; }
  });
  const target = document.getElementById('page-' + id);
  if (target) { target.style.display = 'block'; target.classList.add('active'); }
  window.scrollTo(0, 0);
  if (id === 'dashboard' && !mapInitialized) { initMap(); mapInitialized = true; }
}

function toggleMenu() { 
    document.getElementById('hamburger').classList.toggle('open'); 
    document.getElementById('mobile-menu').classList.toggle('open'); 
}

function closeMenu() { 
    document.getElementById('hamburger').classList.remove('open'); 
    document.getElementById('mobile-menu').classList.remove('open'); 
}

function switchTab(tab) {
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('form-entrar').style.display = tab === 'entrar' ? 'block' : 'none';
  document.getElementById('form-cadastro').style.display = tab === 'cadastro' ? 'block' : 'none';
  if(event) event.target.classList.add('active');
}

function selectHeat(btn) {
  document.querySelectorAll('.heat-btn').forEach(b => b.classList.remove('selected'));
  btn.classList.add('selected');
}

// 🔐 INTEGRAÇÃO: FAZER LOGIN API
async function fazerLogin() {
  const email = document.getElementById("login-email").value;
  const senha = document.getElementById("login-senha").value;

  if(!email || !senha) { alert("Preencha todos os campos!"); return; }

  try {
    const res = await fetch("/login", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ email, senha })
    });
    const data = await res.json();

    if (res.ok && data.status === "ok") {
      user_id = data.user_id; // Salva o ID real
      goTo('dashboard');
      carregarPosts(); // Puxa o feed do banco!
    } else {
      alert("Erro no login: " + (data.msg || "Credenciais inválidas"));
    }
  } catch (err) {
    alert("Servidor backend não encontrado. O Flask está rodando?");
  }
}

// 📝 INTEGRAÇÃO: CADASTRAR USUÁRIO API
async function fazerCadastro() {
  const email = document.getElementById("reg-email").value;
  const senha = document.getElementById("reg-senha").value;

  if(!email || !senha) { alert("Preencha e-mail e senha!"); return; }

  try {
    const res = await fetch("/register", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ email, senha })
    });

    if (res.ok) {
      alert("Conta criada com sucesso! Faça login para entrar.");
      switchTab('entrar'); 
    } else {
      const data = await res.json();
      alert("Erro no cadastro: " + data.msg);
    }
  } catch (err) {
    alert("Servidor backend não encontrado. O Flask está rodando?");
  }
}

// 💬 INTEGRAÇÃO: CRIAR POST API
async function criarPost() {
  const conteudo = document.getElementById("post-conteudo").value;

  if (!user_id) { alert("Você precisa estar logado para postar!"); return; }
  if (!conteudo.trim()) { alert("Escreva algo antes de postar."); return; }

  try {
    await fetch("/posts", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ conteudo: conteudo, user_id: user_id })
    });

    document.getElementById("post-conteudo").value = "";
    carregarPosts(); // Atualiza o feed com o novo post
  } catch (err) {
    alert("Erro ao conectar com o banco de dados.");
  }
}

// 📥 INTEGRAÇÃO: LER FEED API
// 📥 INTEGRAÇÃO: LER FEED API (MISTURANDO COM DADOS MOCKADOS)
async function carregarPosts() {
  try {
    const res = await fetch("/posts");
    if(!res.ok) return;

    const posts = await res.json();
    const feed = document.getElementById("feed-list");
    
    // Se não tiver posts no banco, não faz nada e deixa os mockados na tela
    if (posts.length === 0) return;

    // Se tiver posts novos no banco, vamos colocar eles ANTES dos falsos
    // Primeiro, vamos varrer apenas os posts que vieram do banco
    posts.reverse().forEach(p => {
      // Cria uma ID única no HTML para não duplicar se a função rodar duas vezes
      const postHtmlId = `post-db-${p.id}`;
      
      if (!document.getElementById(postHtmlId)) {
        const newPost = `
          <div class="feed-item" id="${postHtmlId}" style="animation:fadeIn 0.3s ease; background: var(--orange-pale);">
            <div class="fi-top">
              <div class="fi-avatar" style="background:var(--orange);">U${p.user_id}</div>
              <div class="fi-meta">
                <div class="fi-user">Usuário ${p.user_id} <span style="font-size: 0.6rem; background: var(--orange); color: white; padding: 2px 4px; border-radius: 4px;">NOVO</span></div>
                <div class="fi-loc">em <span>Pernambuco</span></div>
              </div>
              <div class="fi-time">agora mesmo</div>
            </div>
            <div class="fi-content">${escapeHtml(p.conteudo)}</div>
            <div class="fi-footer">
              <span class="fi-heat-badge heat-warm">Movimentando</span>
              <span class="fi-react" onclick="reactPost(this)">♥ 0</span>
            </div>
          </div>
        `;
        // Insere o post real do banco no TOPO da lista (acima dos falsos)
        feed.insertAdjacentHTML('afterbegin', newPost);
      }
    });
  } catch (err) {
    console.log("Servidor não está rodando ou erro ao buscar posts.");
  }
}

function escapeHtml(t) { return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function reactPost(el) { const parts = el.textContent.split(' '); const count = parseInt(parts[1] || '0') + 1; el.textContent = '♥ ' + count; el.style.color = 'var(--orange)'; }

// Função do Mapa
function initMap() {
  const map = L.map('dash-map', { center: [-8.0631, -34.8711], zoom: 13, zoomControl: false });
  L.control.zoom({ position: 'bottomright' }).addTo(map);
  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', { maxZoom: 19 }).addTo(map);
  function makeIcon() { return L.divIcon({ className: '', html: `<div style="width:14px;height:14px;border-radius:50%;background:#F04E00;box-shadow:0 0 0 4px rgba(240,78,0,0.25);"></div>`, iconSize: [14, 14], iconAnchor: [7, 7] }); }
  function addHeat(lat, lng, radius, intensity) { L.circle([lat, lng], { radius, fillColor: '#F04E00', fillOpacity: intensity * 0.32, color: '#F04E00', weight: 0 }).addTo(map); }

  const spots = [
    { lat:-8.0631, lng:-34.8711, label:'Show — Alceu Valença', local:'Marco Zero', heat:'Bombando', r:400, i:0.9 },
    { lat:-8.0090, lng:-34.8550, label:'Carnaval de Olinda', local:'Olinda', heat:'Bombando', r:500, i:0.85 }
  ];
  spots.forEach(s => {
    addHeat(s.lat, s.lng, s.r, s.i);
    L.marker([s.lat, s.lng], { icon: makeIcon() }).addTo(map).bindPopup(`<b>${s.label}</b><br>${s.local}`);
  });
}