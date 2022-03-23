// Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/Assignment 1/src/main/d96/parser/D96.g4 by ANTLR 4.8

from lexererr import *

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class D96Lexer extends Lexer {
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
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"BLOCK_COMMENT", "CMT", "LITERAL", "INT_LIT", "OCTAL", "DECIMAL", "HEX", 
			"BINARY", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", "DIGIT", "EXPONENT", "PRIMITIVE_TYPE", 
			"BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
			"ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
			"CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "BY", "ADD", 
			"SUB_OP", "MUL", "DIV", "PRCNT", "NOT", "AND", "OR", "EQ", "ASSIGN", 
			"NOT_EQ", "LESS", "LESS_EQ", "GREAT", "GREAT_EQ", "EQ_STR", "CONCAT_STR", 
			"STATIC_ACC", "OBJ_CREATE", "LB", "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", 
			"DOT", "CM", "SEMI", "CL", "DOUBLEQUOTE", "ID", "STATIC_ID", "WS", "ERROR_CHAR", 
			"UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL"
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


	public D96Lexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "D96.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 2:
			LITERAL_action((RuleContext)_localctx, actionIndex);
			break;
		case 71:
			ERROR_CHAR_action((RuleContext)_localctx, actionIndex);
			break;
		case 72:
			UNCLOSE_STRING_action((RuleContext)_localctx, actionIndex);
			break;
		case 73:
			ILLEGAL_ESCAPE_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void LITERAL_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.text = self.text.replace('_','')
			break;
		case 1:
			self.text = self.text.replace('_','')
			break;
		case 2:
			self.text = self.text[1:-1]
			break;
		}
	}
	private void ERROR_CHAR_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
				
					raise ErrorToken(self.text)	
				
			break;
		}
	}
	private void UNCLOSE_STRING_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:

					raise UncloseString(self.text[1:])
				
			break;
		}
	}
	private void ILLEGAL_ESCAPE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:

					raise IllegalEscape(self.text[1:])
				
			break;
		}
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F\u0238\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\4<\t<\4=\t="+
		"\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I"+
		"\tI\4J\tJ\4K\tK\4L\tL\4M\tM\4N\tN\3\2\3\2\7\2\u00a0\n\2\f\2\16\2\u00a3"+
		"\13\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4"+
		"\3\4\5\4\u00b6\n\4\3\5\3\5\3\5\3\5\5\5\u00bc\n\5\3\6\3\6\3\6\5\6\u00c1"+
		"\n\6\6\6\u00c3\n\6\r\6\16\6\u00c4\3\7\3\7\5\7\u00c9\n\7\6\7\u00cb\n\7"+
		"\r\7\16\7\u00cc\3\b\3\b\3\b\3\b\5\b\u00d3\n\b\6\b\u00d5\n\b\r\b\16\b\u00d6"+
		"\3\t\3\t\3\t\3\t\5\t\u00dd\n\t\6\t\u00df\n\t\r\t\16\t\u00e0\3\n\5\n\u00e4"+
		"\n\n\3\n\3\n\7\n\u00e8\n\n\f\n\16\n\u00eb\13\n\3\n\3\n\3\n\3\n\3\n\7\n"+
		"\u00f2\n\n\f\n\16\n\u00f5\13\n\5\n\u00f7\n\n\3\n\3\n\3\n\3\n\3\n\7\n\u00fe"+
		"\n\n\f\n\16\n\u0101\13\n\3\n\5\n\u0104\n\n\5\n\u0106\n\n\3\13\3\13\5\13"+
		"\u010a\n\13\3\f\3\f\3\f\3\f\7\f\u0110\n\f\f\f\16\f\u0113\13\f\3\f\3\f"+
		"\3\r\3\r\3\16\3\16\3\16\5\16\u011c\n\16\3\16\6\16\u011f\n\16\r\16\16\16"+
		"\u0120\3\17\3\17\3\17\3\17\5\17\u0127\n\17\3\20\3\20\3\20\3\20\3\20\3"+
		"\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3"+
		"\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3"+
		"\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3"+
		"\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3"+
		"\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3"+
		"\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\""+
		"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3"+
		"%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-"+
		"\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3\63"+
		"\3\63\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\38\3"+
		"8\38\39\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3"+
		"B\3B\3C\3C\3D\3D\3E\3E\3F\3F\7F\u0202\nF\fF\16F\u0205\13F\3G\3G\6G\u0209"+
		"\nG\rG\16G\u020a\3H\6H\u020e\nH\rH\16H\u020f\3H\3H\3I\3I\3I\3J\3J\7J\u0219"+
		"\nJ\fJ\16J\u021c\13J\3J\5J\u021f\nJ\3J\3J\3K\3K\7K\u0225\nK\fK\16K\u0228"+
		"\13K\3K\3K\3K\3L\3L\5L\u022f\nL\3M\3M\3M\3N\3N\3N\5N\u0237\nN\3\u00a1"+
		"\2O\3\3\5\2\7\4\t\5\13\2\r\2\17\2\21\2\23\6\25\7\27\b\31\t\33\2\35\n\37"+
		"\13!\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32"+
		"?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63"+
		"q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA"+
		"\u008dB\u008fC\u0091D\u0093E\u0095F\u0097\2\u0099\2\u009b\2\3\2\21\3\2"+
		"\62\62\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\4\2\62\63aa\3\2\62;\4\2GGgg\5"+
		"\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\7\2\n"+
		"\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u0255\2\3\3\2\2\2\2\7\3\2\2"+
		"\2\2\t\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\35"+
		"\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)"+
		"\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2"+
		"\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2"+
		"A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3"+
		"\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2"+
		"\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2"+
		"g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3"+
		"\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3"+
		"\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2"+
		"\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091"+
		"\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u009d\3\2\2\2\5\u00a8\3\2\2"+
		"\2\7\u00b5\3\2\2\2\t\u00bb\3\2\2\2\13\u00bd\3\2\2\2\r\u00ca\3\2\2\2\17"+
		"\u00ce\3\2\2\2\21\u00d8\3\2\2\2\23\u0105\3\2\2\2\25\u0109\3\2\2\2\27\u010b"+
		"\3\2\2\2\31\u0116\3\2\2\2\33\u0118\3\2\2\2\35\u0126\3\2\2\2\37\u0128\3"+
		"\2\2\2!\u012e\3\2\2\2#\u0137\3\2\2\2%\u013a\3\2\2\2\'\u0141\3\2\2\2)\u0146"+
		"\3\2\2\2+\u014e\3\2\2\2-\u0153\3\2\2\2/\u0159\3\2\2\2\61\u015f\3\2\2\2"+
		"\63\u0162\3\2\2\2\65\u0166\3\2\2\2\67\u016c\3\2\2\29\u0174\3\2\2\2;\u017b"+
		"\3\2\2\2=\u0182\3\2\2\2?\u0187\3\2\2\2A\u018d\3\2\2\2C\u0191\3\2\2\2E"+
		"\u0195\3\2\2\2G\u019a\3\2\2\2I\u01a6\3\2\2\2K\u01b1\3\2\2\2M\u01b4\3\2"+
		"\2\2O\u01b6\3\2\2\2Q\u01b8\3\2\2\2S\u01ba\3\2\2\2U\u01bc\3\2\2\2W\u01be"+
		"\3\2\2\2Y\u01c0\3\2\2\2[\u01c3\3\2\2\2]\u01c6\3\2\2\2_\u01c9\3\2\2\2a"+
		"\u01cb\3\2\2\2c\u01ce\3\2\2\2e\u01d0\3\2\2\2g\u01d3\3\2\2\2i\u01d5\3\2"+
		"\2\2k\u01d8\3\2\2\2m\u01dc\3\2\2\2o\u01df\3\2\2\2q\u01e2\3\2\2\2s\u01e6"+
		"\3\2\2\2u\u01e8\3\2\2\2w\u01ea\3\2\2\2y\u01ec\3\2\2\2{\u01ee\3\2\2\2}"+
		"\u01f0\3\2\2\2\177\u01f2\3\2\2\2\u0081\u01f5\3\2\2\2\u0083\u01f7\3\2\2"+
		"\2\u0085\u01f9\3\2\2\2\u0087\u01fb\3\2\2\2\u0089\u01fd\3\2\2\2\u008b\u01ff"+
		"\3\2\2\2\u008d\u0206\3\2\2\2\u008f\u020d\3\2\2\2\u0091\u0213\3\2\2\2\u0093"+
		"\u0216\3\2\2\2\u0095\u0222\3\2\2\2\u0097\u022e\3\2\2\2\u0099\u0230\3\2"+
		"\2\2\u009b\u0236\3\2\2\2\u009d\u00a1\5\5\3\2\u009e\u00a0\13\2\2\2\u009f"+
		"\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a1\u009f\3\2"+
		"\2\2\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5\5\3\2\u00a5"+
		"\u00a6\3\2\2\2\u00a6\u00a7\b\2\2\2\u00a7\4\3\2\2\2\u00a8\u00a9\7%\2\2"+
		"\u00a9\u00aa\7%\2\2\u00aa\6\3\2\2\2\u00ab\u00ac\5\23\n\2\u00ac\u00ad\b"+
		"\4\3\2\u00ad\u00b6\3\2\2\2\u00ae\u00af\5\t\5\2\u00af\u00b0\b\4\4\2\u00b0"+
		"\u00b6\3\2\2\2\u00b1\u00b6\5\25\13\2\u00b2\u00b3\5\27\f\2\u00b3\u00b4"+
		"\b\4\5\2\u00b4\u00b6\3\2\2\2\u00b5\u00ab\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5"+
		"\u00b1\3\2\2\2\u00b5\u00b2\3\2\2\2\u00b6\b\3\2\2\2\u00b7\u00bc\5\13\6"+
		"\2\u00b8\u00bc\5\r\7\2\u00b9\u00bc\5\17\b\2\u00ba\u00bc\5\21\t\2\u00bb"+
		"\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2"+
		"\2\2\u00bc\n\3\2\2\2\u00bd\u00c2\t\2\2\2\u00be\u00c0\t\3\2\2\u00bf\u00c1"+
		"\7a\2\2\u00c0\u00bf\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c3\3\2\2\2\u00c2"+
		"\u00be\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2"+
		"\2\2\u00c5\f\3\2\2\2\u00c6\u00c8\5\31\r\2\u00c7\u00c9\7a\2\2\u00c8\u00c7"+
		"\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00cb\3\2\2\2\u00ca\u00c6\3\2\2\2\u00cb"+
		"\u00cc\3\2\2\2\u00cc\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\16\3\2\2"+
		"\2\u00ce\u00cf\t\2\2\2\u00cf\u00d4\t\4\2\2\u00d0\u00d2\t\5\2\2\u00d1\u00d3"+
		"\7a\2\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\u00d5\3\2\2\2\u00d4"+
		"\u00d0\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2"+
		"\2\2\u00d7\20\3\2\2\2\u00d8\u00d9\t\2\2\2\u00d9\u00de\t\6\2\2\u00da\u00dc"+
		"\t\7\2\2\u00db\u00dd\7a\2\2\u00dc\u00db\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd"+
		"\u00df\3\2\2\2\u00de\u00da\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\u00de\3\2"+
		"\2\2\u00e0\u00e1\3\2\2\2\u00e1\22\3\2\2\2\u00e2\u00e4\5\r\7\2\u00e3\u00e2"+
		"\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e9\5\u0081A"+
		"\2\u00e6\u00e8\5\31\r\2\u00e7\u00e6\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9"+
		"\u00e7\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3\2"+
		"\2\2\u00ec\u00ed\5\33\16\2\u00ed\u0106\3\2\2\2\u00ee\u00f6\5\r\7\2\u00ef"+
		"\u00f3\5\u0081A\2\u00f0\u00f2\5\31\r\2\u00f1\u00f0\3\2\2\2\u00f2\u00f5"+
		"\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f3\u00f4\3\2\2\2\u00f4\u00f7\3\2\2\2\u00f5"+
		"\u00f3\3\2\2\2\u00f6\u00ef\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2"+
		"\2\2\u00f8\u00f9\5\33\16\2\u00f9\u0106\3\2\2\2\u00fa\u00fb\5\r\7\2\u00fb"+
		"\u00ff\5\u0081A\2\u00fc\u00fe\5\31\r\2\u00fd\u00fc\3\2\2\2\u00fe\u0101"+
		"\3\2\2\2\u00ff\u00fd\3\2\2\2\u00ff\u0100\3\2\2\2\u0100\u0103\3\2\2\2\u0101"+
		"\u00ff\3\2\2\2\u0102\u0104\5\33\16\2\u0103\u0102\3\2\2\2\u0103\u0104\3"+
		"\2\2\2\u0104\u0106\3\2\2\2\u0105\u00e3\3\2\2\2\u0105\u00ee\3\2\2\2\u0105"+
		"\u00fa\3\2\2\2\u0106\24\3\2\2\2\u0107\u010a\5+\26\2\u0108\u010a\5-\27"+
		"\2\u0109\u0107\3\2\2\2\u0109\u0108\3\2\2\2\u010a\26\3\2\2\2\u010b\u0111"+
		"\5\u0089E\2\u010c\u0110\5\u0097L\2\u010d\u010e\7)\2\2\u010e\u0110\7$\2"+
		"\2\u010f\u010c\3\2\2\2\u010f\u010d\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u010f"+
		"\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114"+
		"\u0115\5\u0089E\2\u0115\30\3\2\2\2\u0116\u0117\t\b\2\2\u0117\32\3\2\2"+
		"\2\u0118\u011b\t\t\2\2\u0119\u011c\5M\'\2\u011a\u011c\5O(\2\u011b\u0119"+
		"\3\2\2\2\u011b\u011a\3\2\2\2\u011b\u011c\3\2\2\2\u011c\u011e\3\2\2\2\u011d"+
		"\u011f\5\31\r\2\u011e\u011d\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u011e\3"+
		"\2\2\2\u0120\u0121\3\2\2\2\u0121\34\3\2\2\2\u0122\u0127\5\63\32\2\u0123"+
		"\u0127\5\65\33\2\u0124\u0127\5\67\34\2\u0125\u0127\59\35\2\u0126\u0122"+
		"\3\2\2\2\u0126\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3\2\2\2\u0127"+
		"\36\3\2\2\2\u0128\u0129\7D\2\2\u0129\u012a\7t\2\2\u012a\u012b\7g\2\2\u012b"+
		"\u012c\7c\2\2\u012c\u012d\7m\2\2\u012d \3\2\2\2\u012e\u012f\7E\2\2\u012f"+
		"\u0130\7q\2\2\u0130\u0131\7p\2\2\u0131\u0132\7v\2\2\u0132\u0133\7k\2\2"+
		"\u0133\u0134\7p\2\2\u0134\u0135\7w\2\2\u0135\u0136\7g\2\2\u0136\"\3\2"+
		"\2\2\u0137\u0138\7K\2\2\u0138\u0139\7h\2\2\u0139$\3\2\2\2\u013a\u013b"+
		"\7G\2\2\u013b\u013c\7n\2\2\u013c\u013d\7u\2\2\u013d\u013e\7g\2\2\u013e"+
		"\u013f\7k\2\2\u013f\u0140\7h\2\2\u0140&\3\2\2\2\u0141\u0142\7G\2\2\u0142"+
		"\u0143\7n\2\2\u0143\u0144\7u\2\2\u0144\u0145\7g\2\2\u0145(\3\2\2\2\u0146"+
		"\u0147\7H\2\2\u0147\u0148\7q\2\2\u0148\u0149\7t\2\2\u0149\u014a\7g\2\2"+
		"\u014a\u014b\7c\2\2\u014b\u014c\7e\2\2\u014c\u014d\7j\2\2\u014d*\3\2\2"+
		"\2\u014e\u014f\7V\2\2\u014f\u0150\7t\2\2\u0150\u0151\7w\2\2\u0151\u0152"+
		"\7g\2\2\u0152,\3\2\2\2\u0153\u0154\7H\2\2\u0154\u0155\7c\2\2\u0155\u0156"+
		"\7n\2\2\u0156\u0157\7u\2\2\u0157\u0158\7g\2\2\u0158.\3\2\2\2\u0159\u015a"+
		"\7C\2\2\u015a\u015b\7t\2\2\u015b\u015c\7t\2\2\u015c\u015d\7c\2\2\u015d"+
		"\u015e\7{\2\2\u015e\60\3\2\2\2\u015f\u0160\7K\2\2\u0160\u0161\7p\2\2\u0161"+
		"\62\3\2\2\2\u0162\u0163\7K\2\2\u0163\u0164\7p\2\2\u0164\u0165\7v\2\2\u0165"+
		"\64\3\2\2\2\u0166\u0167\7H\2\2\u0167\u0168\7n\2\2\u0168\u0169\7q\2\2\u0169"+
		"\u016a\7c\2\2\u016a\u016b\7v\2\2\u016b\66\3\2\2\2\u016c\u016d\7D\2\2\u016d"+
		"\u016e\7q\2\2\u016e\u016f\7q\2\2\u016f\u0170\7n\2\2\u0170\u0171\7g\2\2"+
		"\u0171\u0172\7c\2\2\u0172\u0173\7p\2\2\u01738\3\2\2\2\u0174\u0175\7U\2"+
		"\2\u0175\u0176\7v\2\2\u0176\u0177\7t\2\2\u0177\u0178\7k\2\2\u0178\u0179"+
		"\7p\2\2\u0179\u017a\7i\2\2\u017a:\3\2\2\2\u017b\u017c\7T\2\2\u017c\u017d"+
		"\7g\2\2\u017d\u017e\7v\2\2\u017e\u017f\7w\2\2\u017f\u0180\7t\2\2\u0180"+
		"\u0181\7p\2\2\u0181<\3\2\2\2\u0182\u0183\7P\2\2\u0183\u0184\7w\2\2\u0184"+
		"\u0185\7n\2\2\u0185\u0186\7n\2\2\u0186>\3\2\2\2\u0187\u0188\7E\2\2\u0188"+
		"\u0189\7n\2\2\u0189\u018a\7c\2\2\u018a\u018b\7u\2\2\u018b\u018c\7u\2\2"+
		"\u018c@\3\2\2\2\u018d\u018e\7X\2\2\u018e\u018f\7c\2\2\u018f\u0190\7n\2"+
		"\2\u0190B\3\2\2\2\u0191\u0192\7X\2\2\u0192\u0193\7c\2\2\u0193\u0194\7"+
		"t\2\2\u0194D\3\2\2\2\u0195\u0196\7U\2\2\u0196\u0197\7g\2\2\u0197\u0198"+
		"\7n\2\2\u0198\u0199\7h\2\2\u0199F\3\2\2\2\u019a\u019b\7E\2\2\u019b\u019c"+
		"\7q\2\2\u019c\u019d\7p\2\2\u019d\u019e\7u\2\2\u019e\u019f\7v\2\2\u019f"+
		"\u01a0\7t\2\2\u01a0\u01a1\7w\2\2\u01a1\u01a2\7e\2\2\u01a2\u01a3\7v\2\2"+
		"\u01a3\u01a4\7q\2\2\u01a4\u01a5\7t\2\2\u01a5H\3\2\2\2\u01a6\u01a7\7F\2"+
		"\2\u01a7\u01a8\7g\2\2\u01a8\u01a9\7u\2\2\u01a9\u01aa\7v\2\2\u01aa\u01ab"+
		"\7t\2\2\u01ab\u01ac\7w\2\2\u01ac\u01ad\7e\2\2\u01ad\u01ae\7v\2\2\u01ae"+
		"\u01af\7q\2\2\u01af\u01b0\7t\2\2\u01b0J\3\2\2\2\u01b1\u01b2\7D\2\2\u01b2"+
		"\u01b3\7{\2\2\u01b3L\3\2\2\2\u01b4\u01b5\7-\2\2\u01b5N\3\2\2\2\u01b6\u01b7"+
		"\7/\2\2\u01b7P\3\2\2\2\u01b8\u01b9\7,\2\2\u01b9R\3\2\2\2\u01ba\u01bb\7"+
		"\61\2\2\u01bbT\3\2\2\2\u01bc\u01bd\7\'\2\2\u01bdV\3\2\2\2\u01be\u01bf"+
		"\7#\2\2\u01bfX\3\2\2\2\u01c0\u01c1\7(\2\2\u01c1\u01c2\7(\2\2\u01c2Z\3"+
		"\2\2\2\u01c3\u01c4\7~\2\2\u01c4\u01c5\7~\2\2\u01c5\\\3\2\2\2\u01c6\u01c7"+
		"\7?\2\2\u01c7\u01c8\7?\2\2\u01c8^\3\2\2\2\u01c9\u01ca\7?\2\2\u01ca`\3"+
		"\2\2\2\u01cb\u01cc\7#\2\2\u01cc\u01cd\7?\2\2\u01cdb\3\2\2\2\u01ce\u01cf"+
		"\7>\2\2\u01cfd\3\2\2\2\u01d0\u01d1\7>\2\2\u01d1\u01d2\7?\2\2\u01d2f\3"+
		"\2\2\2\u01d3\u01d4\7@\2\2\u01d4h\3\2\2\2\u01d5\u01d6\7@\2\2\u01d6\u01d7"+
		"\7?\2\2\u01d7j\3\2\2\2\u01d8\u01d9\7?\2\2\u01d9\u01da\7?\2\2\u01da\u01db"+
		"\7\60\2\2\u01dbl\3\2\2\2\u01dc\u01dd\7-\2\2\u01dd\u01de\7\60\2\2\u01de"+
		"n\3\2\2\2\u01df\u01e0\7<\2\2\u01e0\u01e1\7<\2\2\u01e1p\3\2\2\2\u01e2\u01e3"+
		"\7P\2\2\u01e3\u01e4\7g\2\2\u01e4\u01e5\7y\2\2\u01e5r\3\2\2\2\u01e6\u01e7"+
		"\7*\2\2\u01e7t\3\2\2\2\u01e8\u01e9\7+\2\2\u01e9v\3\2\2\2\u01ea\u01eb\7"+
		"}\2\2\u01ebx\3\2\2\2\u01ec\u01ed\7\177\2\2\u01edz\3\2\2\2\u01ee\u01ef"+
		"\7]\2\2\u01ef|\3\2\2\2\u01f0\u01f1\7_\2\2\u01f1~\3\2\2\2\u01f2\u01f3\7"+
		"\60\2\2\u01f3\u01f4\7\60\2\2\u01f4\u0080\3\2\2\2\u01f5\u01f6\7\60\2\2"+
		"\u01f6\u0082\3\2\2\2\u01f7\u01f8\7.\2\2\u01f8\u0084\3\2\2\2\u01f9\u01fa"+
		"\7=\2\2\u01fa\u0086\3\2\2\2\u01fb\u01fc\7<\2\2\u01fc\u0088\3\2\2\2\u01fd"+
		"\u01fe\7$\2\2\u01fe\u008a\3\2\2\2\u01ff\u0203\t\n\2\2\u0200\u0202\t\13"+
		"\2\2\u0201\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203"+
		"\u0204\3\2\2\2\u0204\u008c\3\2\2\2\u0205\u0203\3\2\2\2\u0206\u0208\7&"+
		"\2\2\u0207\u0209\t\13\2\2\u0208\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020a"+
		"\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u008e\3\2\2\2\u020c\u020e\t\f"+
		"\2\2\u020d\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u020d\3\2\2\2\u020f"+
		"\u0210\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\bH\2\2\u0212\u0090\3\2"+
		"\2\2\u0213\u0214\13\2\2\2\u0214\u0215\bI\6\2\u0215\u0092\3\2\2\2\u0216"+
		"\u021a\7$\2\2\u0217\u0219\5\u0097L\2\u0218\u0217\3\2\2\2\u0219\u021c\3"+
		"\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021e\3\2\2\2\u021c"+
		"\u021a\3\2\2\2\u021d\u021f\t\r\2\2\u021e\u021d\3\2\2\2\u021f\u0220\3\2"+
		"\2\2\u0220\u0221\bJ\7\2\u0221\u0094\3\2\2\2\u0222\u0226\7$\2\2\u0223\u0225"+
		"\5\u0097L\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2"+
		"\2\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0226\3\2\2\2\u0229\u022a"+
		"\5\u009bN\2\u022a\u022b\bK\b\2\u022b\u0096\3\2\2\2\u022c\u022f\n\16\2"+
		"\2\u022d\u022f\5\u0099M\2\u022e\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f"+
		"\u0098\3\2\2\2\u0230\u0231\7^\2\2\u0231\u0232\t\17\2\2\u0232\u009a\3\2"+
		"\2\2\u0233\u0234\7^\2\2\u0234\u0237\n\17\2\2\u0235\u0237\n\20\2\2\u0236"+
		"\u0233\3\2\2\2\u0236\u0235\3\2\2\2\u0237\u009c\3\2\2\2#\2\u00a1\u00b5"+
		"\u00bb\u00c0\u00c4\u00c8\u00cc\u00d2\u00d6\u00dc\u00e0\u00e3\u00e9\u00f3"+
		"\u00f6\u00ff\u0103\u0105\u0109\u010f\u0111\u011b\u0120\u0126\u0203\u020a"+
		"\u020f\u021a\u021e\u0226\u022e\u0236\t\b\2\2\3\4\2\3\4\3\3\4\4\3I\5\3"+
		"J\6\3K\7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}