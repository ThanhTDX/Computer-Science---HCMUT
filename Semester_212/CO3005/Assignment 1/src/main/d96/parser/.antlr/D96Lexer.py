# Generated from /home/thanh792001/Computer-Science---HCMUT/Semester_212/CO3005/Assignment 1/src/main/d96/parser/D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\3\2\3\2\7\2\u00a0\n\2\f\2\16\2\u00a3\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u00b6\n\4\3\5\3\5\3\5\3\5\5\5\u00bc")
        buf.write("\n\5\3\6\3\6\3\6\3\6\5\6\u00c2\n\6\3\6\7\6\u00c5\n\6\f")
        buf.write("\6\16\6\u00c8\13\6\5\6\u00ca\n\6\3\7\3\7\3\7\5\7\u00cf")
        buf.write("\n\7\3\7\7\7\u00d2\n\7\f\7\16\7\u00d5\13\7\5\7\u00d7\n")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\5\b\u00de\n\b\3\b\7\b\u00e1\n\b")
        buf.write("\f\b\16\b\u00e4\13\b\5\b\u00e6\n\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00ed\n\t\3\t\7\t\u00f0\n\t\f\t\16\t\u00f3\13\t\5")
        buf.write("\t\u00f5\n\t\3\n\5\n\u00f8\n\n\3\n\3\n\7\n\u00fc\n\n\f")
        buf.write("\n\16\n\u00ff\13\n\3\n\3\n\3\n\3\n\3\n\7\n\u0106\n\n\f")
        buf.write("\n\16\n\u0109\13\n\5\n\u010b\n\n\3\n\3\n\3\n\3\n\3\n\7")
        buf.write("\n\u0112\n\n\f\n\16\n\u0115\13\n\3\n\5\n\u0118\n\n\5\n")
        buf.write("\u011a\n\n\3\13\3\13\5\13\u011e\n\13\3\f\3\f\3\f\3\f\7")
        buf.write("\f\u0124\n\f\f\f\16\f\u0127\13\f\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\16\5\16\u0130\n\16\3\16\6\16\u0133\n\16\r\16\16")
        buf.write("\16\u0134\3\17\3\17\3\17\3\17\5\17\u013b\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\39\39\39\3:\3:\3;\3;\3<")
        buf.write("\3<\3=\3=\3>\3>\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3")
        buf.write("D\3E\3E\3F\3F\7F\u0216\nF\fF\16F\u0219\13F\3G\3G\6G\u021d")
        buf.write("\nG\rG\16G\u021e\3H\6H\u0222\nH\rH\16H\u0223\3H\3H\3I")
        buf.write("\3I\3I\3J\3J\7J\u022d\nJ\fJ\16J\u0230\13J\3J\5J\u0233")
        buf.write("\nJ\3J\3J\3K\3K\7K\u0239\nK\fK\16K\u023c\13K\3K\3K\3K")
        buf.write("\3L\3L\5L\u0243\nL\3M\3M\3M\3N\3N\3N\5N\u024b\nN\3\u00a1")
        buf.write("\2O\3\3\5\2\7\4\t\5\13\2\r\2\17\2\21\2\23\6\25\7\27\b")
        buf.write("\31\t\33\2\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61")
        buf.write("\24\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37")
        buf.write("I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64")
        buf.write("s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\u0093E\u0095F\u0097\2\u0099")
        buf.write("\2\u009b\2\3\2\23\3\2\629\3\2\639\3\2\62;\3\2\63;\4\2")
        buf.write("ZZzz\4\2\62;CH\4\2\63;CH\4\2DDdd\3\2\62\63\4\2GGgg\5\2")
        buf.write("C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\7\3\n\f\16\17")
        buf.write("$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^\2")
        buf.write("\u026d\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\35\3\2\2\2")
        buf.write("\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2")
        buf.write("\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2")
        buf.write("\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2")
        buf.write("\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b")
        buf.write("\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\3\u009d\3\2\2\2\5\u00a8")
        buf.write("\3\2\2\2\7\u00b5\3\2\2\2\t\u00bb\3\2\2\2\13\u00bd\3\2")
        buf.write("\2\2\r\u00d6\3\2\2\2\17\u00d8\3\2\2\2\21\u00e7\3\2\2\2")
        buf.write("\23\u0119\3\2\2\2\25\u011d\3\2\2\2\27\u011f\3\2\2\2\31")
        buf.write("\u012a\3\2\2\2\33\u012c\3\2\2\2\35\u013a\3\2\2\2\37\u013c")
        buf.write("\3\2\2\2!\u0142\3\2\2\2#\u014b\3\2\2\2%\u014e\3\2\2\2")
        buf.write("\'\u0155\3\2\2\2)\u015a\3\2\2\2+\u0162\3\2\2\2-\u0167")
        buf.write("\3\2\2\2/\u016d\3\2\2\2\61\u0173\3\2\2\2\63\u0176\3\2")
        buf.write("\2\2\65\u017a\3\2\2\2\67\u0180\3\2\2\29\u0188\3\2\2\2")
        buf.write(";\u018f\3\2\2\2=\u0196\3\2\2\2?\u019b\3\2\2\2A\u01a1\3")
        buf.write("\2\2\2C\u01a5\3\2\2\2E\u01a9\3\2\2\2G\u01ae\3\2\2\2I\u01ba")
        buf.write("\3\2\2\2K\u01c5\3\2\2\2M\u01c9\3\2\2\2O\u01cc\3\2\2\2")
        buf.write("Q\u01ce\3\2\2\2S\u01d0\3\2\2\2U\u01d2\3\2\2\2W\u01d4\3")
        buf.write("\2\2\2Y\u01d6\3\2\2\2[\u01d8\3\2\2\2]\u01db\3\2\2\2_\u01de")
        buf.write("\3\2\2\2a\u01e1\3\2\2\2c\u01e3\3\2\2\2e\u01e6\3\2\2\2")
        buf.write("g\u01e8\3\2\2\2i\u01eb\3\2\2\2k\u01ed\3\2\2\2m\u01f0\3")
        buf.write("\2\2\2o\u01f4\3\2\2\2q\u01f7\3\2\2\2s\u01fa\3\2\2\2u\u01fc")
        buf.write("\3\2\2\2w\u01fe\3\2\2\2y\u0200\3\2\2\2{\u0202\3\2\2\2")
        buf.write("}\u0204\3\2\2\2\177\u0206\3\2\2\2\u0081\u0209\3\2\2\2")
        buf.write("\u0083\u020b\3\2\2\2\u0085\u020d\3\2\2\2\u0087\u020f\3")
        buf.write("\2\2\2\u0089\u0211\3\2\2\2\u008b\u0213\3\2\2\2\u008d\u021a")
        buf.write("\3\2\2\2\u008f\u0221\3\2\2\2\u0091\u0227\3\2\2\2\u0093")
        buf.write("\u022a\3\2\2\2\u0095\u0236\3\2\2\2\u0097\u0242\3\2\2\2")
        buf.write("\u0099\u0244\3\2\2\2\u009b\u024a\3\2\2\2\u009d\u00a1\5")
        buf.write("\5\3\2\u009e\u00a0\13\2\2\2\u009f\u009e\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a1\u009f\3\2\2\2")
        buf.write("\u00a2\u00a4\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a5\5")
        buf.write("\5\3\2\u00a5\u00a6\3\2\2\2\u00a6\u00a7\b\2\2\2\u00a7\4")
        buf.write("\3\2\2\2\u00a8\u00a9\7%\2\2\u00a9\u00aa\7%\2\2\u00aa\6")
        buf.write("\3\2\2\2\u00ab\u00ac\5\23\n\2\u00ac\u00ad\b\4\3\2\u00ad")
        buf.write("\u00b6\3\2\2\2\u00ae\u00af\5\t\5\2\u00af\u00b0\b\4\4\2")
        buf.write("\u00b0\u00b6\3\2\2\2\u00b1\u00b6\5\25\13\2\u00b2\u00b3")
        buf.write("\5\27\f\2\u00b3\u00b4\b\4\5\2\u00b4\u00b6\3\2\2\2\u00b5")
        buf.write("\u00ab\3\2\2\2\u00b5\u00ae\3\2\2\2\u00b5\u00b1\3\2\2\2")
        buf.write("\u00b5\u00b2\3\2\2\2\u00b6\b\3\2\2\2\u00b7\u00bc\5\13")
        buf.write("\6\2\u00b8\u00bc\5\r\7\2\u00b9\u00bc\5\17\b\2\u00ba\u00bc")
        buf.write("\5\21\t\2\u00bb\u00b7\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb")
        buf.write("\u00b9\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc\n\3\2\2\2\u00bd")
        buf.write("\u00c9\7\62\2\2\u00be\u00ca\t\2\2\2\u00bf\u00c6\t\3\2")
        buf.write("\2\u00c0\u00c2\7a\2\2\u00c1\u00c0\3\2\2\2\u00c1\u00c2")
        buf.write("\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c5\t\2\2\2\u00c4")
        buf.write("\u00c1\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00ca\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c9\u00be\3\2\2\2\u00c9\u00bf\3\2\2\2\u00ca\f")
        buf.write("\3\2\2\2\u00cb\u00d7\t\4\2\2\u00cc\u00d3\t\5\2\2\u00cd")
        buf.write("\u00cf\7a\2\2\u00ce\u00cd\3\2\2\2\u00ce\u00cf\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d2\t\4\2\2\u00d1\u00ce\3")
        buf.write("\2\2\2\u00d2\u00d5\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4")
        buf.write("\3\2\2\2\u00d4\u00d7\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6")
        buf.write("\u00cb\3\2\2\2\u00d6\u00cc\3\2\2\2\u00d7\16\3\2\2\2\u00d8")
        buf.write("\u00d9\7\62\2\2\u00d9\u00e5\t\6\2\2\u00da\u00e6\t\7\2")
        buf.write("\2\u00db\u00e2\t\b\2\2\u00dc\u00de\7a\2\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df")
        buf.write("\u00e1\t\7\2\2\u00e0\u00dd\3\2\2\2\u00e1\u00e4\3\2\2\2")
        buf.write("\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e6\3")
        buf.write("\2\2\2\u00e4\u00e2\3\2\2\2\u00e5\u00da\3\2\2\2\u00e5\u00db")
        buf.write("\3\2\2\2\u00e6\20\3\2\2\2\u00e7\u00e8\7\62\2\2\u00e8\u00f4")
        buf.write("\t\t\2\2\u00e9\u00f5\t\n\2\2\u00ea\u00f1\7\63\2\2\u00eb")
        buf.write("\u00ed\7a\2\2\u00ec\u00eb\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\u00ee\3\2\2\2\u00ee\u00f0\t\n\2\2\u00ef\u00ec\3")
        buf.write("\2\2\2\u00f0\u00f3\3\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2")
        buf.write("\3\2\2\2\u00f2\u00f5\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4")
        buf.write("\u00e9\3\2\2\2\u00f4\u00ea\3\2\2\2\u00f5\22\3\2\2\2\u00f6")
        buf.write("\u00f8\5\r\7\2\u00f7\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fd\5\u0081A\2\u00fa\u00fc")
        buf.write("\5\31\r\2\u00fb\u00fa\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2")
        buf.write("\u00ff\u00fd\3\2\2\2\u0100\u0101\5\33\16\2\u0101\u011a")
        buf.write("\3\2\2\2\u0102\u010a\5\r\7\2\u0103\u0107\5\u0081A\2\u0104")
        buf.write("\u0106\5\31\r\2\u0105\u0104\3\2\2\2\u0106\u0109\3\2\2")
        buf.write("\2\u0107\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u010b")
        buf.write("\3\2\2\2\u0109\u0107\3\2\2\2\u010a\u0103\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\5\33\16")
        buf.write("\2\u010d\u011a\3\2\2\2\u010e\u010f\5\r\7\2\u010f\u0113")
        buf.write("\5\u0081A\2\u0110\u0112\5\31\r\2\u0111\u0110\3\2\2\2\u0112")
        buf.write("\u0115\3\2\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0118\5")
        buf.write("\33\16\2\u0117\u0116\3\2\2\2\u0117\u0118\3\2\2\2\u0118")
        buf.write("\u011a\3\2\2\2\u0119\u00f7\3\2\2\2\u0119\u0102\3\2\2\2")
        buf.write("\u0119\u010e\3\2\2\2\u011a\24\3\2\2\2\u011b\u011e\5+\26")
        buf.write("\2\u011c\u011e\5-\27\2\u011d\u011b\3\2\2\2\u011d\u011c")
        buf.write("\3\2\2\2\u011e\26\3\2\2\2\u011f\u0125\5\u0089E\2\u0120")
        buf.write("\u0124\5\u0097L\2\u0121\u0122\7)\2\2\u0122\u0124\7$\2")
        buf.write("\2\u0123\u0120\3\2\2\2\u0123\u0121\3\2\2\2\u0124\u0127")
        buf.write("\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2\2\2\u0126")
        buf.write("\u0128\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u0129\5\u0089")
        buf.write("E\2\u0129\30\3\2\2\2\u012a\u012b\t\4\2\2\u012b\32\3\2")
        buf.write("\2\2\u012c\u012f\t\13\2\2\u012d\u0130\5O(\2\u012e\u0130")
        buf.write("\5Q)\2\u012f\u012d\3\2\2\2\u012f\u012e\3\2\2\2\u012f\u0130")
        buf.write("\3\2\2\2\u0130\u0132\3\2\2\2\u0131\u0133\5\31\r\2\u0132")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\u0132\3\2\2\2")
        buf.write("\u0134\u0135\3\2\2\2\u0135\34\3\2\2\2\u0136\u013b\5\63")
        buf.write("\32\2\u0137\u013b\5\65\33\2\u0138\u013b\5\67\34\2\u0139")
        buf.write("\u013b\59\35\2\u013a\u0136\3\2\2\2\u013a\u0137\3\2\2\2")
        buf.write("\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b\36\3\2")
        buf.write("\2\2\u013c\u013d\7D\2\2\u013d\u013e\7t\2\2\u013e\u013f")
        buf.write("\7g\2\2\u013f\u0140\7c\2\2\u0140\u0141\7m\2\2\u0141 \3")
        buf.write("\2\2\2\u0142\u0143\7E\2\2\u0143\u0144\7q\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7v\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7p\2\2\u0148\u0149\7w\2\2\u0149\u014a\7g\2\2\u014a\"")
        buf.write("\3\2\2\2\u014b\u014c\7K\2\2\u014c\u014d\7h\2\2\u014d$")
        buf.write("\3\2\2\2\u014e\u014f\7G\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7u\2\2\u0151\u0152\7g\2\2\u0152\u0153\7k\2\2\u0153\u0154")
        buf.write("\7h\2\2\u0154&\3\2\2\2\u0155\u0156\7G\2\2\u0156\u0157")
        buf.write("\7n\2\2\u0157\u0158\7u\2\2\u0158\u0159\7g\2\2\u0159(\3")
        buf.write("\2\2\2\u015a\u015b\7H\2\2\u015b\u015c\7q\2\2\u015c\u015d")
        buf.write("\7t\2\2\u015d\u015e\7g\2\2\u015e\u015f\7c\2\2\u015f\u0160")
        buf.write("\7e\2\2\u0160\u0161\7j\2\2\u0161*\3\2\2\2\u0162\u0163")
        buf.write("\7V\2\2\u0163\u0164\7t\2\2\u0164\u0165\7w\2\2\u0165\u0166")
        buf.write("\7g\2\2\u0166,\3\2\2\2\u0167\u0168\7H\2\2\u0168\u0169")
        buf.write("\7c\2\2\u0169\u016a\7n\2\2\u016a\u016b\7u\2\2\u016b\u016c")
        buf.write("\7g\2\2\u016c.\3\2\2\2\u016d\u016e\7C\2\2\u016e\u016f")
        buf.write("\7t\2\2\u016f\u0170\7t\2\2\u0170\u0171\7c\2\2\u0171\u0172")
        buf.write("\7{\2\2\u0172\60\3\2\2\2\u0173\u0174\7K\2\2\u0174\u0175")
        buf.write("\7p\2\2\u0175\62\3\2\2\2\u0176\u0177\7K\2\2\u0177\u0178")
        buf.write("\7p\2\2\u0178\u0179\7v\2\2\u0179\64\3\2\2\2\u017a\u017b")
        buf.write("\7H\2\2\u017b\u017c\7n\2\2\u017c\u017d\7q\2\2\u017d\u017e")
        buf.write("\7c\2\2\u017e\u017f\7v\2\2\u017f\66\3\2\2\2\u0180\u0181")
        buf.write("\7D\2\2\u0181\u0182\7q\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7n\2\2\u0184\u0185\7g\2\2\u0185\u0186\7c\2\2\u0186\u0187")
        buf.write("\7p\2\2\u01878\3\2\2\2\u0188\u0189\7U\2\2\u0189\u018a")
        buf.write("\7v\2\2\u018a\u018b\7t\2\2\u018b\u018c\7k\2\2\u018c\u018d")
        buf.write("\7p\2\2\u018d\u018e\7i\2\2\u018e:\3\2\2\2\u018f\u0190")
        buf.write("\7T\2\2\u0190\u0191\7g\2\2\u0191\u0192\7v\2\2\u0192\u0193")
        buf.write("\7w\2\2\u0193\u0194\7t\2\2\u0194\u0195\7p\2\2\u0195<\3")
        buf.write("\2\2\2\u0196\u0197\7P\2\2\u0197\u0198\7w\2\2\u0198\u0199")
        buf.write("\7n\2\2\u0199\u019a\7n\2\2\u019a>\3\2\2\2\u019b\u019c")
        buf.write("\7E\2\2\u019c\u019d\7n\2\2\u019d\u019e\7c\2\2\u019e\u019f")
        buf.write("\7u\2\2\u019f\u01a0\7u\2\2\u01a0@\3\2\2\2\u01a1\u01a2")
        buf.write("\7X\2\2\u01a2\u01a3\7c\2\2\u01a3\u01a4\7n\2\2\u01a4B\3")
        buf.write("\2\2\2\u01a5\u01a6\7X\2\2\u01a6\u01a7\7c\2\2\u01a7\u01a8")
        buf.write("\7t\2\2\u01a8D\3\2\2\2\u01a9\u01aa\7U\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad\7h\2\2\u01adF\3")
        buf.write("\2\2\2\u01ae\u01af\7E\2\2\u01af\u01b0\7q\2\2\u01b0\u01b1")
        buf.write("\7p\2\2\u01b1\u01b2\7u\2\2\u01b2\u01b3\7v\2\2\u01b3\u01b4")
        buf.write("\7t\2\2\u01b4\u01b5\7w\2\2\u01b5\u01b6\7e\2\2\u01b6\u01b7")
        buf.write("\7v\2\2\u01b7\u01b8\7q\2\2\u01b8\u01b9\7t\2\2\u01b9H\3")
        buf.write("\2\2\2\u01ba\u01bb\7F\2\2\u01bb\u01bc\7g\2\2\u01bc\u01bd")
        buf.write("\7u\2\2\u01bd\u01be\7v\2\2\u01be\u01bf\7t\2\2\u01bf\u01c0")
        buf.write("\7w\2\2\u01c0\u01c1\7e\2\2\u01c1\u01c2\7v\2\2\u01c2\u01c3")
        buf.write("\7q\2\2\u01c3\u01c4\7t\2\2\u01c4J\3\2\2\2\u01c5\u01c6")
        buf.write("\7P\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8\7y\2\2\u01c8L\3")
        buf.write("\2\2\2\u01c9\u01ca\7D\2\2\u01ca\u01cb\7{\2\2\u01cbN\3")
        buf.write("\2\2\2\u01cc\u01cd\7-\2\2\u01cdP\3\2\2\2\u01ce\u01cf\7")
        buf.write("/\2\2\u01cfR\3\2\2\2\u01d0\u01d1\7,\2\2\u01d1T\3\2\2\2")
        buf.write("\u01d2\u01d3\7\61\2\2\u01d3V\3\2\2\2\u01d4\u01d5\7\'\2")
        buf.write("\2\u01d5X\3\2\2\2\u01d6\u01d7\7#\2\2\u01d7Z\3\2\2\2\u01d8")
        buf.write("\u01d9\7(\2\2\u01d9\u01da\7(\2\2\u01da\\\3\2\2\2\u01db")
        buf.write("\u01dc\7~\2\2\u01dc\u01dd\7~\2\2\u01dd^\3\2\2\2\u01de")
        buf.write("\u01df\7?\2\2\u01df\u01e0\7?\2\2\u01e0`\3\2\2\2\u01e1")
        buf.write("\u01e2\7?\2\2\u01e2b\3\2\2\2\u01e3\u01e4\7#\2\2\u01e4")
        buf.write("\u01e5\7?\2\2\u01e5d\3\2\2\2\u01e6\u01e7\7>\2\2\u01e7")
        buf.write("f\3\2\2\2\u01e8\u01e9\7>\2\2\u01e9\u01ea\7?\2\2\u01ea")
        buf.write("h\3\2\2\2\u01eb\u01ec\7@\2\2\u01ecj\3\2\2\2\u01ed\u01ee")
        buf.write("\7@\2\2\u01ee\u01ef\7?\2\2\u01efl\3\2\2\2\u01f0\u01f1")
        buf.write("\7?\2\2\u01f1\u01f2\7?\2\2\u01f2\u01f3\7\60\2\2\u01f3")
        buf.write("n\3\2\2\2\u01f4\u01f5\7-\2\2\u01f5\u01f6\7\60\2\2\u01f6")
        buf.write("p\3\2\2\2\u01f7\u01f8\7<\2\2\u01f8\u01f9\7<\2\2\u01f9")
        buf.write("r\3\2\2\2\u01fa\u01fb\7*\2\2\u01fbt\3\2\2\2\u01fc\u01fd")
        buf.write("\7+\2\2\u01fdv\3\2\2\2\u01fe\u01ff\7}\2\2\u01ffx\3\2\2")
        buf.write("\2\u0200\u0201\7\177\2\2\u0201z\3\2\2\2\u0202\u0203\7")
        buf.write("]\2\2\u0203|\3\2\2\2\u0204\u0205\7_\2\2\u0205~\3\2\2\2")
        buf.write("\u0206\u0207\7\60\2\2\u0207\u0208\7\60\2\2\u0208\u0080")
        buf.write("\3\2\2\2\u0209\u020a\7\60\2\2\u020a\u0082\3\2\2\2\u020b")
        buf.write("\u020c\7.\2\2\u020c\u0084\3\2\2\2\u020d\u020e\7=\2\2\u020e")
        buf.write("\u0086\3\2\2\2\u020f\u0210\7<\2\2\u0210\u0088\3\2\2\2")
        buf.write("\u0211\u0212\7$\2\2\u0212\u008a\3\2\2\2\u0213\u0217\t")
        buf.write("\f\2\2\u0214\u0216\t\r\2\2\u0215\u0214\3\2\2\2\u0216\u0219")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u008c\3\2\2\2\u0219\u0217\3\2\2\2\u021a\u021c\7&\2\2")
        buf.write("\u021b\u021d\t\r\2\2\u021c\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u008e")
        buf.write("\3\2\2\2\u0220\u0222\t\16\2\2\u0221\u0220\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0221\3\2\2\2\u0223\u0224\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0226\bH\2\2\u0226\u0090\3")
        buf.write("\2\2\2\u0227\u0228\13\2\2\2\u0228\u0229\bI\6\2\u0229\u0092")
        buf.write("\3\2\2\2\u022a\u022e\7$\2\2\u022b\u022d\5\u0097L\2\u022c")
        buf.write("\u022b\3\2\2\2\u022d\u0230\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022e\u022f\3\2\2\2\u022f\u0232\3\2\2\2\u0230\u022e\3")
        buf.write("\2\2\2\u0231\u0233\t\17\2\2\u0232\u0231\3\2\2\2\u0233")
        buf.write("\u0234\3\2\2\2\u0234\u0235\bJ\7\2\u0235\u0094\3\2\2\2")
        buf.write("\u0236\u023a\7$\2\2\u0237\u0239\5\u0097L\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a")
        buf.write("\u023b\3\2\2\2\u023b\u023d\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023d\u023e\5\u009bN\2\u023e\u023f\bK\b\2\u023f\u0096")
        buf.write("\3\2\2\2\u0240\u0243\n\20\2\2\u0241\u0243\5\u0099M\2\u0242")
        buf.write("\u0240\3\2\2\2\u0242\u0241\3\2\2\2\u0243\u0098\3\2\2\2")
        buf.write("\u0244\u0245\7^\2\2\u0245\u0246\t\21\2\2\u0246\u009a\3")
        buf.write("\2\2\2\u0247\u0248\7^\2\2\u0248\u024b\n\21\2\2\u0249\u024b")
        buf.write("\n\22\2\2\u024a\u0247\3\2\2\2\u024a\u0249\3\2\2\2\u024b")
        buf.write("\u009c\3\2\2\2\'\2\u00a1\u00b5\u00bb\u00c1\u00c6\u00c9")
        buf.write("\u00ce\u00d3\u00d6\u00dd\u00e2\u00e5\u00ec\u00f1\u00f4")
        buf.write("\u00f7\u00fd\u0107\u010a\u0113\u0117\u0119\u011d\u0123")
        buf.write("\u0125\u012f\u0134\u013a\u0217\u021e\u0223\u022e\u0232")
        buf.write("\u023a\u0242\u024a\t\b\2\2\3\4\2\3\4\3\3\4\4\3I\5\3J\6")
        buf.write("\3K\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    LITERAL = 2
    INT_LIT = 3
    FLOAT_LIT = 4
    BOOL_LIT = 5
    STR_LIT = 6
    DIGIT = 7
    PRIMITIVE_TYPE = 8
    BREAK = 9
    CONTINUE = 10
    IF = 11
    ELSEIF = 12
    ELSE = 13
    FOREACH = 14
    TRUE = 15
    FALSE = 16
    ARRAY = 17
    IN = 18
    INT = 19
    FLOAT = 20
    BOOLEAN = 21
    STRING = 22
    RETURN = 23
    NULL = 24
    CLASS = 25
    VAL = 26
    VAR = 27
    SELF = 28
    CONSTRUCTOR = 29
    DESTRUCTOR = 30
    NEW = 31
    BY = 32
    ADD = 33
    SUB = 34
    MUL = 35
    DIV = 36
    PRCNT = 37
    NOT = 38
    AND = 39
    OR = 40
    EQ = 41
    ASSIGN = 42
    NOT_EQ = 43
    LESS = 44
    LESS_EQ = 45
    GREAT = 46
    GREAT_EQ = 47
    EQ_STR = 48
    CONCAT_STR = 49
    STATIC_ACC = 50
    LB = 51
    RB = 52
    LP = 53
    RP = 54
    LSB = 55
    RSB = 56
    DOTDOT = 57
    DOT = 58
    CM = 59
    SEMI = 60
    CL = 61
    DOUBLEQUOTE = 62
    ID = 63
    STATIC_ID = 64
    WS = 65
    ERROR_CHAR = 66
    UNCLOSE_STRING = 67
    ILLEGAL_ESCAPE = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
            "'=='", "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", 
            "'+.'", "'::'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'..'", 
            "'.'", "','", "';'", "':'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LITERAL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
            "STR_LIT", "DIGIT", "PRIMITIVE_TYPE", "BREAK", "CONTINUE", "IF", 
            "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
            "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
            "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "ADD", "SUB", "MUL", "DIV", "PRCNT", "NOT", "AND", "OR", "EQ", 
            "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", "GREAT", "GREAT_EQ", 
            "EQ_STR", "CONCAT_STR", "STATIC_ACC", "LB", "RB", "LP", "RP", 
            "LSB", "RSB", "DOTDOT", "DOT", "CM", "SEMI", "CL", "DOUBLEQUOTE", 
            "ID", "STATIC_ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCK_COMMENT", "CMT", "LITERAL", "INT_LIT", "OCTAL", 
                  "DECIMAL", "HEX", "BINARY", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", 
                  "DIGIT", "EXPONENT", "PRIMITIVE_TYPE", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", 
                  "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "PRCNT", "NOT", 
                  "AND", "OR", "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", 
                  "GREAT", "GREAT_EQ", "EQ_STR", "CONCAT_STR", "STATIC_ACC", 
                  "LB", "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", "DOT", 
                  "CM", "SEMI", "CL", "DOUBLEQUOTE", "ID", "STATIC_ID", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.LITERAL_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            	
            		raise ErrorToken(self.text)	
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise IllegalEscape(self.text[1:])
            	
     


