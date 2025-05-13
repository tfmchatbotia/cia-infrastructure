--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Debian 16.8-1.pgdg120+1)
-- Dumped by pg_dump version 17.0

-- Started on 2025-04-18 17:06:50

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

DO $$ 
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_namespace WHERE nspname = 'public') THEN
        CREATE SCHEMA public;
    END IF;
END $$;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 16392)
-- Name: agency; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.agency (
    agency_id character varying NOT NULL,
    agency_name character varying,
    agency_url character varying,
    agency_timezone character varying NOT NULL,
    agency_lang character varying,
    agency_phone character varying,
    agency_fare_url character varying
);


ALTER TABLE public.agency OWNER TO admin;

--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_id; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_id IS 'Clave de la Agencia';


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_url; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_url IS 'Url de la Entidad';


--
-- TOC entry 3448 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_timezone; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_timezone IS 'Necesario para tener las referencias de las aperturas y cierres';


--
-- TOC entry 3449 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_lang; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_lang IS 'No es necesario';


--
-- TOC entry 3450 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_phone; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_phone IS 'Telefono de la agencia No es necesario';


--
-- TOC entry 3451 (class 0 OID 0)
-- Dependencies: 215
-- Name: COLUMN agency.agency_fare_url; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.agency.agency_fare_url IS 'Url de la agencia No es necesario';


--
-- TOC entry 216 (class 1259 OID 16399)
-- Name: calendar; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.calendar (
    service_id character varying NOT NULL,
    monday boolean[] NOT NULL,
    tuesday boolean[] NOT NULL,
    wednesday boolean[] NOT NULL,
    thursday boolean[] NOT NULL,
    friday boolean[] NOT NULL,
    saturday boolean[] NOT NULL,
    sunday boolean[] NOT NULL,
    start_date date[] NOT NULL,
    end_date date[] NOT NULL
);


ALTER TABLE public.calendar OWNER TO admin;

--
-- TOC entry 3452 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.monday; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.monday IS 'Indica si esta operativo para ese día';


--
-- TOC entry 3453 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.tuesday; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.tuesday IS 'Indica si esta operativo para ese día';


--
-- TOC entry 3454 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.wednesday; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.wednesday IS 'Indica si esta operativo para ese día';


--
-- TOC entry 3455 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.thursday; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.thursday IS 'Indica si esta operativo para ese día';


--
-- TOC entry 3456 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.friday; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.friday IS 'Indica si esta operativo para ese día';


--
-- TOC entry 3457 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.start_date; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.start_date IS 'Fecha de Inicio de la incidencia';


--
-- TOC entry 3458 (class 0 OID 0)
-- Dependencies: 216
-- Name: COLUMN calendar.end_date; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar.end_date IS 'Fecha fin de la incidencia';


--
-- TOC entry 217 (class 1259 OID 16406)
-- Name: calendar_date; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.calendar_date (
    service_id character varying NOT NULL,
    date date[] NOT NULL,
    exception_type "char"[]
);


ALTER TABLE public.calendar_date OWNER TO admin;

--
-- TOC entry 3459 (class 0 OID 0)
-- Dependencies: 217
-- Name: COLUMN calendar_date.date; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar_date.date IS 'Fecha incidencia';


--
-- TOC entry 3460 (class 0 OID 0)
-- Dependencies: 217
-- Name: COLUMN calendar_date.exception_type; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN public.calendar_date.exception_type IS 'Tipo de Incidencia';


--
-- TOC entry 218 (class 1259 OID 16413)
-- Name: fare_attributes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.fare_attributes (
    fare_id character varying NOT NULL,
    price real[],
    currency_type character varying NOT NULL,
    payment_method character varying,
    transfers character varying,
    transfer_duration character varying
);


ALTER TABLE public.fare_attributes OWNER TO admin;

--
-- TOC entry 219 (class 1259 OID 16420)
-- Name: fase_rules; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.fase_rules (
    fare_id character varying NOT NULL,
    route_id character varying,
    origin_id character varying,
    destination_id character varying,
    contains_id character varying
);


ALTER TABLE public.fase_rules OWNER TO admin;

--
-- TOC entry 220 (class 1259 OID 16427)
-- Name: feed_info; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.feed_info (
    feed_publisher_name character varying NOT NULL,
    feed_publisher_url character varying NOT NULL,
    feed_lang character varying NOT NULL,
    feed_start_date date,
    feed_end_date date,
    feed_version character varying
);


ALTER TABLE public.feed_info OWNER TO admin;

--
-- TOC entry 221 (class 1259 OID 16432)
-- Name: frequencies; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.frequencies (
    trip_id character varying NOT NULL,
    start_time time without time zone NOT NULL,
    end_time timestamp without time zone NOT NULL,
    headway_secs character varying,
    exact_times character varying
);


ALTER TABLE public.frequencies OWNER TO admin;

--
-- TOC entry 222 (class 1259 OID 16439)
-- Name: m4_accesos; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.m4_accesos (
    objectid information_schema.cardinal_number[],
    idacceso character varying NOT NULL,
    fechaactual date,
    modo character varying,
    codigoestacion character varying,
    codigoaccesoctm character varying,
    codigoaccesoempresa character varying,
    denominacion character varying,
    observaciones character varying,
    nivel character varying,
    codigovestibuloctm character varying,
    numerovestibulo character varying,
    numeroaccesodentrovestibulo character varying,
    indicadorpertenenciaempresa character varying,
    codigoprovincia character varying,
    codigomunicipio character varying,
    codigovia character varying,
    tipovia character varying,
    particula character varying,
    nombrevia character varying,
    tiponumero character varying,
    numeroportal character varying,
    calificadorportal character varying,
    codigopostal character varying,
    situacionrespectootrascalles character varying,
    horaapertura time without time zone,
    horacierre time without time zone,
    accesominusvalidos character varying,
    fechaalta date,
    fechainicio date,
    fechafin date,
    distanciaaccesovestibulo real[],
    x double precision[],
    y double precision,
    idfestacion character varying
);


ALTER TABLE public.m4_accesos OWNER TO admin;

--
-- TOC entry 223 (class 1259 OID 16446)
-- Name: m4_estaciones; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.m4_estaciones (
    objectid information_schema.cardinal_number[] NOT NULL,
    idestacion character varying,
    fechaactual date,
    modo character varying,
    codigoestacion character varying,
    denominacion character varying,
    observaciones character varying,
    situacion character varying,
    codigoctmestacionredmetro character varying,
    codigoempresa character varying,
    denominacionabreviada character varying,
    modointercambiador character varying,
    codigointercambiador character varying,
    tipo character varying,
    codigoprovincia character varying,
    codigomunicipio character varying,
    codigoentidad character varying,
    codigonucleo character varying,
    codigovia character varying,
    tipovia character varying,
    particula character varying,
    nombrevia character varying,
    tiponumero character varying,
    numeroportal character varying,
    calificadorportal character varying,
    carretera character varying,
    codigopostal character varying,
    distrito character varying,
    seccioncensal character varying,
    barrio character varying,
    tesela character varying,
    sectorurbano character varying,
    sector character varying,
    corredor character varying,
    coronatarifaria character varying,
    corona123 character varying,
    zonatransporte character varying,
    encuestadomiciliaria character varying,
    encuestaaforos character varying,
    hoja25000 character varying,
    acondicionamientoviajeros character varying,
    acondicionamientovehiculos character varying,
    fechaalta date,
    fechainicio date,
    fechafin character varying,
    x double precision,
    y double precision,
    gradoaccesibilidad character varying,
    situacioncalle character varying,
    denominacion_sae character varying,
    interurbanos_codigoemt_crtm character varying,
    lineas character varying
);


ALTER TABLE public.m4_estaciones OWNER TO admin;

--
-- TOC entry 224 (class 1259 OID 16453)
-- Name: m4_tramos; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.m4_tramos (
    objectid information_schema.cardinal_number[] NOT NULL,
    idtramo character varying,
    fechaactual date,
    modo character(1),
    codigoitinerario character varying,
    codigogestionlinea character varying,
    numerolineausuario character varying,
    sentido character varying,
    tipoitinerario character varying,
    codigoestacion character varying,
    codigoposte character varying,
    codigoanden character varying,
    numeroorden character varying,
    identificadortipoparada character varying,
    tipoparada character varying,
    denominacion character varying,
    codigoprovincia character varying,
    codigomunicipio character varying,
    municipio character varying,
    coronatarifaria character varying,
    direccion character varying,
    fechaalta date,
    fechainicio date NOT NULL,
    fechafin date,
    longitudtramoanterior real,
    velocidadtramoanterior real,
    modolinea character varying,
    modointercambiador character varying,
    codigointercambiador character varying,
    codprov_linea character varying,
    codmun_linea character varying,
    idftramo character varying,
    codigoobservacion character varying,
    codigosublinea character varying,
    denominacion_sae character varying,
    idflinea character varying,
    shape__length character varying
);


ALTER TABLE public.m4_tramos OWNER TO admin;

--
-- TOC entry 225 (class 1259 OID 16460)
-- Name: route; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.route (
    route_id character varying NOT NULL,
    agency_id character varying,
    route_short_name character varying,
    route_long_name character varying,
    route_desc character varying,
    route_type character varying,
    route_url character varying,
    route_color character varying,
    route_text_color character varying
);


ALTER TABLE public.route OWNER TO admin;

--
-- TOC entry 226 (class 1259 OID 16473)
-- Name: shapes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.shapes (
    shape_id character varying,
    shape_pt_lat double precision,
    shape_pt_lon double precision,
    shape_pt_sequence character varying,
    shape_dist_traveled character varying
);


ALTER TABLE public.shapes OWNER TO admin;

--
-- TOC entry 228 (class 1259 OID 16481)
-- Name: stop; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.stop (
    stop_id character varying NOT NULL,
    stop_code character varying,
    stop_name character varying,
    stop_desc character varying,
    stop_lat double precision[],
    stop_lon double precision[],
    zone_id character(1),
    stop_url character varying,
    location_type character varying,
    parent_station character varying,
    stop_timezone character varying,
    wheelchair_boarding character varying
);


ALTER TABLE public.stop OWNER TO admin;

--
-- TOC entry 227 (class 1259 OID 16478)
-- Name: stop_times; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.stop_times (
);


ALTER TABLE public.stop_times OWNER TO admin;

--
-- TOC entry 229 (class 1259 OID 16493)
-- Name: trip; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.trip (
    route_id character varying,
    service_id character varying,
    trip_id character varying,
    trip_headsign character varying,
    trip_short_name character varying,
    direction_id character varying,
    block_id character varying,
    shape_id character varying,
    wheelchair_accessible character varying
);


ALTER TABLE public.trip OWNER TO admin;

--
-- TOC entry 3425 (class 0 OID 16392)
-- Dependencies: 215
-- Data for Name: agency; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.agency (agency_id, agency_name, agency_url, agency_timezone, agency_lang, agency_phone, agency_fare_url) FROM stdin;
\.


--
-- TOC entry 3426 (class 0 OID 16399)
-- Dependencies: 216
-- Data for Name: calendar; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.calendar (service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date) FROM stdin;
\.


--
-- TOC entry 3427 (class 0 OID 16406)
-- Dependencies: 217
-- Data for Name: calendar_date; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.calendar_date (service_id, date, exception_type) FROM stdin;
\.


--
-- TOC entry 3428 (class 0 OID 16413)
-- Dependencies: 218
-- Data for Name: fare_attributes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.fare_attributes (fare_id, price, currency_type, payment_method, transfers, transfer_duration) FROM stdin;
\.


--
-- TOC entry 3429 (class 0 OID 16420)
-- Dependencies: 219
-- Data for Name: fase_rules; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.fase_rules (fare_id, route_id, origin_id, destination_id, contains_id) FROM stdin;
\.


--
-- TOC entry 3430 (class 0 OID 16427)
-- Dependencies: 220
-- Data for Name: feed_info; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.feed_info (feed_publisher_name, feed_publisher_url, feed_lang, feed_start_date, feed_end_date, feed_version) FROM stdin;
\.


--
-- TOC entry 3431 (class 0 OID 16432)
-- Dependencies: 221
-- Data for Name: frequencies; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.frequencies (trip_id, start_time, end_time, headway_secs, exact_times) FROM stdin;
\.


--
-- TOC entry 3432 (class 0 OID 16439)
-- Dependencies: 222
-- Data for Name: m4_accesos; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.m4_accesos (objectid, idacceso, fechaactual, modo, codigoestacion, codigoaccesoctm, codigoaccesoempresa, denominacion, observaciones, nivel, codigovestibuloctm, numerovestibulo, numeroaccesodentrovestibulo, indicadorpertenenciaempresa, codigoprovincia, codigomunicipio, codigovia, tipovia, particula, nombrevia, tiponumero, numeroportal, calificadorportal, codigopostal, situacionrespectootrascalles, horaapertura, horacierre, accesominusvalidos, fechaalta, fechainicio, fechafin, distanciaaccesovestibulo, x, y, idfestacion) FROM stdin;
\.


--
-- TOC entry 3433 (class 0 OID 16446)
-- Dependencies: 223
-- Data for Name: m4_estaciones; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.m4_estaciones (objectid, idestacion, fechaactual, modo, codigoestacion, denominacion, observaciones, situacion, codigoctmestacionredmetro, codigoempresa, denominacionabreviada, modointercambiador, codigointercambiador, tipo, codigoprovincia, codigomunicipio, codigoentidad, codigonucleo, codigovia, tipovia, particula, nombrevia, tiponumero, numeroportal, calificadorportal, carretera, codigopostal, distrito, seccioncensal, barrio, tesela, sectorurbano, sector, corredor, coronatarifaria, corona123, zonatransporte, encuestadomiciliaria, encuestaaforos, hoja25000, acondicionamientoviajeros, acondicionamientovehiculos, fechaalta, fechainicio, fechafin, x, y, gradoaccesibilidad, situacioncalle, denominacion_sae, interurbanos_codigoemt_crtm, lineas) FROM stdin;
\.


--
-- TOC entry 3434 (class 0 OID 16453)
-- Dependencies: 224
-- Data for Name: m4_tramos; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.m4_tramos (objectid, idtramo, fechaactual, modo, codigoitinerario, codigogestionlinea, numerolineausuario, sentido, tipoitinerario, codigoestacion, codigoposte, codigoanden, numeroorden, identificadortipoparada, tipoparada, denominacion, codigoprovincia, codigomunicipio, municipio, coronatarifaria, direccion, fechaalta, fechainicio, fechafin, longitudtramoanterior, velocidadtramoanterior, modolinea, modointercambiador, codigointercambiador, codprov_linea, codmun_linea, idftramo, codigoobservacion, codigosublinea, denominacion_sae, idflinea, shape__length) FROM stdin;
\.


--
-- TOC entry 3435 (class 0 OID 16460)
-- Dependencies: 225
-- Data for Name: route; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.route (route_id, agency_id, route_short_name, route_long_name, route_desc, route_type, route_url, route_color, route_text_color) FROM stdin;
\.


--
-- TOC entry 3436 (class 0 OID 16473)
-- Dependencies: 226
-- Data for Name: shapes; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.shapes (shape_id, shape_pt_lat, shape_pt_lon, shape_pt_sequence, shape_dist_traveled) FROM stdin;
\.


--
-- TOC entry 3438 (class 0 OID 16481)
-- Dependencies: 228
-- Data for Name: stop; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.stop (stop_id, stop_code, stop_name, stop_desc, stop_lat, stop_lon, zone_id, stop_url, location_type, parent_station, stop_timezone, wheelchair_boarding) FROM stdin;
\.


--
-- TOC entry 3437 (class 0 OID 16478)
-- Dependencies: 227
-- Data for Name: stop_times; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.stop_times  FROM stdin;
\.


--
-- TOC entry 3439 (class 0 OID 16493)
-- Dependencies: 229
-- Data for Name: trip; Type: TABLE DATA; Schema: public; Owner: admin
--

COPY public.trip (route_id, service_id, trip_id, trip_headsign, trip_short_name, direction_id, block_id, shape_id, wheelchair_accessible) FROM stdin;
\.


--
-- TOC entry 3259 (class 2606 OID 16398)
-- Name: agency agency_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.agency
    ADD CONSTRAINT agency_pk PRIMARY KEY (agency_id);


--
-- TOC entry 3263 (class 2606 OID 16412)
-- Name: calendar_date calendar_date_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.calendar_date
    ADD CONSTRAINT calendar_date_pk PRIMARY KEY (service_id);


--
-- TOC entry 3261 (class 2606 OID 16405)
-- Name: calendar calendar_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.calendar
    ADD CONSTRAINT calendar_pk PRIMARY KEY (service_id);


--
-- TOC entry 3265 (class 2606 OID 16419)
-- Name: fare_attributes fare_attributes_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.fare_attributes
    ADD CONSTRAINT fare_attributes_pk PRIMARY KEY (fare_id);


--
-- TOC entry 3267 (class 2606 OID 16426)
-- Name: fase_rules fase_rules_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.fase_rules
    ADD CONSTRAINT fase_rules_pk PRIMARY KEY (fare_id);


--
-- TOC entry 3269 (class 2606 OID 16438)
-- Name: frequencies frequencies_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.frequencies
    ADD CONSTRAINT frequencies_pk PRIMARY KEY (trip_id);


--
-- TOC entry 3271 (class 2606 OID 16445)
-- Name: m4_accesos m4_accesos_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.m4_accesos
    ADD CONSTRAINT m4_accesos_pk PRIMARY KEY (idacceso);


--
-- TOC entry 3273 (class 2606 OID 16452)
-- Name: m4_estaciones m4_estaciones_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.m4_estaciones
    ADD CONSTRAINT m4_estaciones_pk PRIMARY KEY (objectid);


--
-- TOC entry 3275 (class 2606 OID 16459)
-- Name: m4_tramos m4_tramos_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.m4_tramos
    ADD CONSTRAINT m4_tramos_pk PRIMARY KEY (objectid);


--
-- TOC entry 3277 (class 2606 OID 16467)
-- Name: route route_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.route
    ADD CONSTRAINT route_pk PRIMARY KEY (route_id);


--
-- TOC entry 3279 (class 2606 OID 16487)
-- Name: stop stop_pk; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.stop
    ADD CONSTRAINT stop_pk PRIMARY KEY (stop_id);


--
-- TOC entry 3280 (class 2606 OID 16468)
-- Name: route route_agency_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.route
    ADD CONSTRAINT route_agency_fk FOREIGN KEY (agency_id) REFERENCES public.agency(agency_id) ON UPDATE CASCADE;


--
-- TOC entry 3281 (class 2606 OID 16488)
-- Name: stop stop_stop_fk; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.stop
    ADD CONSTRAINT stop_stop_fk FOREIGN KEY (stop_id) REFERENCES public.stop(stop_id) ON UPDATE CASCADE;


-- Completed on 2025-04-18 17:06:50

--
-- PostgreSQL database dump complete
--

