CSS = """
*{box-sizing:border-box}
html,body,#root{height:100%}
body{
    margin:0;
    font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Helvetica,Arial;
    background:#212121;           
    color:#eaeaea;
}
.page{
    height:100vh;
    display:flex;
    align-items:center;
    justify-content:center;
    padding:24px; 
    overflow:hidden;                 
}
.card{
    width:100%;
    max-width:700px;
    height: min(800px, calc(100vh - 48px));              
    display:flex;
    flex-direction:column;
    border:1px solid #2b2b2b;
    border-radius:16px;
    background:#242424;          
    overflow:hidden;
    box-shadow:0 8px 24px rgba(0,0,0,.35);
}
/* Header */
.header{
    height:56px;
    display:flex;
    align-items:center;
    gap:12px;
    padding:0 16px;
    background:#242424;
    border-bottom:1px solid #2b2b2b;
}
.header .avatar{width:36px;height:36px;border-radius:50%;background:#2f2f2f}
.header .title{display:flex;flex-direction:column}
.header .name{font-weight:600;font-size:16px}
.header .status{font-size:12px;opacity:.7}
/* Área conversación */
.chat {
    flex:1;
    display:flex;
    flex-direction:column;
    overflow:hidden;
    min-height: 0; 
}
.scroll {
    flex: 1;
    overflow-y: auto;   
    padding: 18px 20px;
    min-height: 0;
    overscroll-behavior:contain;
}

.scroll::-webkit-scrollbar {
    width: 6px; /* delgado */
}

.scroll::-webkit-scrollbar-track {
    background: transparent;  /* sin fondo blanco */
}

.scroll::-webkit-scrollbar-thumb {
    background-color: #303030; /* mismo color que las burbujas */
    border-radius: 8px;
}

.scroll::-webkit-scrollbar-thumb:hover {
    background-color: #3a3a3a; /* un poco más claro al pasar el mouse */
}

/* Firefox */
.scroll {
    scrollbar-width: thin;                 
    scrollbar-color: #303030 transparent;  
}

/* Mensajes */
.row{display:flex;width:100%}
.row.left{justify-content:flex-start}
.row.right{justify-content:flex-end}
.msg{
    max-width:min(78%,720px);
    margin:8px 0;
    padding:10px 12px;
    border-radius:14px;
    line-height:1.4;
    font-size:15px;
    word-wrap:break-word;
    white-space:pre-wrap;
    position:relative;
    background:#303030;           
    border:1px solid #3a3a3a;
    color:#eee;
}
.msg.sent:after{
    content:"";
    position:absolute;top:0;right:-10px;
    border-width:0 0 10px 10px;border-style:solid;
    border-color:transparent transparent transparent #303030;
}
.msg.received:after{
    content:"";
    position:absolute;top:0;left:-10px;
    border-width:0 10px 10px 0;border-style:solid;
    border-color:transparent #303030 transparent transparent;
}
.meta{display:inline-flex;gap:8px;align-items:center;font-size:11px;opacity:.7;margin-top:4px}

/* Estado de carga */
.typing-indicator {
    display: inline-flex;
    gap: 4px;
    padding: 8px 12px;
    background: #303030;
    border-radius: 14px;
}

.typing-dot {
    width: 8px;
    height: 8px;
    background: #888;
    border-radius: 50%;
    animation: typing 1.4s infinite ease-in-out;
}

.typing-dot:nth-child(1) { animation-delay: -0.32s; }
.typing-dot:nth-child(2) { animation-delay: -0.16s; }

@keyframes typing {
    0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
    40% { transform: scale(1); opacity: 1; }
}

/* Composer */
.composer{
    display:grid;
    grid-template-columns:1fr auto;
    gap:10px;
    padding:12px;
    border-top:1px solid #2b2b2b;
    background:#242424;
}
.input{
    border:1px solid #3a3a3a;
    background:#303030;
    color:#eaeaea;
    border-radius:12px;
    padding:12px 14px;
    font-size:15px;
    outline:none;
}
.input::placeholder{color:#b9b9b9}
.button{
    border:1px solid #ffffff;
    background:#ffffff;
    color:#111111;
    border-radius:12px;
    padding:12px 16px;
    font-weight:700;
    cursor:pointer;
}
.button:disabled{opacity:.6;cursor:not-allowed}
@media(max-width:768px){.msg{max-width:88%}}
"""