# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0236\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\3\2\3\2\7\2\u009c\n\2\f\2\16\2\u009f\13\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\5\4\u00ac\n\4\3\5\3")
        buf.write("\5\3\5\3\5\5\5\u00b2\n\5\3\5\7\5\u00b5\n\5\f\5\16\5\u00b8")
        buf.write("\13\5\5\5\u00ba\n\5\3\6\3\6\3\6\5\6\u00bf\n\6\3\6\7\6")
        buf.write("\u00c2\n\6\f\6\16\6\u00c5\13\6\5\6\u00c7\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\5\7\u00ce\n\7\3\7\7\7\u00d1\n\7\f\7\16\7\u00d4")
        buf.write("\13\7\5\7\u00d6\n\7\3\b\3\b\3\b\3\b\3\b\5\b\u00dd\n\b")
        buf.write("\3\b\7\b\u00e0\n\b\f\b\16\b\u00e3\13\b\5\b\u00e5\n\b\3")
        buf.write("\t\5\t\u00e8\n\t\3\t\3\t\7\t\u00ec\n\t\f\t\16\t\u00ef")
        buf.write("\13\t\3\t\3\t\3\t\3\t\3\t\7\t\u00f6\n\t\f\t\16\t\u00f9")
        buf.write("\13\t\5\t\u00fb\n\t\3\t\3\t\3\t\3\t\3\t\7\t\u0102\n\t")
        buf.write("\f\t\16\t\u0105\13\t\3\t\5\t\u0108\n\t\5\t\u010a\n\t\3")
        buf.write("\n\3\n\5\n\u010e\n\n\3\13\3\13\3\13\3\13\7\13\u0114\n")
        buf.write("\13\f\13\16\13\u0117\13\13\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\r\5\r\u0120\n\r\3\r\6\r\u0123\n\r\r\r\16\r\u0124\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3.\3")
        buf.write(".\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\67\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\7D\u0200\n")
        buf.write("D\fD\16D\u0203\13D\3E\3E\6E\u0207\nE\rE\16E\u0208\3F\6")
        buf.write("F\u020c\nF\rF\16F\u020d\3F\3F\3G\3G\3G\3H\3H\7H\u0217")
        buf.write("\nH\fH\16H\u021a\13H\3H\5H\u021d\nH\3H\3H\3I\3I\7I\u0223")
        buf.write("\nI\fI\16I\u0226\13I\3I\3I\3I\3J\3J\5J\u022d\nJ\3K\3K")
        buf.write("\3K\3L\3L\3L\5L\u0235\nL\3\u009d\2M\3\3\5\2\7\4\t\2\13")
        buf.write("\2\r\2\17\2\21\5\23\6\25\7\27\b\31\2\33\t\35\n\37\13!")
        buf.write("\f#\r%\16\'\17)\20+\21-\22/\23\61\24\63\25\65\26\67\27")
        buf.write("9\30;\31=\32?\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([")
        buf.write(")]*_+a,c-e.g/i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177")
        buf.write(";\u0081<\u0083=\u0085>\u0087?\u0089@\u008bA\u008dB\u008f")
        buf.write("C\u0091D\u0093\2\u0095\2\u0097\2\3\2\23\3\2\629\3\2\63")
        buf.write("9\3\2\62;\3\2\63;\4\2ZZzz\4\2\62;CH\4\2\63;CH\4\2DDdd")
        buf.write("\3\2\62\63\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f")
        buf.write("\17\17\"\"\7\3\n\f\16\17$$))^^\7\2\n\f\16\17$$))^^\n\2")
        buf.write("$$))^^ddhhppttvv\3\2^^\2\u0251\2\3\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2")
        buf.write("?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2")
        buf.write("\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2")
        buf.write("\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2")
        buf.write("\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3")
        buf.write("\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o")
        buf.write("\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2")
        buf.write("y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\3\u0099\3\2\2\2\5\u00a4\3\2\2")
        buf.write("\2\7\u00ab\3\2\2\2\t\u00ad\3\2\2\2\13\u00c6\3\2\2\2\r")
        buf.write("\u00c8\3\2\2\2\17\u00d7\3\2\2\2\21\u0109\3\2\2\2\23\u010d")
        buf.write("\3\2\2\2\25\u010f\3\2\2\2\27\u011a\3\2\2\2\31\u011c\3")
        buf.write("\2\2\2\33\u0126\3\2\2\2\35\u012c\3\2\2\2\37\u0135\3\2")
        buf.write("\2\2!\u0138\3\2\2\2#\u013f\3\2\2\2%\u0144\3\2\2\2\'\u014c")
        buf.write("\3\2\2\2)\u0151\3\2\2\2+\u0157\3\2\2\2-\u015d\3\2\2\2")
        buf.write("/\u0160\3\2\2\2\61\u0164\3\2\2\2\63\u016a\3\2\2\2\65\u0172")
        buf.write("\3\2\2\2\67\u0179\3\2\2\29\u0180\3\2\2\2;\u0185\3\2\2")
        buf.write("\2=\u018b\3\2\2\2?\u018f\3\2\2\2A\u0193\3\2\2\2C\u0198")
        buf.write("\3\2\2\2E\u01a4\3\2\2\2G\u01af\3\2\2\2I\u01b3\3\2\2\2")
        buf.write("K\u01b6\3\2\2\2M\u01b8\3\2\2\2O\u01ba\3\2\2\2Q\u01bc\3")
        buf.write("\2\2\2S\u01be\3\2\2\2U\u01c0\3\2\2\2W\u01c2\3\2\2\2Y\u01c5")
        buf.write("\3\2\2\2[\u01c8\3\2\2\2]\u01cb\3\2\2\2_\u01cd\3\2\2\2")
        buf.write("a\u01d0\3\2\2\2c\u01d2\3\2\2\2e\u01d5\3\2\2\2g\u01d7\3")
        buf.write("\2\2\2i\u01da\3\2\2\2k\u01de\3\2\2\2m\u01e1\3\2\2\2o\u01e4")
        buf.write("\3\2\2\2q\u01e6\3\2\2\2s\u01e8\3\2\2\2u\u01ea\3\2\2\2")
        buf.write("w\u01ec\3\2\2\2y\u01ee\3\2\2\2{\u01f0\3\2\2\2}\u01f3\3")
        buf.write("\2\2\2\177\u01f5\3\2\2\2\u0081\u01f7\3\2\2\2\u0083\u01f9")
        buf.write("\3\2\2\2\u0085\u01fb\3\2\2\2\u0087\u01fd\3\2\2\2\u0089")
        buf.write("\u0204\3\2\2\2\u008b\u020b\3\2\2\2\u008d\u0211\3\2\2\2")
        buf.write("\u008f\u0214\3\2\2\2\u0091\u0220\3\2\2\2\u0093\u022c\3")
        buf.write("\2\2\2\u0095\u022e\3\2\2\2\u0097\u0234\3\2\2\2\u0099\u009d")
        buf.write("\5\5\3\2\u009a\u009c\13\2\2\2\u009b\u009a\3\2\2\2\u009c")
        buf.write("\u009f\3\2\2\2\u009d\u009e\3\2\2\2\u009d\u009b\3\2\2\2")
        buf.write("\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1\5")
        buf.write("\5\3\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\b\2\2\2\u00a3\4")
        buf.write("\3\2\2\2\u00a4\u00a5\7%\2\2\u00a5\u00a6\7%\2\2\u00a6\6")
        buf.write("\3\2\2\2\u00a7\u00ac\5\t\5\2\u00a8\u00ac\5\13\6\2\u00a9")
        buf.write("\u00ac\5\r\7\2\u00aa\u00ac\5\17\b\2\u00ab\u00a7\3\2\2")
        buf.write("\2\u00ab\u00a8\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa")
        buf.write("\3\2\2\2\u00ac\b\3\2\2\2\u00ad\u00b9\7\62\2\2\u00ae\u00ba")
        buf.write("\t\2\2\2\u00af\u00b6\t\3\2\2\u00b0\u00b2\7a\2\2\u00b1")
        buf.write("\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b5\t\2\2\2\u00b4\u00b1\3\2\2\2\u00b5\u00b8\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00ba")
        buf.write("\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00ae\3\2\2\2\u00b9")
        buf.write("\u00af\3\2\2\2\u00ba\n\3\2\2\2\u00bb\u00c7\t\4\2\2\u00bc")
        buf.write("\u00c3\t\5\2\2\u00bd\u00bf\7a\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00be\u00bf\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\t")
        buf.write("\4\2\2\u00c1\u00be\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1")
        buf.write("\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5")
        buf.write("\u00c3\3\2\2\2\u00c6\u00bb\3\2\2\2\u00c6\u00bc\3\2\2\2")
        buf.write("\u00c7\f\3\2\2\2\u00c8\u00c9\7\62\2\2\u00c9\u00d5\t\6")
        buf.write("\2\2\u00ca\u00d6\t\7\2\2\u00cb\u00d2\t\b\2\2\u00cc\u00ce")
        buf.write("\7a\2\2\u00cd\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce")
        buf.write("\u00cf\3\2\2\2\u00cf\u00d1\t\7\2\2\u00d0\u00cd\3\2\2\2")
        buf.write("\u00d1\u00d4\3\2\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d3\3")
        buf.write("\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5\u00ca")
        buf.write("\3\2\2\2\u00d5\u00cb\3\2\2\2\u00d6\16\3\2\2\2\u00d7\u00d8")
        buf.write("\7\62\2\2\u00d8\u00e4\t\t\2\2\u00d9\u00e5\t\n\2\2\u00da")
        buf.write("\u00e1\7\63\2\2\u00db\u00dd\7a\2\2\u00dc\u00db\3\2\2\2")
        buf.write("\u00dc\u00dd\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00e0\t")
        buf.write("\n\2\2\u00df\u00dc\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3")
        buf.write("\u00e1\3\2\2\2\u00e4\u00d9\3\2\2\2\u00e4\u00da\3\2\2\2")
        buf.write("\u00e5\20\3\2\2\2\u00e6\u00e8\5\13\6\2\u00e7\u00e6\3\2")
        buf.write("\2\2\u00e7\u00e8\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00ed")
        buf.write("\5}?\2\u00ea\u00ec\5\27\f\2\u00eb\u00ea\3\2\2\2\u00ec")
        buf.write("\u00ef\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0\u00f1\5")
        buf.write("\31\r\2\u00f1\u010a\3\2\2\2\u00f2\u00fa\5\13\6\2\u00f3")
        buf.write("\u00f7\5}?\2\u00f4\u00f6\5\27\f\2\u00f5\u00f4\3\2\2\2")
        buf.write("\u00f6\u00f9\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f8\3")
        buf.write("\2\2\2\u00f8\u00fb\3\2\2\2\u00f9\u00f7\3\2\2\2\u00fa\u00f3")
        buf.write("\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc")
        buf.write("\u00fd\5\31\r\2\u00fd\u010a\3\2\2\2\u00fe\u00ff\5\13\6")
        buf.write("\2\u00ff\u0103\5}?\2\u0100\u0102\5\27\f\2\u0101\u0100")
        buf.write("\3\2\2\2\u0102\u0105\3\2\2\2\u0103\u0101\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0106\u0108\5\31\r\2\u0107\u0106\3\2\2\2\u0107\u0108")
        buf.write("\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u00e7\3\2\2\2\u0109")
        buf.write("\u00f2\3\2\2\2\u0109\u00fe\3\2\2\2\u010a\22\3\2\2\2\u010b")
        buf.write("\u010e\5\'\24\2\u010c\u010e\5)\25\2\u010d\u010b\3\2\2")
        buf.write("\2\u010d\u010c\3\2\2\2\u010e\24\3\2\2\2\u010f\u0115\5")
        buf.write("\u0085C\2\u0110\u0114\5\u0093J\2\u0111\u0112\7)\2\2\u0112")
        buf.write("\u0114\7$\2\2\u0113\u0110\3\2\2\2\u0113\u0111\3\2\2\2")
        buf.write("\u0114\u0117\3\2\2\2\u0115\u0113\3\2\2\2\u0115\u0116\3")
        buf.write("\2\2\2\u0116\u0118\3\2\2\2\u0117\u0115\3\2\2\2\u0118\u0119")
        buf.write("\5\u0085C\2\u0119\26\3\2\2\2\u011a\u011b\t\4\2\2\u011b")
        buf.write("\30\3\2\2\2\u011c\u011f\t\13\2\2\u011d\u0120\5K&\2\u011e")
        buf.write("\u0120\5M\'\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121\u0123\5")
        buf.write("\27\f\2\u0122\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0122\3\2\2\2\u0124\u0125\3\2\2\2\u0125\32\3\2\2\2\u0126")
        buf.write("\u0127\7D\2\2\u0127\u0128\7t\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\u012a\7c\2\2\u012a\u012b\7m\2\2\u012b\34\3\2\2\2\u012c")
        buf.write("\u012d\7E\2\2\u012d\u012e\7q\2\2\u012e\u012f\7p\2\2\u012f")
        buf.write("\u0130\7v\2\2\u0130\u0131\7k\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("\u0133\7w\2\2\u0133\u0134\7g\2\2\u0134\36\3\2\2\2\u0135")
        buf.write("\u0136\7K\2\2\u0136\u0137\7h\2\2\u0137 \3\2\2\2\u0138")
        buf.write("\u0139\7G\2\2\u0139\u013a\7n\2\2\u013a\u013b\7u\2\2\u013b")
        buf.write("\u013c\7g\2\2\u013c\u013d\7k\2\2\u013d\u013e\7h\2\2\u013e")
        buf.write("\"\3\2\2\2\u013f\u0140\7G\2\2\u0140\u0141\7n\2\2\u0141")
        buf.write("\u0142\7u\2\2\u0142\u0143\7g\2\2\u0143$\3\2\2\2\u0144")
        buf.write("\u0145\7H\2\2\u0145\u0146\7q\2\2\u0146\u0147\7t\2\2\u0147")
        buf.write("\u0148\7g\2\2\u0148\u0149\7c\2\2\u0149\u014a\7e\2\2\u014a")
        buf.write("\u014b\7j\2\2\u014b&\3\2\2\2\u014c\u014d\7V\2\2\u014d")
        buf.write("\u014e\7t\2\2\u014e\u014f\7w\2\2\u014f\u0150\7g\2\2\u0150")
        buf.write("(\3\2\2\2\u0151\u0152\7H\2\2\u0152\u0153\7c\2\2\u0153")
        buf.write("\u0154\7n\2\2\u0154\u0155\7u\2\2\u0155\u0156\7g\2\2\u0156")
        buf.write("*\3\2\2\2\u0157\u0158\7C\2\2\u0158\u0159\7t\2\2\u0159")
        buf.write("\u015a\7t\2\2\u015a\u015b\7c\2\2\u015b\u015c\7{\2\2\u015c")
        buf.write(",\3\2\2\2\u015d\u015e\7K\2\2\u015e\u015f\7p\2\2\u015f")
        buf.write(".\3\2\2\2\u0160\u0161\7K\2\2\u0161\u0162\7p\2\2\u0162")
        buf.write("\u0163\7v\2\2\u0163\60\3\2\2\2\u0164\u0165\7H\2\2\u0165")
        buf.write("\u0166\7n\2\2\u0166\u0167\7q\2\2\u0167\u0168\7c\2\2\u0168")
        buf.write("\u0169\7v\2\2\u0169\62\3\2\2\2\u016a\u016b\7D\2\2\u016b")
        buf.write("\u016c\7q\2\2\u016c\u016d\7q\2\2\u016d\u016e\7n\2\2\u016e")
        buf.write("\u016f\7g\2\2\u016f\u0170\7c\2\2\u0170\u0171\7p\2\2\u0171")
        buf.write("\64\3\2\2\2\u0172\u0173\7U\2\2\u0173\u0174\7v\2\2\u0174")
        buf.write("\u0175\7t\2\2\u0175\u0176\7k\2\2\u0176\u0177\7p\2\2\u0177")
        buf.write("\u0178\7i\2\2\u0178\66\3\2\2\2\u0179\u017a\7T\2\2\u017a")
        buf.write("\u017b\7g\2\2\u017b\u017c\7v\2\2\u017c\u017d\7w\2\2\u017d")
        buf.write("\u017e\7t\2\2\u017e\u017f\7p\2\2\u017f8\3\2\2\2\u0180")
        buf.write("\u0181\7P\2\2\u0181\u0182\7w\2\2\u0182\u0183\7n\2\2\u0183")
        buf.write("\u0184\7n\2\2\u0184:\3\2\2\2\u0185\u0186\7E\2\2\u0186")
        buf.write("\u0187\7n\2\2\u0187\u0188\7c\2\2\u0188\u0189\7u\2\2\u0189")
        buf.write("\u018a\7u\2\2\u018a<\3\2\2\2\u018b\u018c\7X\2\2\u018c")
        buf.write("\u018d\7c\2\2\u018d\u018e\7n\2\2\u018e>\3\2\2\2\u018f")
        buf.write("\u0190\7X\2\2\u0190\u0191\7c\2\2\u0191\u0192\7t\2\2\u0192")
        buf.write("@\3\2\2\2\u0193\u0194\7U\2\2\u0194\u0195\7g\2\2\u0195")
        buf.write("\u0196\7n\2\2\u0196\u0197\7h\2\2\u0197B\3\2\2\2\u0198")
        buf.write("\u0199\7E\2\2\u0199\u019a\7q\2\2\u019a\u019b\7p\2\2\u019b")
        buf.write("\u019c\7u\2\2\u019c\u019d\7v\2\2\u019d\u019e\7t\2\2\u019e")
        buf.write("\u019f\7w\2\2\u019f\u01a0\7e\2\2\u01a0\u01a1\7v\2\2\u01a1")
        buf.write("\u01a2\7q\2\2\u01a2\u01a3\7t\2\2\u01a3D\3\2\2\2\u01a4")
        buf.write("\u01a5\7F\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7u\2\2\u01a7")
        buf.write("\u01a8\7v\2\2\u01a8\u01a9\7t\2\2\u01a9\u01aa\7w\2\2\u01aa")
        buf.write("\u01ab\7e\2\2\u01ab\u01ac\7v\2\2\u01ac\u01ad\7q\2\2\u01ad")
        buf.write("\u01ae\7t\2\2\u01aeF\3\2\2\2\u01af\u01b0\7P\2\2\u01b0")
        buf.write("\u01b1\7g\2\2\u01b1\u01b2\7y\2\2\u01b2H\3\2\2\2\u01b3")
        buf.write("\u01b4\7D\2\2\u01b4\u01b5\7{\2\2\u01b5J\3\2\2\2\u01b6")
        buf.write("\u01b7\7-\2\2\u01b7L\3\2\2\2\u01b8\u01b9\7/\2\2\u01b9")
        buf.write("N\3\2\2\2\u01ba\u01bb\7,\2\2\u01bbP\3\2\2\2\u01bc\u01bd")
        buf.write("\7\61\2\2\u01bdR\3\2\2\2\u01be\u01bf\7\'\2\2\u01bfT\3")
        buf.write("\2\2\2\u01c0\u01c1\7#\2\2\u01c1V\3\2\2\2\u01c2\u01c3\7")
        buf.write("(\2\2\u01c3\u01c4\7(\2\2\u01c4X\3\2\2\2\u01c5\u01c6\7")
        buf.write("~\2\2\u01c6\u01c7\7~\2\2\u01c7Z\3\2\2\2\u01c8\u01c9\7")
        buf.write("?\2\2\u01c9\u01ca\7?\2\2\u01ca\\\3\2\2\2\u01cb\u01cc\7")
        buf.write("?\2\2\u01cc^\3\2\2\2\u01cd\u01ce\7#\2\2\u01ce\u01cf\7")
        buf.write("?\2\2\u01cf`\3\2\2\2\u01d0\u01d1\7>\2\2\u01d1b\3\2\2\2")
        buf.write("\u01d2\u01d3\7>\2\2\u01d3\u01d4\7?\2\2\u01d4d\3\2\2\2")
        buf.write("\u01d5\u01d6\7@\2\2\u01d6f\3\2\2\2\u01d7\u01d8\7@\2\2")
        buf.write("\u01d8\u01d9\7?\2\2\u01d9h\3\2\2\2\u01da\u01db\7?\2\2")
        buf.write("\u01db\u01dc\7?\2\2\u01dc\u01dd\7\60\2\2\u01ddj\3\2\2")
        buf.write("\2\u01de\u01df\7-\2\2\u01df\u01e0\7\60\2\2\u01e0l\3\2")
        buf.write("\2\2\u01e1\u01e2\7<\2\2\u01e2\u01e3\7<\2\2\u01e3n\3\2")
        buf.write("\2\2\u01e4\u01e5\7*\2\2\u01e5p\3\2\2\2\u01e6\u01e7\7+")
        buf.write("\2\2\u01e7r\3\2\2\2\u01e8\u01e9\7}\2\2\u01e9t\3\2\2\2")
        buf.write("\u01ea\u01eb\7\177\2\2\u01ebv\3\2\2\2\u01ec\u01ed\7]\2")
        buf.write("\2\u01edx\3\2\2\2\u01ee\u01ef\7_\2\2\u01efz\3\2\2\2\u01f0")
        buf.write("\u01f1\7\60\2\2\u01f1\u01f2\7\60\2\2\u01f2|\3\2\2\2\u01f3")
        buf.write("\u01f4\7\60\2\2\u01f4~\3\2\2\2\u01f5\u01f6\7.\2\2\u01f6")
        buf.write("\u0080\3\2\2\2\u01f7\u01f8\7=\2\2\u01f8\u0082\3\2\2\2")
        buf.write("\u01f9\u01fa\7<\2\2\u01fa\u0084\3\2\2\2\u01fb\u01fc\7")
        buf.write("$\2\2\u01fc\u0086\3\2\2\2\u01fd\u0201\t\f\2\2\u01fe\u0200")
        buf.write("\t\r\2\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0088\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0204\u0206\7&\2\2\u0205\u0207\t")
        buf.write("\r\2\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u008a\3\2\2\2\u020a")
        buf.write("\u020c\t\16\2\2\u020b\u020a\3\2\2\2\u020c\u020d\3\2\2")
        buf.write("\2\u020d\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0210\bF\2\2\u0210\u008c\3\2\2\2\u0211")
        buf.write("\u0212\13\2\2\2\u0212\u0213\bG\3\2\u0213\u008e\3\2\2\2")
        buf.write("\u0214\u0218\7$\2\2\u0215\u0217\5\u0093J\2\u0216\u0215")
        buf.write("\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218")
        buf.write("\u0219\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2")
        buf.write("\u021b\u021d\t\17\2\2\u021c\u021b\3\2\2\2\u021d\u021e")
        buf.write("\3\2\2\2\u021e\u021f\bH\4\2\u021f\u0090\3\2\2\2\u0220")
        buf.write("\u0224\7$\2\2\u0221\u0223\5\u0093J\2\u0222\u0221\3\2\2")
        buf.write("\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2\u0224\u0225")
        buf.write("\3\2\2\2\u0225\u0227\3\2\2\2\u0226\u0224\3\2\2\2\u0227")
        buf.write("\u0228\5\u0097L\2\u0228\u0229\bI\5\2\u0229\u0092\3\2\2")
        buf.write("\2\u022a\u022d\n\20\2\2\u022b\u022d\5\u0095K\2\u022c\u022a")
        buf.write("\3\2\2\2\u022c\u022b\3\2\2\2\u022d\u0094\3\2\2\2\u022e")
        buf.write("\u022f\7^\2\2\u022f\u0230\t\21\2\2\u0230\u0096\3\2\2\2")
        buf.write("\u0231\u0232\7^\2\2\u0232\u0235\n\21\2\2\u0233\u0235\n")
        buf.write("\22\2\2\u0234\u0231\3\2\2\2\u0234\u0233\3\2\2\2\u0235")
        buf.write("\u0098\3\2\2\2%\2\u009d\u00ab\u00b1\u00b6\u00b9\u00be")
        buf.write("\u00c3\u00c6\u00cd\u00d2\u00d5\u00dc\u00e1\u00e4\u00e7")
        buf.write("\u00ed\u00f7\u00fa\u0103\u0107\u0109\u010d\u0113\u0115")
        buf.write("\u011f\u0124\u0201\u0208\u020d\u0218\u021c\u0224\u022c")
        buf.write("\u0234\6\b\2\2\3G\2\3H\3\3I\4")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_CMT = 1
    INT_LIT = 2
    FLOAT_LIT = 3
    BOOL_LIT = 4
    STR_LIT = 5
    DIGIT = 6
    BREAK = 7
    CONTINUE = 8
    IF = 9
    ELSEIF = 10
    ELSE = 11
    FOREACH = 12
    TRUE = 13
    FALSE = 14
    ARRAY = 15
    IN = 16
    INT = 17
    FLOAT = 18
    BOOLEAN = 19
    STRING = 20
    RETURN = 21
    NULL = 22
    CLASS = 23
    VAL = 24
    VAR = 25
    SELF = 26
    CONSTRUCTOR = 27
    DESTRUCTOR = 28
    NEW = 29
    BY = 30
    ADD = 31
    SUB = 32
    MUL = 33
    DIV = 34
    PRCNT = 35
    NOT = 36
    AND = 37
    OR = 38
    EQ = 39
    ASSIGN = 40
    NOT_EQ = 41
    LESS = 42
    LESS_EQ = 43
    GREAT = 44
    GREAT_EQ = 45
    EQ_STR = 46
    CONCAT_STR = 47
    STATIC_ACC = 48
    LB = 49
    RB = 50
    LP = 51
    RP = 52
    LSB = 53
    RSB = 54
    DOTDOT = 55
    DOT = 56
    CM = 57
    SEMI = 58
    CL = 59
    DOUBLEQUOTE = 60
    ID = 61
    STATIC_ID = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

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
            "BLOCK_CMT", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", 
            "DIGIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", "PRCNT", 
            "NOT", "AND", "OR", "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", 
            "GREAT", "GREAT_EQ", "EQ_STR", "CONCAT_STR", "STATIC_ACC", "LB", 
            "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", "DOT", "CM", "SEMI", 
            "CL", "DOUBLEQUOTE", "ID", "STATIC_ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCK_CMT", "CMT", "INT_LIT", "OCTAL", "DECIMAL", "HEX", 
                  "BINARY", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", "DIGIT", 
                  "EXPONENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "ADD", "SUB", "MUL", "DIV", "PRCNT", "NOT", "AND", "OR", 
                  "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", "GREAT", 
                  "GREAT_EQ", "EQ_STR", "CONCAT_STR", "STATIC_ACC", "LB", 
                  "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", "DOT", "CM", 
                  "SEMI", "CL", "DOUBLEQUOTE", "ID", "STATIC_ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STR_CHAR", 
                  "ESC_SEQ", "ESC_ILLEGAL" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[69] = self.ERROR_CHAR_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            	
            		raise ErrorToken(self.text)	
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		raise UncloseString(self.text[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		raise IllegalEscape(self.text[1:])
            	
     


