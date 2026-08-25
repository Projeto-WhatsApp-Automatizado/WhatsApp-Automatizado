CREATE TABLE public.usuario (
    id bigint NOT NULL,
    nome character varying NOT NULL,
    email character varying NOT NULL,
    telefone character varying NOT NULL,
    estado character varying,
    interesse character varying
);


ALTER TABLE public.usuario OWNER TO postgres;

--
-- TOC entry 215 (class 1259 OID 24579)
-- Name: Usuario_usuario_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Usuario_usuario_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public."Usuario_usuario_id_seq" OWNER TO postgres;

--
-- TOC entry 4867 (class 0 OID 0)
-- Dependencies: 215
-- Name: Usuario_usuario_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Usuario_usuario_id_seq" OWNED BY public.usuario.id;


--
-- TOC entry 230 (class 1259 OID 41010)
-- Name: administrador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.administrador (
    id integer NOT NULL,
    nome character varying,
    email character varying,
    senha character varying,
    nivel_acesso character varying,
    data_cadastro date,
    status boolean
);


ALTER TABLE public.administrador OWNER TO postgres;

--
-- TOC entry 229 (class 1259 OID 41009)
-- Name: administrador_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.administrador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.administrador_id_seq OWNER TO postgres;

--
-- TOC entry 4868 (class 0 OID 0)
-- Dependencies: 229
-- Name: administrador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.administrador_id_seq OWNED BY public.administrador.id;


--
-- TOC entry 224 (class 1259 OID 40963)
-- Name: atendimento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.atendimento (
    id integer NOT NULL,
    assunto character varying,
    status character varying,
    data_abertura date,
    data_fechamento date,
    usuario_id integer
);


ALTER TABLE public.atendimento OWNER TO postgres;

--
-- TOC entry 223 (class 1259 OID 40962)
-- Name: atendimento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.atendimento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.atendimento_id_seq OWNER TO postgres;

--
-- TOC entry 4869 (class 0 OID 0)
-- Dependencies: 223
-- Name: atendimento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.atendimento_id_seq OWNED BY public.atendimento.id;


--
-- TOC entry 218 (class 1259 OID 32789)
-- Name: curso; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.curso (
    id integer NOT NULL,
    nome character varying,
    descricao character varying,
    carga_horaria integer,
    valor double precision,
    inicio_aulas date,
    status boolean
);


ALTER TABLE public.curso OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 32788)
-- Name: curso_curso_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.curso_curso_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.curso_curso_id_seq OWNER TO postgres;

--
-- TOC entry 4870 (class 0 OID 0)
-- Dependencies: 217
-- Name: curso_curso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.curso_curso_id_seq OWNED BY public.curso.id;


--
-- TOC entry 235 (class 1259 OID 49156)
-- Name: curso_edital; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.curso_edital (
    curso_id integer NOT NULL,
    edital_id integer NOT NULL
);


ALTER TABLE public.curso_edital OWNER TO postgres;

--
-- TOC entry 233 (class 1259 OID 49154)
-- Name: curso_edital_curso_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.curso_edital_curso_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.curso_edital_curso_id_seq OWNER TO postgres;

--
-- TOC entry 4871 (class 0 OID 0)
-- Dependencies: 233
-- Name: curso_edital_curso_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.curso_edital_curso_id_seq OWNED BY public.curso_edital.curso_id;


--
-- TOC entry 234 (class 1259 OID 49155)
-- Name: curso_edital_edital_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.curso_edital_edital_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.curso_edital_edital_id_seq OWNER TO postgres;

--
-- TOC entry 4872 (class 0 OID 0)
-- Dependencies: 234
-- Name: curso_edital_edital_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.curso_edital_edital_id_seq OWNED BY public.curso_edital.edital_id;


--
-- TOC entry 220 (class 1259 OID 32798)
-- Name: edital; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.edital (
    id integer NOT NULL,
    nome character varying,
    descricao character varying,
    banca character varying,
    data_cadastro date,
    data_prova date,
    status boolean
);


ALTER TABLE public.edital OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 32797)
-- Name: edital_edital_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.edital_edital_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.edital_edital_id_seq OWNER TO postgres;

--
-- TOC entry 4873 (class 0 OID 0)
-- Dependencies: 219
-- Name: edital_edital_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.edital_edital_id_seq OWNED BY public.edital.id;


--
-- TOC entry 232 (class 1259 OID 41019)
-- Name: historico_chatbot; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.historico_chatbot (
    id integer NOT NULL,
    mensagem character varying,
    resposta character varying,
    data_hora timestamp without time zone,
    usuario_id integer
);


ALTER TABLE public.historico_chatbot OWNER TO postgres;

--
-- TOC entry 231 (class 1259 OID 41018)
-- Name: historico_chatbot_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.historico_chatbot_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.historico_chatbot_id_seq OWNER TO postgres;

--
-- TOC entry 4874 (class 0 OID 0)
-- Dependencies: 231
-- Name: historico_chatbot_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.historico_chatbot_id_seq OWNED BY public.historico_chatbot.id;


--
-- TOC entry 222 (class 1259 OID 32812)
-- Name: interesse; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.interesse (
    id integer NOT NULL,
    origem character varying,
    data date,
    usuario_id integer,
    curso_id integer,
    edital_id integer
);


ALTER TABLE public.interesse OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 32811)
-- Name: interesse_interesse_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.interesse_interesse_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.interesse_interesse_id_seq OWNER TO postgres;

--
-- TOC entry 4875 (class 0 OID 0)
-- Dependencies: 221
-- Name: interesse_interesse_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.interesse_interesse_id_seq OWNED BY public.interesse.id;


--
-- TOC entry 228 (class 1259 OID 40986)
-- Name: matricula; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.matricula (
    id integer NOT NULL,
    status character varying,
    data_matricula date,
    observacoes character varying,
    usuario_id integer,
    curso_id integer
);


ALTER TABLE public.matricula OWNER TO postgres;

--
-- TOC entry 227 (class 1259 OID 40985)
-- Name: matricula_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.matricula_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.matricula_id_seq OWNER TO postgres;

--
-- TOC entry 4876 (class 0 OID 0)
-- Dependencies: 227
-- Name: matricula_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.matricula_id_seq OWNED BY public.matricula.id;


--
-- TOC entry 226 (class 1259 OID 40977)
-- Name: pagamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pagamento (
    id integer NOT NULL,
    valor double precision,
    forma_pagamento character varying,
    status character varying,
    data_pagamento date,
    observacoes character varying,
    matricula_id integer
);


ALTER TABLE public.pagamento OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 40976)
-- Name: pagamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.pagamento_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.pagamento_id_seq OWNER TO postgres;

--
-- TOC entry 4877 (class 0 OID 0)
-- Dependencies: 225
-- Name: pagamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.pagamento_id_seq OWNED BY public.pagamento.id;


--
-- TOC entry 4687 (class 2604 OID 41013)
-- Name: administrador id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador ALTER COLUMN id SET DEFAULT nextval('public.administrador_id_seq'::regclass);


--
-- TOC entry 4684 (class 2604 OID 40966)
-- Name: atendimento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atendimento ALTER COLUMN id SET DEFAULT nextval('public.atendimento_id_seq'::regclass);


--
-- TOC entry 4681 (class 2604 OID 32792)
-- Name: curso id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso ALTER COLUMN id SET DEFAULT nextval('public.curso_curso_id_seq'::regclass);


--
-- TOC entry 4689 (class 2604 OID 49159)
-- Name: curso_edital curso_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso_edital ALTER COLUMN curso_id SET DEFAULT nextval('public.curso_edital_curso_id_seq'::regclass);


--
-- TOC entry 4690 (class 2604 OID 49160)
-- Name: curso_edital edital_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso_edital ALTER COLUMN edital_id SET DEFAULT nextval('public.curso_edital_edital_id_seq'::regclass);


--
-- TOC entry 4682 (class 2604 OID 32801)
-- Name: edital id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edital ALTER COLUMN id SET DEFAULT nextval('public.edital_edital_id_seq'::regclass);


--
-- TOC entry 4688 (class 2604 OID 41022)
-- Name: historico_chatbot id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historico_chatbot ALTER COLUMN id SET DEFAULT nextval('public.historico_chatbot_id_seq'::regclass);


--
-- TOC entry 4683 (class 2604 OID 32815)
-- Name: interesse id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interesse ALTER COLUMN id SET DEFAULT nextval('public.interesse_interesse_id_seq'::regclass);


--
-- TOC entry 4686 (class 2604 OID 40989)
-- Name: matricula id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula ALTER COLUMN id SET DEFAULT nextval('public.matricula_id_seq'::regclass);


--
-- TOC entry 4685 (class 2604 OID 40980)
-- Name: pagamento id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagamento ALTER COLUMN id SET DEFAULT nextval('public.pagamento_id_seq'::regclass);


--
-- TOC entry 4680 (class 2604 OID 32770)
-- Name: usuario id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario ALTER COLUMN id SET DEFAULT nextval('public."Usuario_usuario_id_seq"'::regclass);


--
-- TOC entry 4692 (class 2606 OID 32772)
-- Name: usuario Usuario_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT "Usuario_pkey" PRIMARY KEY (id);


--
-- TOC entry 4706 (class 2606 OID 41017)
-- Name: administrador administrador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.administrador
    ADD CONSTRAINT administrador_pkey PRIMARY KEY (id);


--
-- TOC entry 4700 (class 2606 OID 40970)
-- Name: atendimento atendimento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atendimento
    ADD CONSTRAINT atendimento_pkey PRIMARY KEY (id);


--
-- TOC entry 4708 (class 2606 OID 49162)
-- Name: curso_edital curso_edital_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso_edital
    ADD CONSTRAINT curso_edital_pkey PRIMARY KEY (curso_id, edital_id);


--
-- TOC entry 4694 (class 2606 OID 32796)
-- Name: curso curso_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso
    ADD CONSTRAINT curso_pkey PRIMARY KEY (id);


--
-- TOC entry 4696 (class 2606 OID 32805)
-- Name: edital edital_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.edital
    ADD CONSTRAINT edital_pkey PRIMARY KEY (id);


--
-- TOC entry 4698 (class 2606 OID 32819)
-- Name: interesse interesse_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT interesse_pkey PRIMARY KEY (id);


--
-- TOC entry 4704 (class 2606 OID 40993)
-- Name: matricula matricula_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT matricula_pkey PRIMARY KEY (id);


--
-- TOC entry 4702 (class 2606 OID 40984)
-- Name: pagamento pagamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagamento
    ADD CONSTRAINT pagamento_pkey PRIMARY KEY (id);


--
-- TOC entry 4709 (class 2606 OID 32825)
-- Name: interesse curso_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT curso_id FOREIGN KEY (curso_id) REFERENCES public.curso(id) NOT VALID;


--
-- TOC entry 4714 (class 2606 OID 40999)
-- Name: matricula curso_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT curso_id FOREIGN KEY (curso_id) REFERENCES public.curso(id) NOT VALID;


--
-- TOC entry 4717 (class 2606 OID 49163)
-- Name: curso_edital curso_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso_edital
    ADD CONSTRAINT curso_id FOREIGN KEY (curso_id) REFERENCES public.curso(id) NOT VALID;


--
-- TOC entry 4710 (class 2606 OID 32830)
-- Name: interesse edital_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT edital_id FOREIGN KEY (edital_id) REFERENCES public.edital(id) NOT VALID;


--
-- TOC entry 4718 (class 2606 OID 49168)
-- Name: curso_edital edital_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.curso_edital
    ADD CONSTRAINT edital_id FOREIGN KEY (edital_id) REFERENCES public.edital(id) NOT VALID;


--
-- TOC entry 4713 (class 2606 OID 41004)
-- Name: pagamento matricula_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pagamento
    ADD CONSTRAINT matricula_id FOREIGN KEY (matricula_id) REFERENCES public.matricula(id) NOT VALID;


--
-- TOC entry 4711 (class 2606 OID 32820)
-- Name: interesse usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.interesse
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4712 (class 2606 OID 40971)
-- Name: atendimento usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.atendimento
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4715 (class 2606 OID 40994)
-- Name: matricula usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.matricula
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


--
-- TOC entry 4716 (class 2606 OID 41025)
-- Name: historico_chatbot usuario_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.historico_chatbot
    ADD CONSTRAINT usuario_id FOREIGN KEY (usuario_id) REFERENCES public.usuario(id) NOT VALID;


-- Completed on 2026-07-28 11:40:18

--
-- PostgreSQL database dump complete
--

