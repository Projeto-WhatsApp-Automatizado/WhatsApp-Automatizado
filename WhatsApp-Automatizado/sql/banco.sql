CREATE TABLE public.usuario (
    id bigint NOT NULL,
    nome character varying NOT NULL,
    email character varying NOT NULL,
    telefone character varying NOT NULL,
    estado character varying,
    interesse character varying
);


--
-- TOC entry 215 (class 1259 OID 24579)
-- Name: Usuario_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public."Usuario_usuario_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4856 (class 0 OID 0)
-- Dependencies: 215
-- Name: Usuario_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public."Usuario_usuario_id_seq" OWNED BY public.usuario.id;


--
-- TOC entry 230 (class 1259 OID 41010)
-- Name: administrador; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.administrador (
    id bigint NOT NULL,
    nome character varying,
    email character varying,
    senha character varying,
    nivel_acesso character varying,
    data_cadastro date,
    status character varying
);


--
-- TOC entry 229 (class 1259 OID 41009)
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.administrador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4857 (class 0 OID 0)
-- Dependencies: 229
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.administrador_id_seq OWNED BY public.administrador.id;


--
-- TOC entry 224 (class 1259 OID 40963)
-- Name: atendimento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.atendimento (
    id bigint NOT NULL,
    assunto character varying,
    status character varying,
    data_abertura date,
    data_fechamento date,
    usuario_id integer
);


--
-- TOC entry 223 (class 1259 OID 40962)
-- Name: atendimento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.atendimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4858 (class 0 OID 0)
-- Dependencies: 223
-- Name: atendimento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.atendimento_id_seq OWNED BY public.atendimento.id;


--
-- TOC entry 218 (class 1259 OID 32789)
-- Name: curso; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.curso (
    id bigint NOT NULL,
    nome character varying,
    descricao character varying,
    carga_horaria integer,
    valor double precision,
    inicio_aulas date,
    status boolean,
    edital_id integer
);


--
-- TOC entry 217 (class 1259 OID 32788)
-- Name: curso_curso_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.curso_curso_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4859 (class 0 OID 0)
-- Dependencies: 217
-- Name: curso_curso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.curso_curso_id_seq OWNED BY public.curso.id;


--
-- TOC entry 220 (class 1259 OID 32798)
-- Name: edital; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.edital (
    id bigint NOT NULL,
    nome character varying,
    descricao character varying,
    banca character varying,
    data_cadastro date,
    data_prova date,
    status boolean
);


--
-- TOC entry 219 (class 1259 OID 32797)
-- Name: edital_edital_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.edital_edital_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4860 (class 0 OID 0)
-- Dependencies: 219
-- Name: edital_edital_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.edital_edital_id_seq OWNED BY public.edital.id;


--
-- TOC entry 232 (class 1259 OID 41019)
-- Name: historico_chatbot; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.historico_chatbot (
    id bigint NOT NULL,
    mensagem character varying,
    resposta character varying,
    data_hora timestamp without time zone,
    usuario_id integer
);


--
-- TOC entry 231 (class 1259 OID 41018)
-- Name: historico_chatbot_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.historico_chatbot_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4861 (class 0 OID 0)
-- Dependencies: 231
-- Name: historico_chatbot_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.historico_chatbot_id_seq OWNED BY public.historico_chatbot.id;


--
-- TOC entry 222 (class 1259 OID 32812)
-- Name: interesse; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.interesse (
    id bigint NOT NULL,
    origem character varying,
    data date,
    usuario_id integer,
    curso_id integer,
    edital_id integer
);


--
-- TOC entry 221 (class 1259 OID 32811)
-- Name: interesse_interesse_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.interesse_interesse_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4862 (class 0 OID 0)
-- Dependencies: 221
-- Name: interesse_interesse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.interesse_interesse_id_seq OWNED BY public.interesse.id;


--
-- TOC entry 228 (class 1259 OID 40986)
-- Name: matricula; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.matricula (
    id bigint NOT NULL,
    status character varying,
    data_matricula date,
    observacoes character varying,
    usuario_id integer,
    curso_id integer
);


--
-- TOC entry 227 (class 1259 OID 40985)
-- Name: matricula_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.matricula_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4863 (class 0 OID 0)
-- Dependencies: 227
-- Name: matricula_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.matricula_id_seq OWNED BY public.matricula.id;


--
-- TOC entry 226 (class 1259 OID 40977)
-- Name: pagamento; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pagamento (
    id bigint NOT NULL,
    valor double precision,
    forma_pagamento character varying,
    status character varying,
    data_pagamento date,
    observacoes character varying,
    matricula_id integer
);


--
-- TOC entry 225 (class 1259 OID 40976)
-- Name: pagamento_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.pagamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- TOC entry 4864 (class 0 OID 0)
-- Dependencies: 225
-- Name: pagamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.pagamento_id_seq OWNED BY public.pagamento.id;


--
-- TOC entry 4681 (class 2604 OID 41013)
-- Name: administrador id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id SET DEFAULT nextval('public.administrador_id_seq'::regclass);


--
-- TOC entry 4678 (class 2604 OID 40966)
-- Name: atendimento id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.atendimento ALTER COLUMN id SET DEFAULT nextval('public.atendimento_id_seq'::regclass);


--
-- TOC entry 4675 (class 2604 OID 32792)
-- Name: curso id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.curso ALTER COLUMN id SET DEFAULT nextval('public.curso_curso_id_seq'::regclass);


--
-- TOC entry 4676 (class 2604 OID 32801)
-- Name: edital id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.edital ALTER COLUMN id SET DEFAULT nextval('public.edital_edital_id_seq'::regclass);


--
-- TOC entry 4682 (class 2604 OID 41022)
-- Name: historico_chatbot id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historico_chatbot ALTER COLUMN id SET DEFAULT nextval('public.historico_chatbot_id_seq'::regclass);


--
-- TOC entry 4677 (class 2604 OID 32815)
-- Name: interesse id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.interesse ALTER COLUMN id SET DEFAULT nextval('public.interesse_interesse_id_seq'::regclass);


--
-- TOC entry 4680 (class 2604 OID 40989)
-- Name: matricula id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula ALTER COLUMN id SET DEFAULT nextval('public.matricula_id_seq'::regclass);


--
-- TOC entry 4679 (class 2604 OID 40980)
-- Name: pagamento id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pagamento ALTER COLUMN id SET DEFAULT nextval('public.pagamento_id_seq'::regclass);


--
-- TOC entry 4674 (class 2604 OID 32770)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public."Usuario_usuario_id_seq"'::regclass);


--
-- TOC entry 4684 (class 2606 OID 32772)
-- Name: usuario Usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT "Usuario_pkey" PRIMARY KEY (id);


--
-- TOC entry 4698 (class 2606 OID 41017)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- TOC entry 4692 (class 2606 OID 40970)
-- Name: atendimento atendimento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.atendimento
    ADD CONSTRAINT atendimento_pkey PRIMARY KEY (id);


--
-- TOC entry 4686 (class 2606 OID 32796)
-- Name: curso curso_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_pkey PRIMARY KEY (id);


--
-- TOC entry 4688 (class 2606 OID 32805)
-- Name: edital edital_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.edital
    ADD CONSTRAINT edital_pkey PRIMARY KEY (id);


--
-- TOC entry 4690 (class 2606 OID 32819)
-- Name: interesse interesse_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT interesse_pkey PRIMARY KEY (id);


--
-- TOC entry 4696 (class 2606 OID 40993)
-- Name: matricula matricula_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT matricula_pkey PRIMARY KEY (id);


--
-- TOC entry 4694 (class 2606 OID 40984)
-- Name: pagamento pagamento_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pagamento
    ADD CONSTRAINT pagamento_pkey PRIMARY KEY (id);


--
-- TOC entry 4700 (class 2606 OID 32825)
-- Name: interesse curso_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT curso_id FOREIGN KEY (curso_id) REFERENCES public.curso(id) NOT VALID;


--
-- TOC entry 4705 (class 2606 OID 40999)
-- Name: matricula curso_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT curso_id FOREIGN KEY (curso_id) REFERENCES public.curso(id) NOT VALID;


--
-- TOC entry 4701 (class 2606 OID 32830)
-- Name: interesse edital_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT edital_id FOREIGN KEY (edital_id) REFERENCES public.edital(id) NOT VALID;


--
-- TOC entry 4699 (class 2606 OID 32806)
-- Name: curso edital_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.curso
    ADD CONSTRAINT edital_id FOREIGN KEY (edital_id) REFERENCES public.edital(id) NOT VALID;


--
-- TOC entry 4704 (class 2606 OID 41004)
-- Name: pagamento matricula_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pagamento
    ADD CONSTRAINT matricula_id FOREIGN KEY (matricula_id) REFERENCES public.matricula(id) NOT VALID;


--
-- TOC entry 4702 (class 2606 OID 32820)
-- Name: interesse usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4703 (class 2606 OID 40971)
-- Name: atendimento usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.atendimento
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4706 (class 2606 OID 40994)
-- Name: matricula usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4707 (class 2606 OID 41025)
-- Name: historico_chatbot usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.historico_chatbot
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


-- Completed on 2026-07-09 09:53:58

--
-- PostgreSQL database dump complete
--

