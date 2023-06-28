--
-- PostgreSQL database dump
--

-- Dumped from database version 14.6 (Ubuntu 14.6-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: heroku_ext; Type: SCHEMA; Schema: -; Owner: u5i4rotrbtfceq
--

CREATE SCHEMA heroku_ext;


ALTER SCHEMA heroku_ext OWNER TO u5i4rotrbtfceq;

--
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: -
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA heroku_ext;


--
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track planning and execution statistics of all SQL statements executed';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO wyecuxdxvijnzx;

--
-- Name: categories; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.categories OWNER TO wyecuxdxvijnzx;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: customer; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.customer (
    id integer NOT NULL,
    "sessionId" character varying NOT NULL,
    name character varying,
    "phoneNumber" character varying,
    "numberOfTickets" character varying,
    "typeOfTicket" character varying,
    paid boolean,
    "paymentId" character varying,
    "startDate" character varying,
    event character varying
);


ALTER TABLE public.customer OWNER TO wyecuxdxvijnzx;

--
-- Name: customer_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.customer_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: customer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.customer_id_seq OWNED BY public.customer.id;


--
-- Name: event; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.event (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    description character varying NOT NULL,
    image character varying,
    category character varying,
    "startDate" character varying,
    organiser character varying,
    code character varying
);


ALTER TABLE public.event OWNER TO wyecuxdxvijnzx;

--
-- Name: event_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.event_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.event_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: event_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.event_id_seq OWNED BY public.event.id;


--
-- Name: item; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.item (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    price character varying(10),
    description character varying NOT NULL,
    image character varying,
    trending boolean,
    category character varying NOT NULL,
    vendor integer NOT NULL
);


ALTER TABLE public.item OWNER TO wyecuxdxvijnzx;

--
-- Name: item_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.item_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.item_id_seq OWNED BY public.item.id;


--
-- Name: order; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public."order" (
    id integer NOT NULL,
    name character varying NOT NULL,
    phone character varying NOT NULL,
    price character varying,
    location character varying,
    items character varying
);


ALTER TABLE public."order" OWNER TO wyecuxdxvijnzx;

--
-- Name: order_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.order_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.order_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: order_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.order_id_seq OWNED BY public."order".id;


--
-- Name: poll; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.poll (
    id integer NOT NULL,
    "sessionId" character varying NOT NULL,
    name character varying,
    "phoneNumber" character varying,
    movie character varying,
    "movieConfirm" character varying,
    talanku boolean,
    tlk boolean,
    probability character varying,
    "startDate" character varying,
    event character varying
);


ALTER TABLE public.poll OWNER TO wyecuxdxvijnzx;

--
-- Name: poll_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.poll_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.poll_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: poll_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.poll_id_seq OWNED BY public.poll.id;


--
-- Name: ticket; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.ticket (
    id integer NOT NULL,
    "sessionId" character varying NOT NULL,
    name character varying,
    "phoneNumber" character varying,
    "numberOfTickets" character varying,
    "ticketConfirm" character varying,
    "typeOfTickets" character varying,
    event character varying,
    paid boolean,
    code character varying,
    cost character varying
);


ALTER TABLE public.ticket OWNER TO wyecuxdxvijnzx;

--
-- Name: ticket_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.ticket_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: ticket_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.ticket_id_seq OWNED BY public.ticket.id;


--
-- Name: ticket_transaction; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.ticket_transaction (
    id integer NOT NULL,
    event character varying NOT NULL,
    "customerName" character varying,
    "typeOfTicket" character varying,
    date_created timestamp without time zone,
    amount character varying,
    account character varying,
    ref character varying,
    paid boolean,
    code character varying
);


ALTER TABLE public.ticket_transaction OWNER TO wyecuxdxvijnzx;

--
-- Name: ticket_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.ticket_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ticket_transaction_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: ticket_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.ticket_transaction_id_seq OWNED BY public.ticket_transaction.id;


--
-- Name: transactions; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.transactions (
    id integer NOT NULL,
    candidate character varying NOT NULL,
    "candidateName" character varying,
    award character varying,
    date_created timestamp without time zone,
    amount character varying,
    account character varying,
    ref character varying,
    paid boolean
);


ALTER TABLE public.transactions OWNER TO wyecuxdxvijnzx;

--
-- Name: transactions_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.transactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.transactions_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: transactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.transactions_id_seq OWNED BY public.transactions.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(10) NOT NULL,
    phone character varying(15) NOT NULL,
    password character varying(15)
);


ALTER TABLE public."user" OWNER TO wyecuxdxvijnzx;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: ussd_sessions; Type: TABLE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE TABLE public.ussd_sessions (
    id integer NOT NULL,
    "sessionId" character varying NOT NULL,
    event character varying NOT NULL
);


ALTER TABLE public.ussd_sessions OWNER TO wyecuxdxvijnzx;

--
-- Name: ussd_sessions_id_seq; Type: SEQUENCE; Schema: public; Owner: wyecuxdxvijnzx
--

CREATE SEQUENCE public.ussd_sessions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ussd_sessions_id_seq OWNER TO wyecuxdxvijnzx;

--
-- Name: ussd_sessions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER SEQUENCE public.ussd_sessions_id_seq OWNED BY public.ussd_sessions.id;


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: customer id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.customer ALTER COLUMN id SET DEFAULT nextval('public.customer_id_seq'::regclass);


--
-- Name: event id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.event ALTER COLUMN id SET DEFAULT nextval('public.event_id_seq'::regclass);


--
-- Name: item id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.item ALTER COLUMN id SET DEFAULT nextval('public.item_id_seq'::regclass);


--
-- Name: order id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public."order" ALTER COLUMN id SET DEFAULT nextval('public.order_id_seq'::regclass);


--
-- Name: poll id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.poll ALTER COLUMN id SET DEFAULT nextval('public.poll_id_seq'::regclass);


--
-- Name: ticket id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ticket ALTER COLUMN id SET DEFAULT nextval('public.ticket_id_seq'::regclass);


--
-- Name: ticket_transaction id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ticket_transaction ALTER COLUMN id SET DEFAULT nextval('public.ticket_transaction_id_seq'::regclass);


--
-- Name: transactions id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.transactions ALTER COLUMN id SET DEFAULT nextval('public.transactions_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: ussd_sessions id; Type: DEFAULT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ussd_sessions ALTER COLUMN id SET DEFAULT nextval('public.ussd_sessions_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.alembic_version (version_num) FROM stdin;
175913ab1e9a
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.categories (id, name) FROM stdin;
\.


--
-- Data for Name: customer; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.customer (id, "sessionId", name, "phoneNumber", "numberOfTickets", "typeOfTicket", paid, "paymentId", "startDate", event) FROM stdin;
\.


--
-- Data for Name: event; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.event (id, name, description, image, category, "startDate", organiser, code) FROM stdin;
1	Touchdown0.1	Gay Party	default.jpg	\N	\N	\N	01
\.


--
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.item (id, name, price, description, image, trending, category, vendor) FROM stdin;
\.


--
-- Data for Name: order; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public."order" (id, name, phone, price, location, items) FROM stdin;
\.


--
-- Data for Name: poll; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.poll (id, "sessionId", name, "phoneNumber", movie, "movieConfirm", talanku, tlk, probability, "startDate", event) FROM stdin;
\.


--
-- Data for Name: ticket; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.ticket (id, "sessionId", name, "phoneNumber", "numberOfTickets", "ticketConfirm", "typeOfTickets", event, paid, code, cost) FROM stdin;
41	2000000000275762	Ona	\N	1	1	Regular	TouchBase0.1	\N	Q7EUHSH8OJ	0.2
1	16695638431566855	Kweku	\N	1	1	Regular	TouchBase0.1	\N	\N	\N
2	16695662062462188	Gh	\N	1	\N	Regular	TouchBase0.1	\N	\N	20
12	16695766141561272	Ddd	\N	1	\N	Regular	TouchBase0.1	\N	\N	20
13	16695766421751943	\N	\N	\N	\N	\N	TouchBase0.1	\N	\N	\N
3	16695662861524502	33	\N	1	1	Regular	TouchBase0.1	\N	W5R5OSZCQ4	20
34	851721172	WO MAAME	\N	1	1	Regular	TouchBase0.1	\N	6WGDQ3V9N8	0.2
54	16698881451550765	Kweku	\N	1	1	Regular	TouchBase0.1	\N	\N	20
4	16695672142497302	Kweku	\N	1	\N	Regular	TouchBase0.1	\N	\N	20
23	3000000015576833	Ona	\N	1	1	Regular	TouchBase0.1	\N	MEQURY78LC	20
14	16695766761562001	Nk	\N	1	1	Regular	TouchBase0.1	\N	YB5KXQM6GW	20
5	16695672591545133	Kill	\N	1	1	Regular	TouchBase0.1	\N	J486B2C8JN	20
6	16695675142418209	\N	\N	1	\N	Regular	TouchBase0.1	\N	\N	\N
35	5031258961	MICHELLE, NANA'S LOVER	\N	1	1	Regular	TouchBase0.1	\N	4CLU2UXLO4	0.2
15	16695767911759327	Nk	\N	1	1	Regular	TouchBase0.1	\N	TAOBXJEQ45	20
24	16696654752464804	Graham	\N	1	1	Regular	TouchBase0.1	\N	CW76PCL8M2	20
7	16695754692444018	1	\N	1	1	Regular	TouchBase0.1	\N	YU87RZ62KF	20
42	851858797	JGJM	\N	1	1	Regular	TouchBase0.1	\N	0ZFC05NESR	0.2
16	16695769232486219	Nana Kweku	\N	1	1	Regular	TouchBase0.1	\N	NPXF4YTTJ6	20
8	16695756981548997	Dgd	\N	1	1	Regular	TouchBase0.1	\N	1ATVZMXKJZ	20
49	1000004306115050	Airtel test	\N	1	1	Regular	TouchBase0.1	\N	HY68F6WWWA	0.2
25	16696655572468673	Graham	\N	1	1	Regular	TouchBase0.1	\N	MXSG4CXPXM	20
9	16695758842456285	Jjj	\N	1	1	Regular	TouchBase0.1	\N	9	20
17	3000000014905521	Ona	\N	1	1	Regular	TouchBase0.1	\N	YTHXT7EAN0	20
36	851768974	June	\N	1	1	Regular	TouchBase0.1	\N	98NB80CPOX	0.2
10	16695760132460063	Ad	\N	1	1	Regular	TouchBase0.1	\N	10	20
26	850091652	Maame	\N	1	1	Regular	TouchBase0.1	\N	UDPRL8X036	20
11	16695761552464222	Nk	\N	1	\N	Regular	TouchBase0.1	\N	\N	20
18	847811226	June	\N	1	1	Regular	TouchBase0.1	\N	P2EXBVFZV7	20
27	16696757582453959	\N	\N	\N	\N	\N	TouchBase0.1	\N	\N	\N
28	5029663744	\N	\N	\N	\N	\N	TouchBase0.1	\N	\N	\N
19	847849313	June	\N	1	1	Regular	TouchBase0.1	\N	5PL7C73SPW	20
43	5031401260	law	\N	1	1	Regular	TouchBase0.1	\N	8OLFI5KLNS	0.2
20	16696197731583898	\N	\N	\N	\N	Regular	TouchBase0.1	\N	\N	\N
37	2000000000263088	Keren 	\N	1	1	Regular	TouchBase0.1	\N	DRK1XY2AEL	0.2
21	16696634962456566	Nana Kweku 1	\N	1	1	Regular	TouchBase0.1	\N	BXIPC70Q8Q	20
50	2000000000573804	Airtel test	\N	1	1	Regular	TouchBase0.1	\N	XC9VTEHKNG	0.2
30	16696762001577480	Kweku	\N	1	1	Regular	TouchBase0.1	\N	3MXIH9KM2R	20
22	5029302406	June	\N	1	1	Regular	TouchBase0.1	\N	VSM5H69SGR	20
44	5031418388	law§test	\N	1	1	Regular	TouchBase0.1	\N	UPCNNKM0B1	0.2
29	850155173	life	\N	1	1	Regular	TouchBase0.1	\N	RFHPXYI0U7	20
38	3000000016233293	Nana Kweku test	\N	1	1	Regular	TouchBase0.1	\N	GCI53Z60LQ	0.2
45	16697558871760011	\N	\N	\N	\N	\N	TouchBase0.1	\N	\N	\N
31	850423038	Joseph	\N	1	1	Regular	TouchBase0.1	\N	XVQOVYXLS4	20
46	16697559402452599	\N	\N	\N	\N	\N	TouchBase0.1	\N	\N	\N
39	2000000000268907	Nana Kweku test	\N	1	1	Regular	TouchBase0.1	\N	69F6QWXB9J	0.2
32	851555430	Maame	\N	2	\N	Regular	TouchBase0.1	\N	\N	40
33	851709365	\N	\N	User timeout	\N	Regular	TouchBase0.1	\N	\N	\N
40	2000000000273250	\N	\N	\N	\N	Regular	TouchBase0.1	\N	\N	\N
51	5033771612	\N	\N	User timeout	\N	Regular	TouchBase0.1	\N	\N	\N
52	16698858621583343	\N	\N	\N	\N	Regular	TouchBase0.1	\N	\N	\N
47	852164235	666	\N	1	1	Regular	TouchBase0.1	\N	UZQ5XFF8KD	0.2
53	2000000001365058	Ona	\N	1	\N	Regular	TouchBase0.1	\N	\N	0.2
48	16697563781780296	Kweku	\N	1	1	Regular	TouchBase0.1	\N	R4PZUTCIRN	0.2
\.


--
-- Data for Name: ticket_transaction; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.ticket_transaction (id, event, "customerName", "typeOfTicket", date_created, amount, account, ref, paid, code) FROM stdin;
1	TouchBase0.1	Kweku	Regular	2022-11-27 15:44:20.912562	\N	233545977791	27745906	f	\N
2	TouchBase0.1	33	Regular	2022-11-27 16:25:06.456351	\N	233545977791	27745913	f	\N
3	TouchBase0.1	Kill	Regular	2022-11-27 16:41:14.868088	20	233545977791	27745915	f	J486B2C8JN
4	TouchBase0.1	1	Regular	2022-11-27 18:58:18.153248	20	233545977791	27745946	f	YU87RZ62KF
5	TouchBase0.1	Dgd	Regular	2022-11-27 19:01:54.274816	20	233545977791	27745947	f	1ATVZMXKJZ
6	TouchBase0.1	Jjj	Regular	2022-11-27 19:05:05.433803	20	233545977791	27745948	f	YSOG60IGVZ
7	TouchBase0.1	Ad	Regular	2022-11-27 19:07:11.414485	20	233545977791	27745949	f	2JV83B9VEK
8	TouchBase0.1	Nk	Regular	2022-11-27 19:18:15.679441	20	233545977791	27745951	f	14
9	TouchBase0.1	Nk	Regular	2022-11-27 19:20:04.4028	20	233545977791	27745953	f	15
10	TouchBase0.1	Nana Kweku	Regular	2022-11-27 19:22:27.209039	20	233545977791	27745954	f	16
11	TouchBase0.1	Ona	Regular	2022-11-27 19:25:26.250015	20	233570136459	27745955	f	17
12	TouchBase0.1	June	Regular	2022-11-27 19:49:33.6715	20	233202311542	27745963	f	18
13	TouchBase0.1	June	Regular	2022-11-27 20:04:26.917168	20	233202311542	27745969	f	19
14	TouchBase0.1	Nana Kweku 1	Regular	2022-11-28 19:25:22.751127	20	233545977791	27747265	f	21
15	TouchBase0.1	June	Regular	2022-11-28 19:53:58.204724	20	233202311542	27747287	f	22
16	TouchBase0.1	Ona	Regular	2022-11-28 19:56:58.170247	20	233570136459	27747293	f	23
17	TouchBase0.1	Graham	Regular	2022-11-28 19:58:18.665176	20	233551333676	27747296	f	24
18	TouchBase0.1	Graham	Regular	2022-11-28 20:00:40.387348	20	233551333676	27747299	f	25
19	TouchBase0.1	Maame	Regular	2022-11-28 21:54:14.122085	20	233207958775	\N	f	\N
20	TouchBase0.1	Kweku	Regular	2022-11-28 22:56:57.118719	20	233545977791	27747346	f	30
21	TouchBase0.1	life	Regular	2022-11-28 22:57:24.259884	20	233205197215	\N	f	\N
22	TouchBase0.1	Joseph	Regular	2022-11-29 07:43:35.867801	20	233506765860	27747366	f	31
23	TouchBase0.1	WO MAAME	Regular	2022-11-29 18:54:43.261131	0.2	233504739879	27748190	f	34
24	TouchBase0.1	MICHELLE, NANA'S LOVER	Regular	2022-11-29 19:11:48.647094	0.2	233504739879	27748192	f	35
25	TouchBase0.1	June	Regular	2022-11-29 19:13:35.629963	0.2	233202311542	\N	f	\N
26	TouchBase0.1	Keren 	Regular	2022-11-29 19:29:11.424182	0.2	233264167630	27748200	f	37
27	TouchBase0.1	Nana Kweku test	Regular	2022-11-29 19:31:29.128689	0.2	233264167630	27748202	f	38
28	TouchBase0.1	Nana Kweku test	Regular	2022-11-29 19:34:04.29839	0.2	233264167630	27748207	f	39
29	TouchBase0.1	Ona	Regular	2022-11-29 19:39:13.753729	0.2	233570136459	27748217	f	41
30	TouchBase0.1	JGJM	Regular	2022-11-29 19:46:06.943124	0.2	233504739879	27748225	f	42
31	TouchBase0.1	law	Regular	2022-11-29 19:57:35.059379	0.2	233502960444	\N	f	\N
32	TouchBase0.1	law§test	Regular	2022-11-29 20:01:06.55014	0.2	233502960444	\N	f	\N
33	01	server	Regular	2022-11-29 20:40:27.129304	0.20	233504739879	\N	f	\N
34	01	server	Regular	2022-11-29 20:44:31.800942	0.20	233504739879	\N	f	\N
35	01	server	Regular	2022-11-29 20:48:08.415579	0.20	233545977791	\N	f	\N
36	TouchBase0.1	666	Regular	2022-11-29 21:08:57.870642	0.2	233504739879	\N	f	\N
37	01	server	Regular	2022-11-29 21:11:59.750653	0.20	233545977791	\N	f	\N
38	TouchBase0.1	Kweku	Regular	2022-11-29 21:13:14.916971	0.2	233545977791	27748259	f	48
39	01	server	Regular	2022-11-29 21:16:49.600685	0.20	233545977791	27748260	f	get_random_string[10]
40	01	server	Regular	2022-11-29 21:17:23.632171	0.20	233504739879	\N	f	\N
41	01	server	Regular	2022-11-29 21:26:03.816662	0.20	233504739879	27748263	f	get_random_string[10]
42	TouchBase0.1	Airtel test	Regular	2022-11-30 07:24:20.371547	0.2	233264167630	\N	f	\N
43	TouchBase0.1	Airtel test	Regular	2022-11-30 07:25:32.159723	0.2	233264167630	\N	f	\N
\.


--
-- Data for Name: transactions; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.transactions (id, candidate, "candidateName", award, date_created, amount, account, ref, paid) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public."user" (id, username, phone, password) FROM stdin;
\.


--
-- Data for Name: ussd_sessions; Type: TABLE DATA; Schema: public; Owner: wyecuxdxvijnzx
--

COPY public.ussd_sessions (id, "sessionId", event) FROM stdin;
1	16695638431566855	127
2	16695662062462188	127
3	16695662861524502	127
4	16695672142497302	127
5	16695672591545133	127
6	16695675142418209	127
7	16695754692444018	01
8	16695756981548997	127
9	16695758842456285	127
10	16695760132460063	127
11	16695761552464222	127
12	16695766141561272	127
13	16695766421751943	127
14	16695766761562001	127
15	16695767911759327	127
16	16695769232486219	127
17	3000000014905521	01
18	847811226	01
19	847849313	01
20	16696197731583898	01
21	16696634962456566	127
22	5029302406	01
23	3000000015576833	01
24	16696654752464804	127
25	16696655572468673	127
26	850091652	127
27	16696757582453959	127
28	5029663744	127
29	850155173	127
30	16696762001577480	127
31	850423038	127
32	851555430	127
33	851709365	127
34	851721172	127
35	5031258961	127
36	851768974	01
37	2000000000263088	127
38	3000000016233293	127
39	2000000000268907	127
40	2000000000273250	01
41	2000000000275762	01
42	851858797	127
43	5031401260	127
44	5031418388	127
45	16697558871760011	127
46	16697559402452599	127
47	852164235	127
48	16697563781780296	127
49	1000004306115050	127
50	2000000000573804	127
51	5033771612	127
52	16698858621583343	127
53	2000000001365058	01
54	16698881451550765	127
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.categories_id_seq', 1, false);


--
-- Name: customer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.customer_id_seq', 1, false);


--
-- Name: event_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.event_id_seq', 1, true);


--
-- Name: item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.item_id_seq', 1, false);


--
-- Name: order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.order_id_seq', 1, false);


--
-- Name: poll_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.poll_id_seq', 1, false);


--
-- Name: ticket_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.ticket_id_seq', 54, true);


--
-- Name: ticket_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.ticket_transaction_id_seq', 43, true);


--
-- Name: transactions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.transactions_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.user_id_seq', 1, false);


--
-- Name: ussd_sessions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: wyecuxdxvijnzx
--

SELECT pg_catalog.setval('public.ussd_sessions_id_seq', 54, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: customer customer_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.customer
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);


--
-- Name: event event_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.event
    ADD CONSTRAINT event_pkey PRIMARY KEY (id);


--
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (id);


--
-- Name: order order_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public."order"
    ADD CONSTRAINT order_pkey PRIMARY KEY (id);


--
-- Name: poll poll_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.poll
    ADD CONSTRAINT poll_pkey PRIMARY KEY (id);


--
-- Name: ticket ticket_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ticket
    ADD CONSTRAINT ticket_pkey PRIMARY KEY (id);


--
-- Name: ticket_transaction ticket_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ticket_transaction
    ADD CONSTRAINT ticket_transaction_pkey PRIMARY KEY (id);


--
-- Name: transactions transactions_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.transactions
    ADD CONSTRAINT transactions_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: ussd_sessions ussd_sessions_pkey; Type: CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.ussd_sessions
    ADD CONSTRAINT ussd_sessions_pkey PRIMARY KEY (id);


--
-- Name: item item_vendor_fkey; Type: FK CONSTRAINT; Schema: public; Owner: wyecuxdxvijnzx
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_vendor_fkey FOREIGN KEY (vendor) REFERENCES public."user"(id) ON DELETE CASCADE;


--
-- Name: SCHEMA heroku_ext; Type: ACL; Schema: -; Owner: u5i4rotrbtfceq
--

GRANT USAGE ON SCHEMA heroku_ext TO wyecuxdxvijnzx;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: wyecuxdxvijnzx
--

REVOKE ALL ON SCHEMA public FROM postgres;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO wyecuxdxvijnzx;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: LANGUAGE plpgsql; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON LANGUAGE plpgsql TO wyecuxdxvijnzx;


--
-- PostgreSQL database dump complete
--

