// Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/Assignment 1/src/main/d96/parser/D96.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		BLOCK_COMMENT=1, LITERAL=2, INT_LIT=3, FLOAT_LIT=4, BOOL_LIT=5, STR_LIT=6, 
		DIGIT=7, PRIMITIVE_TYPE=8, BREAK=9, CONTINUE=10, IF=11, ELSEIF=12, ELSE=13, 
		FOREACH=14, TRUE=15, FALSE=16, ARRAY=17, IN=18, INT=19, FLOAT=20, BOOLEAN=21, 
		STRING=22, RETURN=23, NULL=24, CLASS=25, VAL=26, VAR=27, SELF=28, CONSTRUCTOR=29, 
		DESTRUCTOR=30, BY=31, ADD=32, SUB_OP=33, MUL=34, DIV=35, PRCNT=36, NOT=37, 
		AND=38, OR=39, EQ=40, ASSIGN=41, NOT_EQ=42, LESS=43, LESS_EQ=44, GREAT=45, 
		GREAT_EQ=46, EQ_STR=47, CONCAT_STR=48, STATIC_ACC=49, OBJ_CREATE=50, LB=51, 
		RB=52, LP=53, RP=54, LSB=55, RSB=56, DOTDOT=57, DOT=58, CM=59, SEMI=60, 
		CL=61, DOUBLEQUOTE=62, ID=63, STATIC_ID=64, WS=65, ERROR_CHAR=66, UNCLOSE_STRING=67, 
		ILLEGAL_ESCAPE=68;
	public static final int
		RULE_program = 0, RULE_class_decl = 1, RULE_mem_list = 2, RULE_attri_decl = 3, 
		RULE_attri_decl_wo_assign = 4, RULE_attri_decl_w_assign = 5, RULE_attri_recurse = 6, 
		RULE_id_list = 7, RULE_method_decl = 8, RULE_param_list = 9, RULE_expr_list = 10, 
		RULE_expr = 11, RULE_expr1 = 12, RULE_expr2 = 13, RULE_expr3 = 14, RULE_expr4 = 15, 
		RULE_expr5 = 16, RULE_expr6 = 17, RULE_expr7 = 18, RULE_idx_op = 19, RULE_expr8 = 20, 
		RULE_expr9 = 21, RULE_expr10 = 22, RULE_expr11 = 23, RULE_operand = 24, 
		RULE_func_call = 25, RULE_stmt = 26, RULE_var_const_stmt = 27, RULE_assign_stmt = 28, 
		RULE_if_stmt = 29, RULE_for_in_stmt = 30, RULE_break_stmt = 31, RULE_cont_stmt = 32, 
		RULE_rtrn_stmt = 33, RULE_method_stmt = 34, RULE_block_stmt = 35, RULE_idx_arr = 36, 
		RULE_mul_dim_arr = 37, RULE_data_type = 38, RULE_array_type = 39, RULE_class_type = 40;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "class_decl", "mem_list", "attri_decl", "attri_decl_wo_assign", 
			"attri_decl_w_assign", "attri_recurse", "id_list", "method_decl", "param_list", 
			"expr_list", "expr", "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
			"expr7", "idx_op", "expr8", "expr9", "expr10", "expr11", "operand", "func_call", 
			"stmt", "var_const_stmt", "assign_stmt", "if_stmt", "for_in_stmt", "break_stmt", 
			"cont_stmt", "rtrn_stmt", "method_stmt", "block_stmt", "idx_arr", "mul_dim_arr", 
			"data_type", "array_type", "class_type"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, "'Break'", "'Continue'", 
			"'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
			"'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
			"'Class'", "'Val'", "'Var'", "'Self'", "'Constructor'", "'Destructor'", 
			"'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
			"'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", "'::'", 
			"'New'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'..'", "'.'", "','", 
			"';'", "':'", "'\"'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "BLOCK_COMMENT", "LITERAL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
			"STR_LIT", "DIGIT", "PRIMITIVE_TYPE", "BREAK", "CONTINUE", "IF", "ELSEIF", 
			"ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
			"STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
			"DESTRUCTOR", "BY", "ADD", "SUB_OP", "MUL", "DIV", "PRCNT", "NOT", "AND", 
			"OR", "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", "GREAT", "GREAT_EQ", 
			"EQ_STR", "CONCAT_STR", "STATIC_ACC", "OBJ_CREATE", "LB", "RB", "LP", 
			"RP", "LSB", "RSB", "DOTDOT", "DOT", "CM", "SEMI", "CL", "DOUBLEQUOTE", 
			"ID", "STATIC_ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public D96Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(D96Parser.EOF, 0); }
		public List<Class_declContext> class_decl() {
			return getRuleContexts(Class_declContext.class);
		}
		public Class_declContext class_decl(int i) {
			return getRuleContext(Class_declContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(82);
				class_decl();
				}
				}
				setState(85); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==CLASS );
			setState(87);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_declContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(D96Parser.CLASS, 0); }
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public Mem_listContext mem_list() {
			return getRuleContext(Mem_listContext.class,0);
		}
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public TerminalNode CL() { return getToken(D96Parser.CL, 0); }
		public Class_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_decl; }
	}

	public final Class_declContext class_decl() throws RecognitionException {
		Class_declContext _localctx = new Class_declContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_class_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			match(CLASS);
			setState(90);
			match(ID);
			setState(93);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CL) {
				{
				setState(91);
				match(CL);
				setState(92);
				match(ID);
				}
			}

			setState(95);
			match(LP);
			setState(96);
			mem_list();
			setState(97);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Mem_listContext extends ParserRuleContext {
		public List<Attri_declContext> attri_decl() {
			return getRuleContexts(Attri_declContext.class);
		}
		public Attri_declContext attri_decl(int i) {
			return getRuleContext(Attri_declContext.class,i);
		}
		public List<Method_declContext> method_decl() {
			return getRuleContexts(Method_declContext.class);
		}
		public Method_declContext method_decl(int i) {
			return getRuleContext(Method_declContext.class,i);
		}
		public Mem_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mem_list; }
	}

	public final Mem_listContext mem_list() throws RecognitionException {
		Mem_listContext _localctx = new Mem_listContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_mem_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 26)) & ~0x3f) == 0 && ((1L << (_la - 26)) & ((1L << (VAL - 26)) | (1L << (VAR - 26)) | (1L << (CONSTRUCTOR - 26)) | (1L << (DESTRUCTOR - 26)) | (1L << (ID - 26)) | (1L << (STATIC_ID - 26)))) != 0)) {
				{
				setState(101);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case VAL:
				case VAR:
					{
					setState(99);
					attri_decl();
					}
					break;
				case CONSTRUCTOR:
				case DESTRUCTOR:
				case ID:
				case STATIC_ID:
					{
					setState(100);
					method_decl();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(105);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attri_declContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public TerminalNode VAL() { return getToken(D96Parser.VAL, 0); }
		public TerminalNode VAR() { return getToken(D96Parser.VAR, 0); }
		public Attri_decl_wo_assignContext attri_decl_wo_assign() {
			return getRuleContext(Attri_decl_wo_assignContext.class,0);
		}
		public Attri_decl_w_assignContext attri_decl_w_assign() {
			return getRuleContext(Attri_decl_w_assignContext.class,0);
		}
		public Attri_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attri_decl; }
	}

	public final Attri_declContext attri_decl() throws RecognitionException {
		Attri_declContext _localctx = new Attri_declContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_attri_decl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(106);
			_la = _input.LA(1);
			if ( !(_la==VAL || _la==VAR) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(109);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
			case 1:
				{
				setState(107);
				attri_decl_wo_assign();
				}
				break;
			case 2:
				{
				setState(108);
				attri_decl_w_assign();
				}
				break;
			}
			setState(111);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attri_decl_wo_assignContext extends ParserRuleContext {
		public Id_listContext id_list() {
			return getRuleContext(Id_listContext.class,0);
		}
		public TerminalNode CL() { return getToken(D96Parser.CL, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public Attri_decl_wo_assignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attri_decl_wo_assign; }
	}

	public final Attri_decl_wo_assignContext attri_decl_wo_assign() throws RecognitionException {
		Attri_decl_wo_assignContext _localctx = new Attri_decl_wo_assignContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_attri_decl_wo_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(113);
			id_list();
			setState(114);
			match(CL);
			setState(115);
			data_type();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attri_decl_w_assignContext extends ParserRuleContext {
		public Attri_recurseContext attri_recurse() {
			return getRuleContext(Attri_recurseContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode STATIC_ID() { return getToken(D96Parser.STATIC_ID, 0); }
		public Attri_decl_w_assignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attri_decl_w_assign; }
	}

	public final Attri_decl_w_assignContext attri_decl_w_assign() throws RecognitionException {
		Attri_decl_w_assignContext _localctx = new Attri_decl_w_assignContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_attri_decl_w_assign);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(117);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STATIC_ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(118);
			attri_recurse();
			setState(119);
			expr();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Attri_recurseContext extends ParserRuleContext {
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Attri_recurseContext attri_recurse() {
			return getRuleContext(Attri_recurseContext.class,0);
		}
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode STATIC_ID() { return getToken(D96Parser.STATIC_ID, 0); }
		public TerminalNode CL() { return getToken(D96Parser.CL, 0); }
		public Data_typeContext data_type() {
			return getRuleContext(Data_typeContext.class,0);
		}
		public TerminalNode EQ() { return getToken(D96Parser.EQ, 0); }
		public Attri_recurseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attri_recurse; }
	}

	public final Attri_recurseContext attri_recurse() throws RecognitionException {
		Attri_recurseContext _localctx = new Attri_recurseContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_attri_recurse);
		int _la;
		try {
			setState(131);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CM:
				enterOuterAlt(_localctx, 1);
				{
				setState(121);
				match(CM);
				setState(122);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STATIC_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(123);
				attri_recurse();
				setState(124);
				expr();
				setState(125);
				match(CM);
				}
				break;
			case CL:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				match(CL);
				setState(128);
				data_type();
				setState(129);
				match(EQ);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Id_listContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public List<TerminalNode> STATIC_ID() { return getTokens(D96Parser.STATIC_ID); }
		public TerminalNode STATIC_ID(int i) {
			return getToken(D96Parser.STATIC_ID, i);
		}
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Id_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_list; }
	}

	public final Id_listContext id_list() throws RecognitionException {
		Id_listContext _localctx = new Id_listContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_id_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(133);
			_la = _input.LA(1);
			if ( !(_la==ID || _la==STATIC_ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(138);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(134);
				match(CM);
				setState(135);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STATIC_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				setState(140);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_declContext extends ParserRuleContext {
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode STATIC_ID() { return getToken(D96Parser.STATIC_ID, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode CONSTRUCTOR() { return getToken(D96Parser.CONSTRUCTOR, 0); }
		public TerminalNode DESTRUCTOR() { return getToken(D96Parser.DESTRUCTOR, 0); }
		public Method_declContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_decl; }
	}

	public final Method_declContext method_decl() throws RecognitionException {
		Method_declContext _localctx = new Method_declContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_method_decl);
		int _la;
		try {
			setState(159);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case STATIC_ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(141);
				_la = _input.LA(1);
				if ( !(_la==ID || _la==STATIC_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(142);
				match(LB);
				setState(144);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID || _la==STATIC_ID) {
					{
					setState(143);
					param_list();
					}
				}

				setState(146);
				match(RB);
				setState(147);
				block_stmt();
				}
				break;
			case CONSTRUCTOR:
				enterOuterAlt(_localctx, 2);
				{
				setState(148);
				match(CONSTRUCTOR);
				setState(149);
				match(LB);
				setState(151);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID || _la==STATIC_ID) {
					{
					setState(150);
					param_list();
					}
				}

				setState(153);
				match(RB);
				setState(154);
				block_stmt();
				}
				break;
			case DESTRUCTOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(155);
				match(DESTRUCTOR);
				setState(156);
				match(LB);
				setState(157);
				match(RB);
				setState(158);
				block_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_listContext extends ParserRuleContext {
		public List<Id_listContext> id_list() {
			return getRuleContexts(Id_listContext.class);
		}
		public Id_listContext id_list(int i) {
			return getRuleContext(Id_listContext.class,i);
		}
		public List<TerminalNode> CL() { return getTokens(D96Parser.CL); }
		public TerminalNode CL(int i) {
			return getToken(D96Parser.CL, i);
		}
		public List<Data_typeContext> data_type() {
			return getRuleContexts(Data_typeContext.class);
		}
		public Data_typeContext data_type(int i) {
			return getRuleContext(Data_typeContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(D96Parser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(D96Parser.SEMI, i);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_param_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(161);
			id_list();
			setState(162);
			match(CL);
			setState(163);
			data_type();
			setState(171);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SEMI) {
				{
				{
				setState(164);
				match(SEMI);
				setState(165);
				id_list();
				setState(166);
				match(CL);
				setState(167);
				data_type();
				}
				}
				setState(173);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr_listContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Expr_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr_list; }
	}

	public final Expr_listContext expr_list() throws RecognitionException {
		Expr_listContext _localctx = new Expr_listContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_expr_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			expr();
			setState(179);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==CM) {
				{
				{
				setState(175);
				match(CM);
				setState(176);
				expr();
				}
				}
				setState(181);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public List<Expr1Context> expr1() {
			return getRuleContexts(Expr1Context.class);
		}
		public Expr1Context expr1(int i) {
			return getRuleContext(Expr1Context.class,i);
		}
		public TerminalNode EQ_STR() { return getToken(D96Parser.EQ_STR, 0); }
		public TerminalNode CONCAT_STR() { return getToken(D96Parser.CONCAT_STR, 0); }
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_expr);
		int _la;
		try {
			setState(187);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(182);
				expr1();
				setState(183);
				_la = _input.LA(1);
				if ( !(_la==EQ_STR || _la==CONCAT_STR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(184);
				expr1();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(186);
				expr1();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr1Context extends ParserRuleContext {
		public List<Expr2Context> expr2() {
			return getRuleContexts(Expr2Context.class);
		}
		public Expr2Context expr2(int i) {
			return getRuleContext(Expr2Context.class,i);
		}
		public TerminalNode EQ() { return getToken(D96Parser.EQ, 0); }
		public TerminalNode NOT_EQ() { return getToken(D96Parser.NOT_EQ, 0); }
		public TerminalNode LESS() { return getToken(D96Parser.LESS, 0); }
		public TerminalNode GREAT() { return getToken(D96Parser.GREAT, 0); }
		public TerminalNode LESS_EQ() { return getToken(D96Parser.LESS_EQ, 0); }
		public TerminalNode GREAT_EQ() { return getToken(D96Parser.GREAT_EQ, 0); }
		public Expr1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr1; }
	}

	public final Expr1Context expr1() throws RecognitionException {
		Expr1Context _localctx = new Expr1Context(_ctx, getState());
		enterRule(_localctx, 24, RULE_expr1);
		int _la;
		try {
			setState(194);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(189);
				expr2();
				setState(190);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NOT_EQ) | (1L << LESS) | (1L << LESS_EQ) | (1L << GREAT) | (1L << GREAT_EQ))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(191);
				expr2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(193);
				expr2();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr2Context extends ParserRuleContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public TerminalNode AND() { return getToken(D96Parser.AND, 0); }
		public TerminalNode OR() { return getToken(D96Parser.OR, 0); }
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	}

	public final Expr2Context expr2() throws RecognitionException {
		Expr2Context _localctx = new Expr2Context(_ctx, getState());
		enterRule(_localctx, 26, RULE_expr2);
		int _la;
		try {
			setState(201);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(196);
				expr3();
				setState(197);
				_la = _input.LA(1);
				if ( !(_la==AND || _la==OR) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(198);
				expr2();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(200);
				expr3();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr3Context extends ParserRuleContext {
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public TerminalNode ADD() { return getToken(D96Parser.ADD, 0); }
		public TerminalNode SUB_OP() { return getToken(D96Parser.SUB_OP, 0); }
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
	}

	public final Expr3Context expr3() throws RecognitionException {
		Expr3Context _localctx = new Expr3Context(_ctx, getState());
		enterRule(_localctx, 28, RULE_expr3);
		int _la;
		try {
			setState(208);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(203);
				expr4();
				setState(204);
				_la = _input.LA(1);
				if ( !(_la==ADD || _la==SUB_OP) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(205);
				expr3();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(207);
				expr4();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr4Context extends ParserRuleContext {
		public Expr5Context expr5() {
			return getRuleContext(Expr5Context.class,0);
		}
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public TerminalNode MUL() { return getToken(D96Parser.MUL, 0); }
		public TerminalNode DIV() { return getToken(D96Parser.DIV, 0); }
		public TerminalNode PRCNT() { return getToken(D96Parser.PRCNT, 0); }
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
	}

	public final Expr4Context expr4() throws RecognitionException {
		Expr4Context _localctx = new Expr4Context(_ctx, getState());
		enterRule(_localctx, 30, RULE_expr4);
		int _la;
		try {
			setState(215);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(210);
				expr5();
				setState(211);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << MUL) | (1L << DIV) | (1L << PRCNT))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(212);
				expr4();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(214);
				expr5();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr5Context extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(D96Parser.NOT, 0); }
		public Expr6Context expr6() {
			return getRuleContext(Expr6Context.class,0);
		}
		public Expr5Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr5; }
	}

	public final Expr5Context expr5() throws RecognitionException {
		Expr5Context _localctx = new Expr5Context(_ctx, getState());
		enterRule(_localctx, 32, RULE_expr5);
		try {
			setState(220);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(217);
				match(NOT);
				setState(218);
				expr6();
				}
				break;
			case LITERAL:
			case SELF:
			case SUB_OP:
			case OBJ_CREATE:
			case LB:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(219);
				expr6();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr6Context extends ParserRuleContext {
		public TerminalNode SUB_OP() { return getToken(D96Parser.SUB_OP, 0); }
		public Expr7Context expr7() {
			return getRuleContext(Expr7Context.class,0);
		}
		public Expr6Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr6; }
	}

	public final Expr6Context expr6() throws RecognitionException {
		Expr6Context _localctx = new Expr6Context(_ctx, getState());
		enterRule(_localctx, 34, RULE_expr6);
		try {
			setState(225);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUB_OP:
				enterOuterAlt(_localctx, 1);
				{
				setState(222);
				match(SUB_OP);
				setState(223);
				expr7();
				}
				break;
			case LITERAL:
			case SELF:
			case OBJ_CREATE:
			case LB:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(224);
				expr7();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr7Context extends ParserRuleContext {
		public Expr8Context expr8() {
			return getRuleContext(Expr8Context.class,0);
		}
		public Idx_opContext idx_op() {
			return getRuleContext(Idx_opContext.class,0);
		}
		public Expr7Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr7; }
	}

	public final Expr7Context expr7() throws RecognitionException {
		Expr7Context _localctx = new Expr7Context(_ctx, getState());
		enterRule(_localctx, 36, RULE_expr7);
		try {
			setState(231);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(227);
				expr8();
				setState(228);
				idx_op();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(230);
				expr8();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Idx_opContext extends ParserRuleContext {
		public TerminalNode LSB() { return getToken(D96Parser.LSB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RSB() { return getToken(D96Parser.RSB, 0); }
		public Idx_opContext idx_op() {
			return getRuleContext(Idx_opContext.class,0);
		}
		public Idx_opContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idx_op; }
	}

	public final Idx_opContext idx_op() throws RecognitionException {
		Idx_opContext _localctx = new Idx_opContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_idx_op);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(LSB);
			setState(234);
			expr();
			setState(235);
			match(RSB);
			setState(237);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(236);
				idx_op();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr8Context extends ParserRuleContext {
		public TerminalNode DOT() { return getToken(D96Parser.DOT, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public Expr9Context expr9() {
			return getRuleContext(Expr9Context.class,0);
		}
		public TerminalNode SELF() { return getToken(D96Parser.SELF, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Expr8Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr8; }
	}

	public final Expr8Context expr8() throws RecognitionException {
		Expr8Context _localctx = new Expr8Context(_ctx, getState());
		enterRule(_localctx, 40, RULE_expr8);
		try {
			setState(256);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(241);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LITERAL:
				case OBJ_CREATE:
				case LB:
				case ID:
					{
					setState(239);
					expr9();
					}
					break;
				case SELF:
					{
					setState(240);
					match(SELF);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(243);
				match(DOT);
				setState(244);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(247);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case LITERAL:
				case OBJ_CREATE:
				case LB:
				case ID:
					{
					setState(245);
					expr9();
					}
					break;
				case SELF:
					{
					setState(246);
					match(SELF);
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(249);
				match(DOT);
				setState(250);
				match(ID);
				setState(251);
				match(LB);
				setState(252);
				expr_list();
				setState(253);
				match(RB);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(255);
				expr9();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr9Context extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode STATIC_ID() { return getToken(D96Parser.STATIC_ID, 0); }
		public TerminalNode SELF() { return getToken(D96Parser.SELF, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Expr10Context expr10() {
			return getRuleContext(Expr10Context.class,0);
		}
		public Expr9Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr9; }
	}

	public final Expr9Context expr9() throws RecognitionException {
		Expr9Context _localctx = new Expr9Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_expr9);
		int _la;
		try {
			setState(267);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(258);
				match(ID);
				setState(259);
				_la = _input.LA(1);
				if ( !(_la==SELF || _la==STATIC_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(260);
				match(ID);
				setState(261);
				_la = _input.LA(1);
				if ( !(_la==SELF || _la==STATIC_ID) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(262);
				match(LB);
				setState(263);
				expr_list();
				setState(264);
				match(RB);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(266);
				expr10();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr10Context extends ParserRuleContext {
		public Class_typeContext class_type() {
			return getRuleContext(Class_typeContext.class,0);
		}
		public Expr11Context expr11() {
			return getRuleContext(Expr11Context.class,0);
		}
		public Expr10Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr10; }
	}

	public final Expr10Context expr10() throws RecognitionException {
		Expr10Context _localctx = new Expr10Context(_ctx, getState());
		enterRule(_localctx, 44, RULE_expr10);
		try {
			setState(271);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OBJ_CREATE:
				enterOuterAlt(_localctx, 1);
				{
				setState(269);
				class_type();
				}
				break;
			case LITERAL:
			case LB:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(270);
				expr11();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Expr11Context extends ParserRuleContext {
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public OperandContext operand() {
			return getRuleContext(OperandContext.class,0);
		}
		public Expr11Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr11; }
	}

	public final Expr11Context expr11() throws RecognitionException {
		Expr11Context _localctx = new Expr11Context(_ctx, getState());
		enterRule(_localctx, 46, RULE_expr11);
		try {
			setState(278);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LB:
				enterOuterAlt(_localctx, 1);
				{
				setState(273);
				match(LB);
				setState(274);
				expr();
				setState(275);
				match(RB);
				}
				break;
			case LITERAL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(277);
				operand();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class OperandContext extends ParserRuleContext {
		public TerminalNode LITERAL() { return getToken(D96Parser.LITERAL, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public Func_callContext func_call() {
			return getRuleContext(Func_callContext.class,0);
		}
		public OperandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operand; }
	}

	public final OperandContext operand() throws RecognitionException {
		OperandContext _localctx = new OperandContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_operand);
		try {
			setState(283);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(280);
				match(LITERAL);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(281);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(282);
				func_call();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Func_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Func_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func_call; }
	}

	public final Func_callContext func_call() throws RecognitionException {
		Func_callContext _localctx = new Func_callContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_func_call);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(285);
			match(ID);
			setState(286);
			match(LB);
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LITERAL) | (1L << SELF) | (1L << SUB_OP) | (1L << NOT) | (1L << OBJ_CREATE) | (1L << LB) | (1L << ID))) != 0)) {
				{
				setState(287);
				expr_list();
				}
			}

			setState(290);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StmtContext extends ParserRuleContext {
		public Var_const_stmtContext var_const_stmt() {
			return getRuleContext(Var_const_stmtContext.class,0);
		}
		public Assign_stmtContext assign_stmt() {
			return getRuleContext(Assign_stmtContext.class,0);
		}
		public If_stmtContext if_stmt() {
			return getRuleContext(If_stmtContext.class,0);
		}
		public For_in_stmtContext for_in_stmt() {
			return getRuleContext(For_in_stmtContext.class,0);
		}
		public Break_stmtContext break_stmt() {
			return getRuleContext(Break_stmtContext.class,0);
		}
		public Cont_stmtContext cont_stmt() {
			return getRuleContext(Cont_stmtContext.class,0);
		}
		public Rtrn_stmtContext rtrn_stmt() {
			return getRuleContext(Rtrn_stmtContext.class,0);
		}
		public Method_stmtContext method_stmt() {
			return getRuleContext(Method_stmtContext.class,0);
		}
		public StmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stmt; }
	}

	public final StmtContext stmt() throws RecognitionException {
		StmtContext _localctx = new StmtContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_stmt);
		try {
			setState(300);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAL:
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				var_const_stmt();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
				assign_stmt();
				}
				break;
			case IF:
				enterOuterAlt(_localctx, 3);
				{
				setState(294);
				if_stmt();
				}
				break;
			case FOREACH:
				enterOuterAlt(_localctx, 4);
				{
				setState(295);
				for_in_stmt();
				}
				break;
			case BREAK:
				enterOuterAlt(_localctx, 5);
				{
				setState(296);
				break_stmt();
				}
				break;
			case CONTINUE:
				enterOuterAlt(_localctx, 6);
				{
				setState(297);
				cont_stmt();
				}
				break;
			case RETURN:
				enterOuterAlt(_localctx, 7);
				{
				setState(298);
				rtrn_stmt();
				}
				break;
			case SEMI:
				enterOuterAlt(_localctx, 8);
				{
				setState(299);
				method_stmt();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Var_const_stmtContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(D96Parser.VAR, 0); }
		public List<TerminalNode> ID() { return getTokens(D96Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(D96Parser.ID, i);
		}
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public TerminalNode VAL() { return getToken(D96Parser.VAL, 0); }
		public Var_const_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var_const_stmt; }
	}

	public final Var_const_stmtContext var_const_stmt() throws RecognitionException {
		Var_const_stmtContext _localctx = new Var_const_stmtContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_var_const_stmt);
		int _la;
		try {
			setState(320);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(302);
				match(VAR);
				setState(303);
				match(ID);
				setState(308);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(304);
					match(CM);
					setState(305);
					match(ID);
					}
					}
					setState(310);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case VAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(311);
				match(VAL);
				setState(312);
				match(ID);
				setState(317);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(313);
					match(CM);
					setState(314);
					match(ID);
					}
					}
					setState(319);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_stmtContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode EQ() { return getToken(D96Parser.EQ, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public Assign_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_stmt; }
	}

	public final Assign_stmtContext assign_stmt() throws RecognitionException {
		Assign_stmtContext _localctx = new Assign_stmtContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_assign_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			match(ID);
			setState(323);
			match(EQ);
			setState(324);
			expr();
			setState(325);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_stmtContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(D96Parser.IF, 0); }
		public List<TerminalNode> LB() { return getTokens(D96Parser.LB); }
		public TerminalNode LB(int i) {
			return getToken(D96Parser.LB, i);
		}
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> RB() { return getTokens(D96Parser.RB); }
		public TerminalNode RB(int i) {
			return getToken(D96Parser.RB, i);
		}
		public List<Block_stmtContext> block_stmt() {
			return getRuleContexts(Block_stmtContext.class);
		}
		public Block_stmtContext block_stmt(int i) {
			return getRuleContext(Block_stmtContext.class,i);
		}
		public List<TerminalNode> ELSEIF() { return getTokens(D96Parser.ELSEIF); }
		public TerminalNode ELSEIF(int i) {
			return getToken(D96Parser.ELSEIF, i);
		}
		public TerminalNode ELSE() { return getToken(D96Parser.ELSE, 0); }
		public If_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_stmt; }
	}

	public final If_stmtContext if_stmt() throws RecognitionException {
		If_stmtContext _localctx = new If_stmtContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_if_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(327);
			match(IF);
			setState(328);
			match(LB);
			setState(329);
			expr();
			setState(330);
			match(RB);
			setState(331);
			block_stmt();
			setState(340);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ELSEIF) {
				{
				{
				setState(332);
				match(ELSEIF);
				setState(333);
				match(LB);
				setState(334);
				expr();
				setState(335);
				match(RB);
				setState(336);
				block_stmt();
				}
				}
				setState(342);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(345);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(343);
				match(ELSE);
				setState(344);
				block_stmt();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class For_in_stmtContext extends ParserRuleContext {
		public TerminalNode FOREACH() { return getToken(D96Parser.FOREACH, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode IN() { return getToken(D96Parser.IN, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DOTDOT() { return getToken(D96Parser.DOTDOT, 0); }
		public Block_stmtContext block_stmt() {
			return getRuleContext(Block_stmtContext.class,0);
		}
		public TerminalNode LSB() { return getToken(D96Parser.LSB, 0); }
		public TerminalNode BY() { return getToken(D96Parser.BY, 0); }
		public TerminalNode RSB() { return getToken(D96Parser.RSB, 0); }
		public For_in_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_for_in_stmt; }
	}

	public final For_in_stmtContext for_in_stmt() throws RecognitionException {
		For_in_stmtContext _localctx = new For_in_stmtContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_for_in_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(347);
			match(FOREACH);
			setState(348);
			match(LB);
			setState(349);
			match(IN);
			setState(350);
			expr();
			setState(351);
			match(DOTDOT);
			setState(352);
			expr();
			setState(358);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LSB) {
				{
				setState(353);
				match(LSB);
				setState(354);
				match(BY);
				setState(355);
				expr();
				setState(356);
				match(RSB);
				}
			}

			setState(360);
			block_stmt();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Break_stmtContext extends ParserRuleContext {
		public TerminalNode BREAK() { return getToken(D96Parser.BREAK, 0); }
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public Break_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_break_stmt; }
	}

	public final Break_stmtContext break_stmt() throws RecognitionException {
		Break_stmtContext _localctx = new Break_stmtContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_break_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(362);
			match(BREAK);
			setState(363);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Cont_stmtContext extends ParserRuleContext {
		public TerminalNode CONTINUE() { return getToken(D96Parser.CONTINUE, 0); }
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public Cont_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cont_stmt; }
	}

	public final Cont_stmtContext cont_stmt() throws RecognitionException {
		Cont_stmtContext _localctx = new Cont_stmtContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_cont_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(365);
			match(CONTINUE);
			setState(366);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Rtrn_stmtContext extends ParserRuleContext {
		public TerminalNode RETURN() { return getToken(D96Parser.RETURN, 0); }
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Rtrn_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rtrn_stmt; }
	}

	public final Rtrn_stmtContext rtrn_stmt() throws RecognitionException {
		Rtrn_stmtContext _localctx = new Rtrn_stmtContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_rtrn_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(368);
			match(RETURN);
			setState(370);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LITERAL) | (1L << SELF) | (1L << SUB_OP) | (1L << NOT) | (1L << OBJ_CREATE) | (1L << LB) | (1L << ID))) != 0)) {
				{
				setState(369);
				expr();
				}
			}

			setState(372);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Method_stmtContext extends ParserRuleContext {
		public TerminalNode SEMI() { return getToken(D96Parser.SEMI, 0); }
		public Method_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_method_stmt; }
	}

	public final Method_stmtContext method_stmt() throws RecognitionException {
		Method_stmtContext _localctx = new Method_stmtContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_method_stmt);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			match(SEMI);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Block_stmtContext extends ParserRuleContext {
		public TerminalNode LP() { return getToken(D96Parser.LP, 0); }
		public TerminalNode RP() { return getToken(D96Parser.RP, 0); }
		public List<StmtContext> stmt() {
			return getRuleContexts(StmtContext.class);
		}
		public StmtContext stmt(int i) {
			return getRuleContext(StmtContext.class,i);
		}
		public Block_stmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block_stmt; }
	}

	public final Block_stmtContext block_stmt() throws RecognitionException {
		Block_stmtContext _localctx = new Block_stmtContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_block_stmt);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(376);
			match(LP);
			setState(378); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(377);
				stmt();
				}
				}
				setState(380); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BREAK) | (1L << CONTINUE) | (1L << IF) | (1L << FOREACH) | (1L << RETURN) | (1L << VAL) | (1L << VAR) | (1L << SEMI) | (1L << ID))) != 0) );
			setState(382);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Idx_arrContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public List<TerminalNode> LITERAL() { return getTokens(D96Parser.LITERAL); }
		public TerminalNode LITERAL(int i) {
			return getToken(D96Parser.LITERAL, i);
		}
		public List<TerminalNode> CM() { return getTokens(D96Parser.CM); }
		public TerminalNode CM(int i) {
			return getToken(D96Parser.CM, i);
		}
		public Idx_arrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_idx_arr; }
	}

	public final Idx_arrContext idx_arr() throws RecognitionException {
		Idx_arrContext _localctx = new Idx_arrContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_idx_arr);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(384);
			match(ARRAY);
			setState(385);
			match(LB);
			setState(394);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LITERAL) {
				{
				setState(386);
				match(LITERAL);
				setState(391);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==CM) {
					{
					{
					setState(387);
					match(CM);
					setState(388);
					match(LITERAL);
					}
					}
					setState(393);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(396);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Mul_dim_arrContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public List<Idx_arrContext> idx_arr() {
			return getRuleContexts(Idx_arrContext.class);
		}
		public Idx_arrContext idx_arr(int i) {
			return getRuleContext(Idx_arrContext.class,i);
		}
		public Mul_dim_arrContext mul_dim_arr() {
			return getRuleContext(Mul_dim_arrContext.class,0);
		}
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public Mul_dim_arrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mul_dim_arr; }
	}

	public final Mul_dim_arrContext mul_dim_arr() throws RecognitionException {
		Mul_dim_arrContext _localctx = new Mul_dim_arrContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_mul_dim_arr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(398);
			match(ARRAY);
			setState(399);
			match(LB);
			setState(405);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				{
				setState(400);
				idx_arr();
				{
				setState(401);
				match(CM);
				setState(402);
				idx_arr();
				}
				}
				break;
			case 2:
				{
				setState(404);
				mul_dim_arr();
				}
				break;
			}
			setState(407);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Data_typeContext extends ParserRuleContext {
		public TerminalNode PRIMITIVE_TYPE() { return getToken(D96Parser.PRIMITIVE_TYPE, 0); }
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Class_typeContext class_type() {
			return getRuleContext(Class_typeContext.class,0);
		}
		public Data_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data_type; }
	}

	public final Data_typeContext data_type() throws RecognitionException {
		Data_typeContext _localctx = new Data_typeContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_data_type);
		try {
			setState(412);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRIMITIVE_TYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(409);
				match(PRIMITIVE_TYPE);
				}
				break;
			case ARRAY:
				enterOuterAlt(_localctx, 2);
				{
				setState(410);
				array_type();
				}
				break;
			case OBJ_CREATE:
				enterOuterAlt(_localctx, 3);
				{
				setState(411);
				class_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public TerminalNode ARRAY() { return getToken(D96Parser.ARRAY, 0); }
		public TerminalNode LSB() { return getToken(D96Parser.LSB, 0); }
		public TerminalNode CM() { return getToken(D96Parser.CM, 0); }
		public TerminalNode LITERAL() { return getToken(D96Parser.LITERAL, 0); }
		public TerminalNode RSB() { return getToken(D96Parser.RSB, 0); }
		public TerminalNode PRIMITIVE_TYPE() { return getToken(D96Parser.PRIMITIVE_TYPE, 0); }
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_array_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(414);
			match(ARRAY);
			setState(415);
			match(LSB);
			setState(418);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PRIMITIVE_TYPE:
				{
				setState(416);
				match(PRIMITIVE_TYPE);
				}
				break;
			case ARRAY:
				{
				setState(417);
				array_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(420);
			match(CM);
			setState(421);
			match(LITERAL);
			setState(422);
			match(RSB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_typeContext extends ParserRuleContext {
		public TerminalNode OBJ_CREATE() { return getToken(D96Parser.OBJ_CREATE, 0); }
		public TerminalNode ID() { return getToken(D96Parser.ID, 0); }
		public TerminalNode LB() { return getToken(D96Parser.LB, 0); }
		public TerminalNode RB() { return getToken(D96Parser.RB, 0); }
		public Expr_listContext expr_list() {
			return getRuleContext(Expr_listContext.class,0);
		}
		public Class_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_type; }
	}

	public final Class_typeContext class_type() throws RecognitionException {
		Class_typeContext _localctx = new Class_typeContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_class_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(424);
			match(OBJ_CREATE);
			setState(425);
			match(ID);
			setState(426);
			match(LB);
			setState(428);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LITERAL) | (1L << SELF) | (1L << SUB_OP) | (1L << NOT) | (1L << OBJ_CREATE) | (1L << LB) | (1L << ID))) != 0)) {
				{
				setState(427);
				expr_list();
				}
			}

			setState(430);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F\u01b3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\6\2"+
		"V\n\2\r\2\16\2W\3\2\3\2\3\3\3\3\3\3\3\3\5\3`\n\3\3\3\3\3\3\3\3\3\3\4\3"+
		"\4\7\4h\n\4\f\4\16\4k\13\4\3\5\3\5\3\5\5\5p\n\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u0086\n"+
		"\b\3\t\3\t\3\t\7\t\u008b\n\t\f\t\16\t\u008e\13\t\3\n\3\n\3\n\5\n\u0093"+
		"\n\n\3\n\3\n\3\n\3\n\3\n\5\n\u009a\n\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00a2"+
		"\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u00ac\n\13\f\13\16\13"+
		"\u00af\13\13\3\f\3\f\3\f\7\f\u00b4\n\f\f\f\16\f\u00b7\13\f\3\r\3\r\3\r"+
		"\3\r\3\r\5\r\u00be\n\r\3\16\3\16\3\16\3\16\3\16\5\16\u00c5\n\16\3\17\3"+
		"\17\3\17\3\17\3\17\5\17\u00cc\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00d3"+
		"\n\20\3\21\3\21\3\21\3\21\3\21\5\21\u00da\n\21\3\22\3\22\3\22\5\22\u00df"+
		"\n\22\3\23\3\23\3\23\5\23\u00e4\n\23\3\24\3\24\3\24\3\24\5\24\u00ea\n"+
		"\24\3\25\3\25\3\25\3\25\5\25\u00f0\n\25\3\26\3\26\5\26\u00f4\n\26\3\26"+
		"\3\26\3\26\3\26\5\26\u00fa\n\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26"+
		"\u0103\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u010e\n"+
		"\27\3\30\3\30\5\30\u0112\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u0119\n\31"+
		"\3\32\3\32\3\32\5\32\u011e\n\32\3\33\3\33\3\33\5\33\u0123\n\33\3\33\3"+
		"\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u012f\n\34\3\35\3\35"+
		"\3\35\3\35\7\35\u0135\n\35\f\35\16\35\u0138\13\35\3\35\3\35\3\35\3\35"+
		"\7\35\u013e\n\35\f\35\16\35\u0141\13\35\5\35\u0143\n\35\3\36\3\36\3\36"+
		"\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\7\37"+
		"\u0155\n\37\f\37\16\37\u0158\13\37\3\37\3\37\5\37\u015c\n\37\3 \3 \3 "+
		"\3 \3 \3 \3 \3 \3 \3 \3 \5 \u0169\n \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#"+
		"\5#\u0175\n#\3#\3#\3$\3$\3%\3%\6%\u017d\n%\r%\16%\u017e\3%\3%\3&\3&\3"+
		"&\3&\3&\7&\u0188\n&\f&\16&\u018b\13&\5&\u018d\n&\3&\3&\3\'\3\'\3\'\3\'"+
		"\3\'\3\'\3\'\5\'\u0198\n\'\3\'\3\'\3(\3(\3(\5(\u019f\n(\3)\3)\3)\3)\5"+
		")\u01a5\n)\3)\3)\3)\3)\3*\3*\3*\3*\5*\u01af\n*\3*\3*\3*\2\2+\2\4\6\b\n"+
		"\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\n\3"+
		"\2\34\35\3\2AB\3\2\61\62\4\2**,\60\3\2()\3\2\"#\3\2$&\4\2\36\36BB\2\u01c0"+
		"\2U\3\2\2\2\4[\3\2\2\2\6i\3\2\2\2\bl\3\2\2\2\ns\3\2\2\2\fw\3\2\2\2\16"+
		"\u0085\3\2\2\2\20\u0087\3\2\2\2\22\u00a1\3\2\2\2\24\u00a3\3\2\2\2\26\u00b0"+
		"\3\2\2\2\30\u00bd\3\2\2\2\32\u00c4\3\2\2\2\34\u00cb\3\2\2\2\36\u00d2\3"+
		"\2\2\2 \u00d9\3\2\2\2\"\u00de\3\2\2\2$\u00e3\3\2\2\2&\u00e9\3\2\2\2(\u00eb"+
		"\3\2\2\2*\u0102\3\2\2\2,\u010d\3\2\2\2.\u0111\3\2\2\2\60\u0118\3\2\2\2"+
		"\62\u011d\3\2\2\2\64\u011f\3\2\2\2\66\u012e\3\2\2\28\u0142\3\2\2\2:\u0144"+
		"\3\2\2\2<\u0149\3\2\2\2>\u015d\3\2\2\2@\u016c\3\2\2\2B\u016f\3\2\2\2D"+
		"\u0172\3\2\2\2F\u0178\3\2\2\2H\u017a\3\2\2\2J\u0182\3\2\2\2L\u0190\3\2"+
		"\2\2N\u019e\3\2\2\2P\u01a0\3\2\2\2R\u01aa\3\2\2\2TV\5\4\3\2UT\3\2\2\2"+
		"VW\3\2\2\2WU\3\2\2\2WX\3\2\2\2XY\3\2\2\2YZ\7\2\2\3Z\3\3\2\2\2[\\\7\33"+
		"\2\2\\_\7A\2\2]^\7?\2\2^`\7A\2\2_]\3\2\2\2_`\3\2\2\2`a\3\2\2\2ab\7\67"+
		"\2\2bc\5\6\4\2cd\78\2\2d\5\3\2\2\2eh\5\b\5\2fh\5\22\n\2ge\3\2\2\2gf\3"+
		"\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\7\3\2\2\2ki\3\2\2\2lo\t\2\2\2mp"+
		"\5\n\6\2np\5\f\7\2om\3\2\2\2on\3\2\2\2pq\3\2\2\2qr\7>\2\2r\t\3\2\2\2s"+
		"t\5\20\t\2tu\7?\2\2uv\5N(\2v\13\3\2\2\2wx\t\3\2\2xy\5\16\b\2yz\5\30\r"+
		"\2z\r\3\2\2\2{|\7=\2\2|}\t\3\2\2}~\5\16\b\2~\177\5\30\r\2\177\u0080\7"+
		"=\2\2\u0080\u0086\3\2\2\2\u0081\u0082\7?\2\2\u0082\u0083\5N(\2\u0083\u0084"+
		"\7*\2\2\u0084\u0086\3\2\2\2\u0085{\3\2\2\2\u0085\u0081\3\2\2\2\u0086\17"+
		"\3\2\2\2\u0087\u008c\t\3\2\2\u0088\u0089\7=\2\2\u0089\u008b\t\3\2\2\u008a"+
		"\u0088\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2\u008c\u008d\3\2"+
		"\2\2\u008d\21\3\2\2\2\u008e\u008c\3\2\2\2\u008f\u0090\t\3\2\2\u0090\u0092"+
		"\7\65\2\2\u0091\u0093\5\24\13\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2"+
		"\2\u0093\u0094\3\2\2\2\u0094\u0095\7\66\2\2\u0095\u00a2\5H%\2\u0096\u0097"+
		"\7\37\2\2\u0097\u0099\7\65\2\2\u0098\u009a\5\24\13\2\u0099\u0098\3\2\2"+
		"\2\u0099\u009a\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c\7\66\2\2\u009c"+
		"\u00a2\5H%\2\u009d\u009e\7 \2\2\u009e\u009f\7\65\2\2\u009f\u00a0\7\66"+
		"\2\2\u00a0\u00a2\5H%\2\u00a1\u008f\3\2\2\2\u00a1\u0096\3\2\2\2\u00a1\u009d"+
		"\3\2\2\2\u00a2\23\3\2\2\2\u00a3\u00a4\5\20\t\2\u00a4\u00a5\7?\2\2\u00a5"+
		"\u00ad\5N(\2\u00a6\u00a7\7>\2\2\u00a7\u00a8\5\20\t\2\u00a8\u00a9\7?\2"+
		"\2\u00a9\u00aa\5N(\2\u00aa\u00ac\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ac\u00af"+
		"\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\25\3\2\2\2\u00af"+
		"\u00ad\3\2\2\2\u00b0\u00b5\5\30\r\2\u00b1\u00b2\7=\2\2\u00b2\u00b4\5\30"+
		"\r\2\u00b3\u00b1\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b5"+
		"\u00b6\3\2\2\2\u00b6\27\3\2\2\2\u00b7\u00b5\3\2\2\2\u00b8\u00b9\5\32\16"+
		"\2\u00b9\u00ba\t\4\2\2\u00ba\u00bb\5\32\16\2\u00bb\u00be\3\2\2\2\u00bc"+
		"\u00be\5\32\16\2\u00bd\u00b8\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\31\3\2"+
		"\2\2\u00bf\u00c0\5\34\17\2\u00c0\u00c1\t\5\2\2\u00c1\u00c2\5\34\17\2\u00c2"+
		"\u00c5\3\2\2\2\u00c3\u00c5\5\34\17\2\u00c4\u00bf\3\2\2\2\u00c4\u00c3\3"+
		"\2\2\2\u00c5\33\3\2\2\2\u00c6\u00c7\5\36\20\2\u00c7\u00c8\t\6\2\2\u00c8"+
		"\u00c9\5\34\17\2\u00c9\u00cc\3\2\2\2\u00ca\u00cc\5\36\20\2\u00cb\u00c6"+
		"\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\35\3\2\2\2\u00cd\u00ce\5 \21\2\u00ce"+
		"\u00cf\t\7\2\2\u00cf\u00d0\5\36\20\2\u00d0\u00d3\3\2\2\2\u00d1\u00d3\5"+
		" \21\2\u00d2\u00cd\3\2\2\2\u00d2\u00d1\3\2\2\2\u00d3\37\3\2\2\2\u00d4"+
		"\u00d5\5\"\22\2\u00d5\u00d6\t\b\2\2\u00d6\u00d7\5 \21\2\u00d7\u00da\3"+
		"\2\2\2\u00d8\u00da\5\"\22\2\u00d9\u00d4\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da"+
		"!\3\2\2\2\u00db\u00dc\7\'\2\2\u00dc\u00df\5$\23\2\u00dd\u00df\5$\23\2"+
		"\u00de\u00db\3\2\2\2\u00de\u00dd\3\2\2\2\u00df#\3\2\2\2\u00e0\u00e1\7"+
		"#\2\2\u00e1\u00e4\5&\24\2\u00e2\u00e4\5&\24\2\u00e3\u00e0\3\2\2\2\u00e3"+
		"\u00e2\3\2\2\2\u00e4%\3\2\2\2\u00e5\u00e6\5*\26\2\u00e6\u00e7\5(\25\2"+
		"\u00e7\u00ea\3\2\2\2\u00e8\u00ea\5*\26\2\u00e9\u00e5\3\2\2\2\u00e9\u00e8"+
		"\3\2\2\2\u00ea\'\3\2\2\2\u00eb\u00ec\79\2\2\u00ec\u00ed\5\30\r\2\u00ed"+
		"\u00ef\7:\2\2\u00ee\u00f0\5(\25\2\u00ef\u00ee\3\2\2\2\u00ef\u00f0\3\2"+
		"\2\2\u00f0)\3\2\2\2\u00f1\u00f4\5,\27\2\u00f2\u00f4\7\36\2\2\u00f3\u00f1"+
		"\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f6\7<\2\2\u00f6"+
		"\u0103\7A\2\2\u00f7\u00fa\5,\27\2\u00f8\u00fa\7\36\2\2\u00f9\u00f7\3\2"+
		"\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\7<\2\2\u00fc"+
		"\u00fd\7A\2\2\u00fd\u00fe\7\65\2\2\u00fe\u00ff\5\26\f\2\u00ff\u0100\7"+
		"\66\2\2\u0100\u0103\3\2\2\2\u0101\u0103\5,\27\2\u0102\u00f3\3\2\2\2\u0102"+
		"\u00f9\3\2\2\2\u0102\u0101\3\2\2\2\u0103+\3\2\2\2\u0104\u0105\7A\2\2\u0105"+
		"\u010e\t\t\2\2\u0106\u0107\7A\2\2\u0107\u0108\t\t\2\2\u0108\u0109\7\65"+
		"\2\2\u0109\u010a\5\26\f\2\u010a\u010b\7\66\2\2\u010b\u010e\3\2\2\2\u010c"+
		"\u010e\5.\30\2\u010d\u0104\3\2\2\2\u010d\u0106\3\2\2\2\u010d\u010c\3\2"+
		"\2\2\u010e-\3\2\2\2\u010f\u0112\5R*\2\u0110\u0112\5\60\31\2\u0111\u010f"+
		"\3\2\2\2\u0111\u0110\3\2\2\2\u0112/\3\2\2\2\u0113\u0114\7\65\2\2\u0114"+
		"\u0115\5\30\r\2\u0115\u0116\7\66\2\2\u0116\u0119\3\2\2\2\u0117\u0119\5"+
		"\62\32\2\u0118\u0113\3\2\2\2\u0118\u0117\3\2\2\2\u0119\61\3\2\2\2\u011a"+
		"\u011e\7\4\2\2\u011b\u011e\7A\2\2\u011c\u011e\5\64\33\2\u011d\u011a\3"+
		"\2\2\2\u011d\u011b\3\2\2\2\u011d\u011c\3\2\2\2\u011e\63\3\2\2\2\u011f"+
		"\u0120\7A\2\2\u0120\u0122\7\65\2\2\u0121\u0123\5\26\f\2\u0122\u0121\3"+
		"\2\2\2\u0122\u0123\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\7\66\2\2\u0125"+
		"\65\3\2\2\2\u0126\u012f\58\35\2\u0127\u012f\5:\36\2\u0128\u012f\5<\37"+
		"\2\u0129\u012f\5> \2\u012a\u012f\5@!\2\u012b\u012f\5B\"\2\u012c\u012f"+
		"\5D#\2\u012d\u012f\5F$\2\u012e\u0126\3\2\2\2\u012e\u0127\3\2\2\2\u012e"+
		"\u0128\3\2\2\2\u012e\u0129\3\2\2\2\u012e\u012a\3\2\2\2\u012e\u012b\3\2"+
		"\2\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2\2\u012f\67\3\2\2\2\u0130\u0131"+
		"\7\35\2\2\u0131\u0136\7A\2\2\u0132\u0133\7=\2\2\u0133\u0135\7A\2\2\u0134"+
		"\u0132\3\2\2\2\u0135\u0138\3\2\2\2\u0136\u0134\3\2\2\2\u0136\u0137\3\2"+
		"\2\2\u0137\u0143\3\2\2\2\u0138\u0136\3\2\2\2\u0139\u013a\7\34\2\2\u013a"+
		"\u013f\7A\2\2\u013b\u013c\7=\2\2\u013c\u013e\7A\2\2\u013d\u013b\3\2\2"+
		"\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3\2\2\2\u0140\u0143"+
		"\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0130\3\2\2\2\u0142\u0139\3\2\2\2\u0143"+
		"9\3\2\2\2\u0144\u0145\7A\2\2\u0145\u0146\7*\2\2\u0146\u0147\5\30\r\2\u0147"+
		"\u0148\7>\2\2\u0148;\3\2\2\2\u0149\u014a\7\r\2\2\u014a\u014b\7\65\2\2"+
		"\u014b\u014c\5\30\r\2\u014c\u014d\7\66\2\2\u014d\u0156\5H%\2\u014e\u014f"+
		"\7\16\2\2\u014f\u0150\7\65\2\2\u0150\u0151\5\30\r\2\u0151\u0152\7\66\2"+
		"\2\u0152\u0153\5H%\2\u0153\u0155\3\2\2\2\u0154\u014e\3\2\2\2\u0155\u0158"+
		"\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u015b\3\2\2\2\u0158"+
		"\u0156\3\2\2\2\u0159\u015a\7\17\2\2\u015a\u015c\5H%\2\u015b\u0159\3\2"+
		"\2\2\u015b\u015c\3\2\2\2\u015c=\3\2\2\2\u015d\u015e\7\20\2\2\u015e\u015f"+
		"\7\65\2\2\u015f\u0160\7\24\2\2\u0160\u0161\5\30\r\2\u0161\u0162\7;\2\2"+
		"\u0162\u0168\5\30\r\2\u0163\u0164\79\2\2\u0164\u0165\7!\2\2\u0165\u0166"+
		"\5\30\r\2\u0166\u0167\7:\2\2\u0167\u0169\3\2\2\2\u0168\u0163\3\2\2\2\u0168"+
		"\u0169\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b\5H%\2\u016b?\3\2\2\2\u016c"+
		"\u016d\7\13\2\2\u016d\u016e\7>\2\2\u016eA\3\2\2\2\u016f\u0170\7\f\2\2"+
		"\u0170\u0171\7>\2\2\u0171C\3\2\2\2\u0172\u0174\7\31\2\2\u0173\u0175\5"+
		"\30\r\2\u0174\u0173\3\2\2\2\u0174\u0175\3\2\2\2\u0175\u0176\3\2\2\2\u0176"+
		"\u0177\7>\2\2\u0177E\3\2\2\2\u0178\u0179\7>\2\2\u0179G\3\2\2\2\u017a\u017c"+
		"\7\67\2\2\u017b\u017d\5\66\34\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2"+
		"\2\u017e\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\3\2\2\2\u0180\u0181"+
		"\78\2\2\u0181I\3\2\2\2\u0182\u0183\7\23\2\2\u0183\u018c\7\65\2\2\u0184"+
		"\u0189\7\4\2\2\u0185\u0186\7=\2\2\u0186\u0188\7\4\2\2\u0187\u0185\3\2"+
		"\2\2\u0188\u018b\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a"+
		"\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018c\u0184\3\2\2\2\u018c\u018d\3\2"+
		"\2\2\u018d\u018e\3\2\2\2\u018e\u018f\7\66\2\2\u018fK\3\2\2\2\u0190\u0191"+
		"\7\23\2\2\u0191\u0197\7\65\2\2\u0192\u0193\5J&\2\u0193\u0194\7=\2\2\u0194"+
		"\u0195\5J&\2\u0195\u0198\3\2\2\2\u0196\u0198\5L\'\2\u0197\u0192\3\2\2"+
		"\2\u0197\u0196\3\2\2\2\u0198\u0199\3\2\2\2\u0199\u019a\7\66\2\2\u019a"+
		"M\3\2\2\2\u019b\u019f\7\n\2\2\u019c\u019f\5P)\2\u019d\u019f\5R*\2\u019e"+
		"\u019b\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019d\3\2\2\2\u019fO\3\2\2\2"+
		"\u01a0\u01a1\7\23\2\2\u01a1\u01a4\79\2\2\u01a2\u01a5\7\n\2\2\u01a3\u01a5"+
		"\5P)\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6"+
		"\u01a7\7=\2\2\u01a7\u01a8\7\4\2\2\u01a8\u01a9\7:\2\2\u01a9Q\3\2\2\2\u01aa"+
		"\u01ab\7\64\2\2\u01ab\u01ac\7A\2\2\u01ac\u01ae\7\65\2\2\u01ad\u01af\5"+
		"\26\f\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0"+
		"\u01b1\7\66\2\2\u01b1S\3\2\2\2.W_gio\u0085\u008c\u0092\u0099\u00a1\u00ad"+
		"\u00b5\u00bd\u00c4\u00cb\u00d2\u00d9\u00de\u00e3\u00e9\u00ef\u00f3\u00f9"+
		"\u0102\u010d\u0111\u0118\u011d\u0122\u012e\u0136\u013f\u0142\u0156\u015b"+
		"\u0168\u0174\u017e\u0189\u018c\u0197\u019e\u01a4\u01ae";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}