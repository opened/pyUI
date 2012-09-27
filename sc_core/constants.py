﻿"""
-----------------------------------------------------------------------------
This source file is part of OSTIS (Open Semantic Technology for Intelligent Systems)
For the latest info, see http://www.ostis.net

Copyright (c) 2010 OSTIS

OSTIS is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OSTIS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with OSTIS.  If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------------------
"""


'''
Created on Apr 18, 2009

@author: Kolb Dmitry
'''
import pm

'''
 Session constants
'''

system_session = pm.cvar.system_session 

'''
Constraints constants
'''
#begin
CONSTR_ALL_INPUT = pm.cvar.__constr_all_input
CONSTR_ALL_OUTPUT = pm.cvar.__constr_all_output
CONSTR_ARC_TYPE_INPUT = pm.cvar.__constr_arc_type_input
CONSTR_ARC_TYPE_OUTPUT = pm.cvar.__constr_arc_type_output
CONSTR_3_f_a_a = pm.cvar.__constr_3faa
CONSTR_3_f_a_f = pm.cvar.__constr_3faf
CONSTR_3_a_a_f = pm.cvar.__constr_3aaf
CONSTR_3_d_f_d = pm.cvar.__constr_3dfd
CONSTR_5_f_a_a_a_a = pm.cvar.__constr_5faaaa
CONSTR_5_f_a_a_a_f = pm.cvar.__constr_5faaaf
CONSTR_5_f_a_f_a_a = pm.cvar.__constr_5fafaa
CONSTR_5_f_a_f_a_f = pm.cvar.__constr_5fafaf
CONSTR_5_a_a_a_a_f = pm.cvar.__constr_5aaaaf
CONSTR_5_a_a_f_a_a = pm.cvar.__constr_5aafaa
CONSTR_5_a_a_f_a_f = pm.cvar.__constr_5aafaf
CONSTR_ORD_BIN_CONN1 = pm.cvar.__constr_ord_bin_conn1
CONSTR_ORD_BIN_CONN1_DEF = pm.cvar.__constr_ord_bin_conn1_def
CONSTR_ORD_BIN_CONN2 = pm.cvar.__constr_ord_bin_conn2
CONSTR_3l2_f_a_a_a_f = pm.cvar.__constr_3l2_faaaf
CONSTR_5_3_a_a_a_a_f_a_f = pm.cvar.__constr_5_3_aaaafaf
CONSTR_in_set = pm.cvar.__constr_in_set
CONSTR_sely3_p1 = pm.cvar.__constr_sely3_p1
CONSTR_sely3_u1p2 = pm.cvar.__constr_sely3_u1p2
CONSTR_sely3_u1u2p3 = pm.cvar.__constr_sely3_u1u2p3
CONSTR_sely5_p1 = pm.cvar.__constr_sely5_p1
CONSTR_sely5_u1p2 = pm.cvar.__constr_sely5_u1p2
CONSTR_sely5_u1u2p3 = pm.cvar.__constr_sely5_u1u2p3
CONSTR_sely5_u1u2u3p4 = pm.cvar.__constr_sely5_u1u2u3p4
CONSTR_sely5_u1u2u3u4p5 = pm.cvar.__constr_sely5_u1u2u3u4p5
CONSTR_intersect2 = pm.cvar.__constr_intersect2
CONSTR_3l2_5faaaf = pm.cvar.__constr_3l2_5faaaf
CONSTR_bin_conn_unord1 = pm.cvar.__constr_bin_conn_unord1
CONSTR_4ln5_faaaaaffa = pm.cvar.__constr_4ln5_faaaaaffa
CONSTR_4l5_faaaaaffa = pm.cvar.__constr_4l5_faaaaaffa
CONSTR_ORD_BIN_CONN1A = pm.cvar.__constr_ord_bin_conn1a
CONSTR_ON_SEGMENT = pm.cvar.__constr_on_segment
#end            

'''
PM keynodes constants
'''            
#begin
SCP_PROCESS = pm.pm_keynodes_item(0)
SCP_OPERATOR = pm.pm_keynodes_item(1)
SCP_OPERATOR_TYPE = pm.pm_keynodes_item(2)
SCP_PROGRAM = pm.pm_keynodes_item(3)
INIT = pm.pm_keynodes_item(4)
INITWITHDATA = pm.pm_keynodes_item(5)
PREPARED_SCP_PROGRAM = pm.pm_keynodes_item(6)
CONST_SEGMENTS_ = pm.pm_keynodes_item(7)
DEFAULT_SEG_ = pm.pm_keynodes_item(8)
OPENED_SEGMENTS_ = pm.pm_keynodes_item(9)
QUEUE = pm.pm_keynodes_item(10)
QUEUE_HEAD_ = pm.pm_keynodes_item(11)
QUEUE_NEXT_ = pm.pm_keynodes_item(12)
QUEUE_PREV_ = pm.pm_keynodes_item(13)
QUEUE_VALUE_ = pm.pm_keynodes_item(14)
QUEUE_NIL = pm.pm_keynodes_item(15)
CONST_ = pm.pm_keynodes_item(16)
VAR_ = pm.pm_keynodes_item(17)
METAVAR_ = pm.pm_keynodes_item(18)
POS_ = pm.pm_keynodes_item(19)
NEG_ = pm.pm_keynodes_item(20)
FUZ_ = pm.pm_keynodes_item(21)
ARC_ = pm.pm_keynodes_item(22)
NODE_ = pm.pm_keynodes_item(23)
UNDF_ = pm.pm_keynodes_item(24)
PERMANENT_ = pm.pm_keynodes_item(25)
TEMPORARY_ = pm.pm_keynodes_item(26)
ACTUAL_ = pm.pm_keynodes_item(27)
PHANTOM_ = pm.pm_keynodes_item(28)
TYPEATTRS = pm.pm_keynodes_item(29)
PROCESS_STATE_THEN = pm.pm_keynodes_item(30)
PROCESS_STATE_ELSE = pm.pm_keynodes_item(31)
PROCESS_STATE_REPEAT = pm.pm_keynodes_item(32)
PROCESS_STATE_SLEEP = pm.pm_keynodes_item(33)
PROCESS_STATE_RUN = pm.pm_keynodes_item(34)
PROCESS_STATE_DEAD = pm.pm_keynodes_item(35)
PROCESS_STATE_ERROR = pm.pm_keynodes_item(36)
PROCESS_ = pm.pm_keynodes_item(37)
MSG_DSTMAJ_ = pm.pm_keynodes_item(38)
MSG_DSTMIN_ = pm.pm_keynodes_item(39)
MSG_SRCMAJ_ = pm.pm_keynodes_item(40)
MSG_SRCMIN_ = pm.pm_keynodes_item(41)
MSG_DATA_ = pm.pm_keynodes_item(42)
MAILBOX_HOOK_ = pm.pm_keynodes_item(43)
MAILBOX = pm.pm_keynodes_item(44)
MAILBOX_ = pm.pm_keynodes_item(45)
MAIL_INCOMING_ = pm.pm_keynodes_item(46)
MAIL_OUTGOING_ = pm.pm_keynodes_item(47)
SYSTEM_MAILBOX = pm.pm_keynodes_item(48)
MAIL_DATA_ = pm.pm_keynodes_item(49)
THIS_PM_MAJOR = pm.pm_keynodes_item(50)
MODULE = pm.pm_keynodes_item(51)
CONNECTED_MODULE = pm.pm_keynodes_item(52)
MODULE_ = pm.pm_keynodes_item(53)
PM_MODULE = pm.pm_keynodes_item(54)
TM_MODULE = pm.pm_keynodes_item(55)
CURRENT_MODULE = pm.pm_keynodes_item(56)
OWNER_ = pm.pm_keynodes_item(57)
USER = pm.pm_keynodes_item(58)
COMMAND = pm.pm_keynodes_item(59)
ASSIGN_ = pm.pm_keynodes_item(60)
FIXED_ = pm.pm_keynodes_item(61)
F_ = pm.pm_keynodes_item(62)
ACTIVE_ = pm.pm_keynodes_item(63)
AUTOSEGMENT_ = pm.pm_keynodes_item(64)
SONS_GARBAGE_ = pm.pm_keynodes_item(65)
PROGRAM_ = pm.pm_keynodes_item(66)
THEN_ = pm.pm_keynodes_item(67)
ELSE_ = pm.pm_keynodes_item(68)
GOTO_ = pm.pm_keynodes_item(69)
ERROR_ = pm.pm_keynodes_item(70)
INIT_ = pm.pm_keynodes_item(71)
VAR_VALUE_ = pm.pm_keynodes_item(72)
REAL_RETURN_VALUE = pm.pm_keynodes_item(73)
LIST = pm.pm_keynodes_item(74)
LIST_NEXT_ = pm.pm_keynodes_item(75)
LIST_VALUE_ = pm.pm_keynodes_item(76)
BREAKPOINT = pm.pm_keynodes_item(77)
PTRACE_ = pm.pm_keynodes_item(78)
PTRACER = pm.pm_keynodes_item(79)
DEBUGGER = pm.pm_keynodes_item(80)
BREAKPOINT_ = pm.pm_keynodes_item(81)
TRACERS_ = pm.pm_keynodes_item(82)
BREAKPOINTS_ = pm.pm_keynodes_item(83)
DEBUG_COPIES_ = pm.pm_keynodes_item(84)
ORIGINALS_ = pm.pm_keynodes_item(85)
SEGMENT_ = pm.pm_keynodes_item(86)
SET_ = pm.pm_keynodes_item(87)
IDTF_ = pm.pm_keynodes_item(88)
CONTENT_ = pm.pm_keynodes_item(89)
CHANGESET = pm.pm_keynodes_item(90)
BEFORE_ = pm.pm_keynodes_item(91)
AFTER_ = pm.pm_keynodes_item(92)
EQUIVALENTS_ = pm.pm_keynodes_item(93)
MERGES_ = pm.pm_keynodes_item(94)
APPLY_DIFF = pm.pm_keynodes_item(95)
MESSAGEBOX = pm.pm_keynodes_item(96)
TYPE_ = pm.pm_keynodes_item(97)
SECONDARY_TEXT_ = pm.pm_keynodes_item(98)
PRIMARY_TEXT_ = pm.pm_keynodes_item(99)
UI_CONFIRM = pm.pm_keynodes_item(100)
UI_INFORMATION = pm.pm_keynodes_item(101)
UI_ERROR = pm.pm_keynodes_item(102)
UI_OK = pm.pm_keynodes_item(103)
UI_YES = pm.pm_keynodes_item(104)
UI_NO = pm.pm_keynodes_item(105)
EV_ALLOW = pm.pm_keynodes_item(106)
EV_DENY = pm.pm_keynodes_item(107)
SCHEDULING_CLASS = pm.pm_keynodes_item(108)
SCHED_CLASS_KERNEL = pm.pm_keynodes_item(109)
SCHED_CLASS_SYSTEM = pm.pm_keynodes_item(110)
SCHED_CLASS_NORMAL = pm.pm_keynodes_item(111)
SUBSCHED_KERNEL = pm.pm_keynodes_item(112)
SUBSCHED_SYSTEM = pm.pm_keynodes_item(113)
SUBSCHED_NORMAL = pm.pm_keynodes_item(114)
SLEEPING = pm.pm_keynodes_item(115)
MESSAGE = pm.pm_keynodes_item(116)
LAZY_DATA_MESSAGE = pm.pm_keynodes_item(117)
ARRIVED_MESSAGE = pm.pm_keynodes_item(118)
WAKEUP_HOOK = pm.pm_keynodes_item(119)
REMOVE_FROM_SHEET = pm.pm_keynodes_item(120)
FATHER_ = pm.pm_keynodes_item(121)
CHILD_DEATH_HOOK_ = pm.pm_keynodes_item(122)
IN_ = pm.pm_keynodes_item(123)
OUT_ = pm.pm_keynodes_item(124)
PRM_ = pm.pm_keynodes_item(125)
IM_PRM_ = pm.pm_keynodes_item(126)
WAITING_FOR_ = pm.pm_keynodes_item(127)
ALL_CHILDS = pm.pm_keynodes_item(128)
OUTPUT_PRM_BINDING_ = pm.pm_keynodes_item(129)
WAIT_GEN_OUTPUT_ARC = pm.pm_keynodes_item(130)
WAIT_GEN_INPUT_ARC = pm.pm_keynodes_item(131)
WAIT_INPUT_ARC = pm.pm_keynodes_item(132)
WAIT_OUTPUT_ARC = pm.pm_keynodes_item(133)
WAIT_ERASE_ELEMENT = pm.pm_keynodes_item(134)
WAIT_GEN_OUTPUT_ARC_PRE = pm.pm_keynodes_item(135)
WAIT_GEN_INPUT_ARC_PRE = pm.pm_keynodes_item(136)
WAIT_ERASE_ELEMENT_PRE = pm.pm_keynodes_item(137)
WAIT_RECIEVE_MESSAGE = pm.pm_keynodes_item(138)
SEND_ = pm.pm_keynodes_item(139)
SEND_NAMED_ = pm.pm_keynodes_item(140)
DEFAULT_SHELL = pm.pm_keynodes_item(141)
SHELL = pm.pm_keynodes_item(142)
SCO_CLASS = pm.pm_keynodes_item(143)
SCO_EXTEND_ = pm.pm_keynodes_item(144)
SCO_OBJECT = pm.pm_keynodes_item(145)
SCO_OBJECT_ = pm.pm_keynodes_item(146)
SCO_IMPLEMENTATION_ = pm.pm_keynodes_item(147)
SCO_PROGRAM_ = pm.pm_keynodes_item(148)
SCO_SIGNATURE = pm.pm_keynodes_item(149)
SCO_VARVALUE_ = pm.pm_keynodes_item(150)
SCO_PRM_ = pm.pm_keynodes_item(151)
SCO_PRM_NAME_ = pm.pm_keynodes_item(152)
SCO_FACTORY_HOOK = pm.pm_keynodes_item(153)
SCO_FACTORY_MAILBOX = pm.pm_keynodes_item(154)
SC_TRUE = pm.pm_keynodes_item(155)
SC_FALSE = pm.pm_keynodes_item(156)
REGISTERED_USER = pm.pm_keynodes_item(157)
FS_NAMES = pm.pm_keynodes_item(158)
FS_NAME_ = pm.pm_keynodes_item(159)
KN_FILE = pm.pm_keynodes_item(160)
KN_DIRECTORY = pm.pm_keynodes_item(161)
OPERATOR_FILE_ = pm.pm_keynodes_item(162)
OPERATOR_LINE_ = pm.pm_keynodes_item(163)
RELAYED_COMMAND = pm.pm_keynodes_item(164)
WAITING_COMMAND = pm.pm_keynodes_item(165)
SHELL_ = pm.pm_keynodes_item(166)
AGENT = pm.pm_keynodes_item(167)
AGN_COMMAND_ = pm.pm_keynodes_item(168)
AGN_MAILBOX_ = pm.pm_keynodes_item(169)
AGN_ACTIVE_ = pm.pm_keynodes_item(170)
AGN_DIRECTORY_ = pm.pm_keynodes_item(171)
HOME = pm.pm_keynodes_item(172)
AGN_INTERNAL = pm.pm_keynodes_item(173)
AGN_EXTERNAL = pm.pm_keynodes_item(174)
AC_RETURN_VALUE = pm.pm_keynodes_item(175)
AC_LOAD_GRAPH = pm.pm_keynodes_item(176)
AC_LOGIN = pm.pm_keynodes_item(177)
AC_SUBCRIBE = pm.pm_keynodes_item(178)
AC_SUBCRIBE_OK = pm.pm_keynodes_item(179)
AC_BUILD_PROGRAM = pm.pm_keynodes_item(180)
AC_RUN_PROGRAM = pm.pm_keynodes_item(181)
AGN_CONNECT_TM = pm.pm_keynodes_item(182)
AC_ERASE = pm.pm_keynodes_item(183)
AC_CHANGE = pm.pm_keynodes_item(184)
AC_CREATE_USER = pm.pm_keynodes_item(185)
AC_GET_ELEMENT_BY_IDTF = pm.pm_keynodes_item(186)
COMMAND_FAILED = pm.pm_keynodes_item(187)
PERSONAL_AGENT = pm.pm_keynodes_item(188)
PERSON_ = pm.pm_keynodes_item(189)
AGENT_ = pm.pm_keynodes_item(190)
INBOX_ = pm.pm_keynodes_item(191)
LOGIN_AGENT = pm.pm_keynodes_item(192)
STARTUP_PROGRAM_ = pm.pm_keynodes_item(193)
SHL_SHEETS = pm.pm_keynodes_item(194)
TML_SHEET = pm.pm_keynodes_item(195)
SHL_LOGIN_OK = pm.pm_keynodes_item(196)
SHL_LOGIN_FAILED = pm.pm_keynodes_item(197)
SHL_CAPTION_ = pm.pm_keynodes_item(198)
SHL_MENU = pm.pm_keynodes_item(199)
SHL_MF_STRING = pm.pm_keynodes_item(200)
SHL_MF_END = pm.pm_keynodes_item(201)
SHL_MF_POPUP = pm.pm_keynodes_item(202)
SHL_ACTIVE_SETTINGS = pm.pm_keynodes_item(203)
SHL_RESOURCE = pm.pm_keynodes_item(204)
SHL_ID_ = pm.pm_keynodes_item(205)
SHL_ITEM_ = pm.pm_keynodes_item(206)
SHL_SIZE_ = pm.pm_keynodes_item(207)
SHL_DLG_CONTROLS = pm.pm_keynodes_item(208)
SHL_DLG_PROPERTIES = pm.pm_keynodes_item(209)
SHL_DLG_BUTTON = pm.pm_keynodes_item(210)
SHL_DLG_STATIC = pm.pm_keynodes_item(211)
SHL_DLG_NAME = pm.pm_keynodes_item(212)
SHL_DIALOG_CREATE = pm.pm_keynodes_item(213)
SHL_DIALOG_DO = pm.pm_keynodes_item(214)
SHL_SHEET_CREATE = pm.pm_keynodes_item(215)
SHL_OPEN_SHEET = pm.pm_keynodes_item(216)
SHL_OUTPUT = pm.pm_keynodes_item(217)
SHL_OUTPUT_NEW_SHEET = pm.pm_keynodes_item(218)
SHL_MODULE_ = pm.pm_keynodes_item(219)
SHL_HAVE_INC_MSG = pm.pm_keynodes_item(220)
SHL_USER_ = pm.pm_keynodes_item(221)
SHL_SHEET_ = pm.pm_keynodes_item(222)
SHL_SCGSHEET = pm.pm_keynodes_item(223)
SHL_SCG3DSHEET = pm.pm_keynodes_item(224)
SHL_SCSOSHEET = pm.pm_keynodes_item(225)
SHL_SCSSHEET = pm.pm_keynodes_item(226)
SHL_SCHSHEET = pm.pm_keynodes_item(227)
SHL_ANIMATIONSHEET = pm.pm_keynodes_item(228)
SHL_TREESHEET = pm.pm_keynodes_item(229)
SHL_AGENTSHEET = pm.pm_keynodes_item(230)
SHL_GEOMETRYSHEET = pm.pm_keynodes_item(231)
SHL_NLSHEET = pm.pm_keynodes_item(232)
IM_LOGIN = pm.pm_keynodes_item(233)
IM_LOGOUT = pm.pm_keynodes_item(234)
IM_USR = pm.pm_keynodes_item(235)
IM_NAME_ = pm.pm_keynodes_item(236)
IM_IM_ = pm.pm_keynodes_item(237)
IM_IM = pm.pm_keynodes_item(238)
IM_CWS_ = pm.pm_keynodes_item(239)
IM_PM_ = pm.pm_keynodes_item(240)
IM_UI_EVENTS_ = pm.pm_keynodes_item(241)
IM_UI_EVENT = pm.pm_keynodes_item(242)
IM_UI_EVENT_ = pm.pm_keynodes_item(243)
IM_WINDOW_ = pm.pm_keynodes_item(244)
IM_MENU_ = pm.pm_keynodes_item(245)
IM_TOOLBAR_ = pm.pm_keynodes_item(246)
IM_IMAGE_ = pm.pm_keynodes_item(247)
IM_DIALOG_ = pm.pm_keynodes_item(248)
IM_PUSH_BUTTON_ = pm.pm_keynodes_item(249)
IM_CHECK_BUTTON_ = pm.pm_keynodes_item(250)
IM_RADIO_BUTTON_ = pm.pm_keynodes_item(251)
IM_GROUP_ = pm.pm_keynodes_item(252)
IM_STATIC_ = pm.pm_keynodes_item(253)
IM_EDITBOX_ = pm.pm_keynodes_item(254)
IM_UI_EVENTCLASS = pm.pm_keynodes_item(255)
IM_EVENTLISTENER_ = pm.pm_keynodes_item(256)
IM_SELECTED_ELEMENTS_ON_SHEET = pm.pm_keynodes_item(257)
IM_SELECTED_ELEMENT_LIST_ON_SHEET = pm.pm_keynodes_item(258)
IM_SINGLE_SELECTED_ELEMENT = pm.pm_keynodes_item(259)
IM_SEND_USER = pm.pm_keynodes_item(260)
IM_SHEET_CONTENT = pm.pm_keynodes_item(261)
IM_SHEET = pm.pm_keynodes_item(262)
IM_LISTENER_CLASS = pm.pm_keynodes_item(263)
IM_LISTENER_CLASS_ = pm.pm_keynodes_item(264)
IM_SCP_PROCESS_LISTENER = pm.pm_keynodes_item(265)
IM_SHEETTYPE = pm.pm_keynodes_item(266)
VK_CONTROL_ = pm.pm_keynodes_item(267)
IM_UI_SHEETEVTEMPLATE = pm.pm_keynodes_item(268)
IM_UI_TYPESHEETEVTEMPLATE = pm.pm_keynodes_item(269)
SHL_MAILBOX = pm.pm_keynodes_item(270)
REL = pm.pm_keynodes_item(271)
ATTR = pm.pm_keynodes_item(272)
CONN_BIN = pm.pm_keynodes_item(273)
SET = pm.pm_keynodes_item(274)
TUPLE = pm.pm_keynodes_item(275)
SUBJ = pm.pm_keynodes_item(276)
LOGIN_MAILBOX = pm.pm_keynodes_item(277)
MARKUP_ = pm.pm_keynodes_item(278)
ROOT_ = pm.pm_keynodes_item(279)
DEFAULT_ = pm.pm_keynodes_item(280)
STYLE_ = pm.pm_keynodes_item(281)
VK_SHIFT_ = pm.pm_keynodes_item(282)
SCON_SYNONYMY = pm.pm_keynodes_item(283)
SCON_MAIN_ = pm.pm_keynodes_item(284)
SCON_TITLE_ = pm.pm_keynodes_item(285)
SCON_DEF_ = pm.pm_keynodes_item(286)
SCON_NEARSEM = pm.pm_keynodes_item(287)
SCON_SETINCLUDE = pm.pm_keynodes_item(288)
SCON_SUB_ = pm.pm_keynodes_item(289)
SCON_OVER_ = pm.pm_keynodes_item(290)
SCON_EXAMPLE_ = pm.pm_keynodes_item(291)
SCON_SETPARTITION = pm.pm_keynodes_item(292)
SCON_WHOLE_ = pm.pm_keynodes_item(293)
SCON_PARTS_ = pm.pm_keynodes_item(294)
SCON_SETUNION = pm.pm_keynodes_item(295)
SCON_SETINTERSECTION = pm.pm_keynodes_item(296)
SCON_RESULT_ = pm.pm_keynodes_item(297)
SCON_SETS_ = pm.pm_keynodes_item(298)
SCON_EXISTSETINTERSECTION = pm.pm_keynodes_item(299)
SCON_EXISTSTRICTSETINTERSECTION = pm.pm_keynodes_item(300)
SCON_NOSETINTERSECTION = pm.pm_keynodes_item(301)
SCON_SETEQUAL = pm.pm_keynodes_item(302)
SCON_FCTRSET = pm.pm_keynodes_item(303)
SCON_SIGNCOMMENT = pm.pm_keynodes_item(304)
SCON_COMMENT_ = pm.pm_keynodes_item(305)
SCON_KEYSIGN = pm.pm_keynodes_item(306)
SCON_KEYSIGN_ = pm.pm_keynodes_item(307)
SCON_KEYSIGN2_ = pm.pm_keynodes_item(308)
SCON_KEYSIGN3_ = pm.pm_keynodes_item(309)
SCON_SIGNDEFINITION = pm.pm_keynodes_item(310)
SCON_SIGNCOMPARISION = pm.pm_keynodes_item(311)
SCON_SIGNDEFINITIONSC = pm.pm_keynodes_item(312)
SCON_IDTFCOMMENT = pm.pm_keynodes_item(313)
SCON_IDTF_ = pm.pm_keynodes_item(314)
SCON_ELEMIDTFCOMMENT = pm.pm_keynodes_item(315)
SCON_ELEM_ = pm.pm_keynodes_item(316)
SCON_RELSCHEME = pm.pm_keynodes_item(317)
SCON_ATTRIBUTE_ = pm.pm_keynodes_item(318)
SCON_RELATION_ = pm.pm_keynodes_item(319)
SCON_FIELDDEF = pm.pm_keynodes_item(320)
SCON_REL_ = pm.pm_keynodes_item(321)
SCON_FIELD_ = pm.pm_keynodes_item(322)
SCON_TITLEBIBLIOGRAPHIC_ = pm.pm_keynodes_item(323)
SCON_DOCUMENT_ = pm.pm_keynodes_item(324)
SCON_AUTHOR = pm.pm_keynodes_item(325)
SCON_AUTHOR_ = pm.pm_keynodes_item(326)
SCON_DOCINCLUDE_ = pm.pm_keynodes_item(327)
SCON_BASICDOCUMENTFRAGMENTATION = pm.pm_keynodes_item(328)
SCON_BASICSEQUENCE_ = pm.pm_keynodes_item(329)
SCON_DOCUMENTFRAGMENTSSET_ = pm.pm_keynodes_item(330)
SCON_ADDITIONALFRAGMENT_ = pm.pm_keynodes_item(331)
SCON_NEXT_ = pm.pm_keynodes_item(332)
SCON_DOCUMENTFRAGMENTATION_ = pm.pm_keynodes_item(333)
SCON_SEQUENCE_ = pm.pm_keynodes_item(334)
SCON_DOCSEMCOMMENT = pm.pm_keynodes_item(335)
SCON_DOCSYNTCOMMENT = pm.pm_keynodes_item(336)
SCON_DOCLOCCOMMENT = pm.pm_keynodes_item(337)
SCON_REFERENCE = pm.pm_keynodes_item(338)
SCON_FROM_ = pm.pm_keynodes_item(339)
SCON_TO_ = pm.pm_keynodes_item(340)
SCON_REFERENCELOC = pm.pm_keynodes_item(341)
SCON_REFERENCEBIBL = pm.pm_keynodes_item(342)
SCON_PAGES_ = pm.pm_keynodes_item(343)
SCON_SEMEQUAL = pm.pm_keynodes_item(344)
SCON_SCS_LANGUAGE = pm.pm_keynodes_item(345)
SCON_SCG_LANGUAGE = pm.pm_keynodes_item(346)
SCON_RUSSIANLANGUAGE = pm.pm_keynodes_item(347)
SCON_ENGLISHLANGUAGE = pm.pm_keynodes_item(348)
SCON_STATPROOF = pm.pm_keynodes_item(349)
SCON_STATEMENT_ = pm.pm_keynodes_item(350)
SCON_PROOF_ = pm.pm_keynodes_item(351)
SCON_CONSEQUENCE = pm.pm_keynodes_item(352)
SCON_CONSEQUENCE_ = pm.pm_keynodes_item(353)
SCON_PARTS = pm.pm_keynodes_item(354)
SCON_EBOOKS = pm.pm_keynodes_item(355)
SCON_CLASS_ = pm.pm_keynodes_item(356)
SCON_CLASSNOTIONS = pm.pm_keynodes_item(357)
SCON_NOTION_ = pm.pm_keynodes_item(358)
SCON_EBOOK = pm.pm_keynodes_item(359)
SCON_EBOOK_ = pm.pm_keynodes_item(360)
SCON_TERMS_ = pm.pm_keynodes_item(361)
SCON_TASKS_ = pm.pm_keynodes_item(362)
SCON_EXAMPLES = pm.pm_keynodes_item(363)
SCON_COMMENT = pm.pm_keynodes_item(364)
SCON_DEF = pm.pm_keynodes_item(365)
SCON_PICT = pm.pm_keynodes_item(366)
SCON_STAT = pm.pm_keynodes_item(367)
SCON_FACT = pm.pm_keynodes_item(368)
SCON_PROOF = pm.pm_keynodes_item(369)
SCON_BIBL = pm.pm_keynodes_item(370)
SCON_SECTION = pm.pm_keynodes_item(371)
SCON_SEB = pm.pm_keynodes_item(372)
SCON_CLASSIFY = pm.pm_keynodes_item(373)
SCON_ANNOTATION = pm.pm_keynodes_item(374)
ELEM_ = pm.pm_keynodes_item(375)
MIME_TYPE = pm.pm_keynodes_item(376)
MIME_ = pm.pm_keynodes_item(377)
STARTUP_ = pm.pm_keynodes_item(378)
SCHEDULER = pm.pm_keynodes_item(379)

N0_ = pm.pm_numattr_item(0)
N1_ = pm.pm_numattr_item(1)
N2_ = pm.pm_numattr_item(2)
N3_ = pm.pm_numattr_item(3)
N4_ = pm.pm_numattr_item(4)
N5_ = pm.pm_numattr_item(5)
N6_ = pm.pm_numattr_item(6)
N7_ = pm.pm_numattr_item(7)
N8_ = pm.pm_numattr_item(8)
N9_ = pm.pm_numattr_item(9)
N10_ = pm.pm_numattr_item(10)
N11_ = pm.pm_numattr_item(11)
N12_ = pm.pm_numattr_item(12)
N13_ = pm.pm_numattr_item(13)
N14_ = pm.pm_numattr_item(14)
N15_ = pm.pm_numattr_item(15)
N16_ = pm.pm_numattr_item(16)
N17_ = pm.pm_numattr_item(17)
N18_ = pm.pm_numattr_item(18)
N19_ = pm.pm_numattr_item(19)
N20_ = pm.pm_numattr_item(20)
N21_ = pm.pm_numattr_item(21)
N22_ = pm.pm_numattr_item(22)
N23_ = pm.pm_numattr_item(23)
N24_ = pm.pm_numattr_item(24)
N25_ = pm.pm_numattr_item(25)
N26_ = pm.pm_numattr_item(26)
N27_ = pm.pm_numattr_item(27)
N28_ = pm.pm_numattr_item(28)
N29_ = pm.pm_numattr_item(29)
N30_ = pm.pm_numattr_item(30)
N31_ = pm.pm_numattr_item(31)
N32_ = pm.pm_numattr_item(32)
N33_ = pm.pm_numattr_item(33)
N34_ = pm.pm_numattr_item(34)
N35_ = pm.pm_numattr_item(35)
N36_ = pm.pm_numattr_item(36)
N37_ = pm.pm_numattr_item(37)
N38_ = pm.pm_numattr_item(38)
N39_ = pm.pm_numattr_item(39)
N40_ = pm.pm_numattr_item(40)
N41_ = pm.pm_numattr_item(41)
N42_ = pm.pm_numattr_item(42)
N43_ = pm.pm_numattr_item(43)
N44_ = pm.pm_numattr_item(44)
N45_ = pm.pm_numattr_item(45)
N46_ = pm.pm_numattr_item(46)
N47_ = pm.pm_numattr_item(47)
N48_ = pm.pm_numattr_item(48)
N49_ = pm.pm_numattr_item(49)
N50_ = pm.pm_numattr_item(50)
N51_ = pm.pm_numattr_item(51)
N52_ = pm.pm_numattr_item(52)
N53_ = pm.pm_numattr_item(53)
N54_ = pm.pm_numattr_item(54)
N55_ = pm.pm_numattr_item(55)
N56_ = pm.pm_numattr_item(56)
N57_ = pm.pm_numattr_item(57)
N58_ = pm.pm_numattr_item(58)
N59_ = pm.pm_numattr_item(59)
N60_ = pm.pm_numattr_item(60)
N61_ = pm.pm_numattr_item(61)
N62_ = pm.pm_numattr_item(62)
N63_ = pm.pm_numattr_item(63)
N64_ = pm.pm_numattr_item(64)
N65_ = pm.pm_numattr_item(65)
N66_ = pm.pm_numattr_item(66)
N67_ = pm.pm_numattr_item(67)
N68_ = pm.pm_numattr_item(68)
N69_ = pm.pm_numattr_item(69)
N70_ = pm.pm_numattr_item(70)
N71_ = pm.pm_numattr_item(71)
N72_ = pm.pm_numattr_item(72)
N73_ = pm.pm_numattr_item(73)
N74_ = pm.pm_numattr_item(74)
N75_ = pm.pm_numattr_item(75)
N76_ = pm.pm_numattr_item(76)
N77_ = pm.pm_numattr_item(77)
N78_ = pm.pm_numattr_item(78)
N79_ = pm.pm_numattr_item(79)
N80_ = pm.pm_numattr_item(80)
N81_ = pm.pm_numattr_item(81)
N82_ = pm.pm_numattr_item(82)
N83_ = pm.pm_numattr_item(83)
N84_ = pm.pm_numattr_item(84)
N85_ = pm.pm_numattr_item(85)
N86_ = pm.pm_numattr_item(86)
N87_ = pm.pm_numattr_item(87)
N88_ = pm.pm_numattr_item(88)
N89_ = pm.pm_numattr_item(89)
N90_ = pm.pm_numattr_item(90)
N91_ = pm.pm_numattr_item(91)
N92_ = pm.pm_numattr_item(92)
N93_ = pm.pm_numattr_item(93)
N94_ = pm.pm_numattr_item(94)
N95_ = pm.pm_numattr_item(95)
N96_ = pm.pm_numattr_item(96)
N97_ = pm.pm_numattr_item(97)
N98_ = pm.pm_numattr_item(98)
N99_ = pm.pm_numattr_item(99)
N100_ = pm.pm_numattr_item(100)
N101_ = pm.pm_numattr_item(101)
N102_ = pm.pm_numattr_item(102)
N103_ = pm.pm_numattr_item(103)
N104_ = pm.pm_numattr_item(104)
N105_ = pm.pm_numattr_item(105)
N106_ = pm.pm_numattr_item(106)
N107_ = pm.pm_numattr_item(107)
N108_ = pm.pm_numattr_item(108)
N109_ = pm.pm_numattr_item(109)
N110_ = pm.pm_numattr_item(110)
N111_ = pm.pm_numattr_item(111)
N112_ = pm.pm_numattr_item(112)
N113_ = pm.pm_numattr_item(113)
N114_ = pm.pm_numattr_item(114)
N115_ = pm.pm_numattr_item(115)
N116_ = pm.pm_numattr_item(116)
N117_ = pm.pm_numattr_item(117)
N118_ = pm.pm_numattr_item(118)
N119_ = pm.pm_numattr_item(119)
N120_ = pm.pm_numattr_item(120)
N121_ = pm.pm_numattr_item(121)
N122_ = pm.pm_numattr_item(122)
N123_ = pm.pm_numattr_item(123)
N124_ = pm.pm_numattr_item(124)
N125_ = pm.pm_numattr_item(125)
N126_ = pm.pm_numattr_item(126)
N127_ = pm.pm_numattr_item(127)
N128_ = pm.pm_numattr_item(128)
N129_ = pm.pm_numattr_item(129)
N130_ = pm.pm_numattr_item(130)
N131_ = pm.pm_numattr_item(131)
N132_ = pm.pm_numattr_item(132)
N133_ = pm.pm_numattr_item(133)
N134_ = pm.pm_numattr_item(134)
N135_ = pm.pm_numattr_item(135)
N136_ = pm.pm_numattr_item(136)
N137_ = pm.pm_numattr_item(137)
N138_ = pm.pm_numattr_item(138)
N139_ = pm.pm_numattr_item(139)
N140_ = pm.pm_numattr_item(140)
N141_ = pm.pm_numattr_item(141)
N142_ = pm.pm_numattr_item(142)
N143_ = pm.pm_numattr_item(143)
N144_ = pm.pm_numattr_item(144)
N145_ = pm.pm_numattr_item(145)
N146_ = pm.pm_numattr_item(146)
N147_ = pm.pm_numattr_item(147)
N148_ = pm.pm_numattr_item(148)
N149_ = pm.pm_numattr_item(149)
N150_ = pm.pm_numattr_item(150)
N151_ = pm.pm_numattr_item(151)
N152_ = pm.pm_numattr_item(152)
N153_ = pm.pm_numattr_item(153)
N154_ = pm.pm_numattr_item(154)
N155_ = pm.pm_numattr_item(155)
N156_ = pm.pm_numattr_item(156)
N157_ = pm.pm_numattr_item(157)
N158_ = pm.pm_numattr_item(158)
N159_ = pm.pm_numattr_item(159)
N160_ = pm.pm_numattr_item(160)
N161_ = pm.pm_numattr_item(161)
N162_ = pm.pm_numattr_item(162)
N163_ = pm.pm_numattr_item(163)
N164_ = pm.pm_numattr_item(164)
N165_ = pm.pm_numattr_item(165)
N166_ = pm.pm_numattr_item(166)
N167_ = pm.pm_numattr_item(167)
N168_ = pm.pm_numattr_item(168)
N169_ = pm.pm_numattr_item(169)
N170_ = pm.pm_numattr_item(170)
N171_ = pm.pm_numattr_item(171)
N172_ = pm.pm_numattr_item(172)
N173_ = pm.pm_numattr_item(173)
N174_ = pm.pm_numattr_item(174)
N175_ = pm.pm_numattr_item(175)
N176_ = pm.pm_numattr_item(176)
N177_ = pm.pm_numattr_item(177)
N178_ = pm.pm_numattr_item(178)
N179_ = pm.pm_numattr_item(179)
N180_ = pm.pm_numattr_item(180)
N181_ = pm.pm_numattr_item(181)
N182_ = pm.pm_numattr_item(182)
N183_ = pm.pm_numattr_item(183)
N184_ = pm.pm_numattr_item(184)
N185_ = pm.pm_numattr_item(185)
N186_ = pm.pm_numattr_item(186)
N187_ = pm.pm_numattr_item(187)
N188_ = pm.pm_numattr_item(188)
N189_ = pm.pm_numattr_item(189)
N190_ = pm.pm_numattr_item(190)
N191_ = pm.pm_numattr_item(191)
N192_ = pm.pm_numattr_item(192)
N193_ = pm.pm_numattr_item(193)
N194_ = pm.pm_numattr_item(194)
N195_ = pm.pm_numattr_item(195)
N196_ = pm.pm_numattr_item(196)
N197_ = pm.pm_numattr_item(197)
N198_ = pm.pm_numattr_item(198)
N199_ = pm.pm_numattr_item(199)
N200_ = pm.pm_numattr_item(200)
N201_ = pm.pm_numattr_item(201)
N202_ = pm.pm_numattr_item(202)
N203_ = pm.pm_numattr_item(203)
N204_ = pm.pm_numattr_item(204)
N205_ = pm.pm_numattr_item(205)
N206_ = pm.pm_numattr_item(206)
N207_ = pm.pm_numattr_item(207)
N208_ = pm.pm_numattr_item(208)
N209_ = pm.pm_numattr_item(209)
N210_ = pm.pm_numattr_item(210)
N211_ = pm.pm_numattr_item(211)
N212_ = pm.pm_numattr_item(212)
N213_ = pm.pm_numattr_item(213)
N214_ = pm.pm_numattr_item(214)
N215_ = pm.pm_numattr_item(215)
N216_ = pm.pm_numattr_item(216)
N217_ = pm.pm_numattr_item(217)
N218_ = pm.pm_numattr_item(218)
N219_ = pm.pm_numattr_item(219)
N220_ = pm.pm_numattr_item(220)
N221_ = pm.pm_numattr_item(221)
N222_ = pm.pm_numattr_item(222)
N223_ = pm.pm_numattr_item(223)
N224_ = pm.pm_numattr_item(224)
N225_ = pm.pm_numattr_item(225)
N226_ = pm.pm_numattr_item(226)
N227_ = pm.pm_numattr_item(227)
N228_ = pm.pm_numattr_item(228)
N229_ = pm.pm_numattr_item(229)
N230_ = pm.pm_numattr_item(230)
N231_ = pm.pm_numattr_item(231)
N232_ = pm.pm_numattr_item(232)
N233_ = pm.pm_numattr_item(233)
N234_ = pm.pm_numattr_item(234)
N235_ = pm.pm_numattr_item(235)
N236_ = pm.pm_numattr_item(236)
N237_ = pm.pm_numattr_item(237)
N238_ = pm.pm_numattr_item(238)
N239_ = pm.pm_numattr_item(239)
N240_ = pm.pm_numattr_item(240)
N241_ = pm.pm_numattr_item(241)
N242_ = pm.pm_numattr_item(242)
N243_ = pm.pm_numattr_item(243)
N244_ = pm.pm_numattr_item(244)
N245_ = pm.pm_numattr_item(245)
N246_ = pm.pm_numattr_item(246)
N247_ = pm.pm_numattr_item(247)
N248_ = pm.pm_numattr_item(248)
N249_ = pm.pm_numattr_item(249)
N250_ = pm.pm_numattr_item(250)
N251_ = pm.pm_numattr_item(251)
N252_ = pm.pm_numattr_item(252)
N253_ = pm.pm_numattr_item(253)
N254_ = pm.pm_numattr_item(254)
N255_ = pm.pm_numattr_item(255)
N256_ = pm.pm_numattr_item(256)            
#end

           