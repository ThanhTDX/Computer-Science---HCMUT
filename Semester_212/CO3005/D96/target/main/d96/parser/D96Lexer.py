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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u021f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3-\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\39\39\59\u0185")
        buf.write("\n9\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\5:\u0193\n:\3")
        buf.write(";\3;\5;\u0197\n;\6;\u0199\n;\r;\16;\u019a\3<\3<\3<\5<")
        buf.write("\u01a0\n<\6<\u01a2\n<\r<\16<\u01a3\3=\3=\3=\3=\5=\u01aa")
        buf.write("\n=\6=\u01ac\n=\r=\16=\u01ad\3>\3>\3>\3>\5>\u01b4\n>\6")
        buf.write(">\u01b6\n>\r>\16>\u01b7\3?\3?\3?\7?\u01bd\n?\f?\16?\u01c0")
        buf.write("\13?\3?\5?\u01c3\n?\3?\3?\3@\3@\5@\u01c9\n@\3A\3A\3A\3")
        buf.write("A\3A\3B\3B\3C\3C\3C\5C\u01d5\nC\3C\6C\u01d8\nC\rC\16C")
        buf.write("\u01d9\3D\3D\7D\u01de\nD\fD\16D\u01e1\13D\3E\3E\6E\u01e5")
        buf.write("\nE\rE\16E\u01e6\3F\3F\3F\3F\5F\u01ed\nF\3G\3G\3G\3G\3")
        buf.write("G\3H\6H\u01f5\nH\rH\16H\u01f6\3H\3H\3I\3I\3I\3J\3J\7J")
        buf.write("\u0200\nJ\fJ\16J\u0203\13J\3J\5J\u0206\nJ\3J\3J\3K\3K")
        buf.write("\7K\u020c\nK\fK\16K\u020f\13K\3K\3K\3K\3L\3L\5L\u0216")
        buf.write("\nL\3M\3M\3M\3N\3N\3N\5N\u021e\nN\3\u00a1\2O\3\3\5\2\7")
        buf.write("\4\t\5\13\6\r\7\17\b\21\t\23\n\25\13\27\f\31\r\33\16\35")
        buf.write("\17\37\20!\21#\22%\23\'\24)\25+\26-\27/\30\61\31\63\32")
        buf.write("\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y")
        buf.write("-[.]/_\60a\61c\62e\63g\64i\65k\66m\67o8q9s:u\2w\2y\2{")
        buf.write("\2};\177<\u0081=\u0083>\u0085\2\u0087?\u0089@\u008bA\u008d")
        buf.write("B\u008fC\u0091D\u0093E\u0095F\u0097\2\u0099\2\u009b\2")
        buf.write("\3\2\21\3\2\62\62\3\2\629\4\2ZZzz\4\2\62;CH\4\2DDdd\4")
        buf.write("\2\62\63aa\3\2\62;\4\2GGgg\5\2C\\aac|\6\2\62;C\\aac|\5")
        buf.write("\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\7\2\n\f\16\17$$")
        buf.write("))^^\n\2$$))^^ddhhppttvv\3\2^^\2\u0234\2\3\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2")
        buf.write("\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2")
        buf.write("\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u009d\3\2\2\2\5\u00a8\3\2\2\2\7\u00ab\3\2\2")
        buf.write("\2\t\u00b1\3\2\2\2\13\u00ba\3\2\2\2\r\u00bd\3\2\2\2\17")
        buf.write("\u00c4\3\2\2\2\21\u00c9\3\2\2\2\23\u00d1\3\2\2\2\25\u00d6")
        buf.write("\3\2\2\2\27\u00dc\3\2\2\2\31\u00e2\3\2\2\2\33\u00e5\3")
        buf.write("\2\2\2\35\u00e9\3\2\2\2\37\u00ef\3\2\2\2!\u00f7\3\2\2")
        buf.write("\2#\u00fe\3\2\2\2%\u0105\3\2\2\2\'\u010a\3\2\2\2)\u0110")
        buf.write("\3\2\2\2+\u0114\3\2\2\2-\u0118\3\2\2\2/\u011d\3\2\2\2")
        buf.write("\61\u0129\3\2\2\2\63\u0134\3\2\2\2\65\u0137\3\2\2\2\67")
        buf.write("\u0139\3\2\2\29\u013b\3\2\2\2;\u013d\3\2\2\2=\u013f\3")
        buf.write("\2\2\2?\u0141\3\2\2\2A\u0143\3\2\2\2C\u0146\3\2\2\2E\u0149")
        buf.write("\3\2\2\2G\u014c\3\2\2\2I\u014e\3\2\2\2K\u0151\3\2\2\2")
        buf.write("M\u0153\3\2\2\2O\u0156\3\2\2\2Q\u0158\3\2\2\2S\u015b\3")
        buf.write("\2\2\2U\u015f\3\2\2\2W\u0162\3\2\2\2Y\u0165\3\2\2\2[\u0169")
        buf.write("\3\2\2\2]\u016b\3\2\2\2_\u016d\3\2\2\2a\u016f\3\2\2\2")
        buf.write("c\u0171\3\2\2\2e\u0173\3\2\2\2g\u0175\3\2\2\2i\u0178\3")
        buf.write("\2\2\2k\u017a\3\2\2\2m\u017c\3\2\2\2o\u017e\3\2\2\2q\u0184")
        buf.write("\3\2\2\2s\u0192\3\2\2\2u\u0198\3\2\2\2w\u019c\3\2\2\2")
        buf.write("y\u01a5\3\2\2\2{\u01af\3\2\2\2}\u01b9\3\2\2\2\177\u01c8")
        buf.write("\3\2\2\2\u0081\u01ca\3\2\2\2\u0083\u01cf\3\2\2\2\u0085")
        buf.write("\u01d1\3\2\2\2\u0087\u01db\3\2\2\2\u0089\u01e2\3\2\2\2")
        buf.write("\u008b\u01ec\3\2\2\2\u008d\u01ee\3\2\2\2\u008f\u01f4\3")
        buf.write("\2\2\2\u0091\u01fa\3\2\2\2\u0093\u01fd\3\2\2\2\u0095\u0209")
        buf.write("\3\2\2\2\u0097\u0215\3\2\2\2\u0099\u0217\3\2\2\2\u009b")
        buf.write("\u021d\3\2\2\2\u009d\u00a1\5\5\3\2\u009e\u00a0\13\2\2")
        buf.write("\2\u009f\u009e\3\2\2\2\u00a0\u00a3\3\2\2\2\u00a1\u00a2")
        buf.write("\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a4\3\2\2\2\u00a3")
        buf.write("\u00a1\3\2\2\2\u00a4\u00a5\5\5\3\2\u00a5\u00a6\3\2\2\2")
        buf.write("\u00a6\u00a7\b\2\2\2\u00a7\4\3\2\2\2\u00a8\u00a9\7%\2")
        buf.write("\2\u00a9\u00aa\7%\2\2\u00aa\6\3\2\2\2\u00ab\u00ac\7D\2")
        buf.write("\2\u00ac\u00ad\7t\2\2\u00ad\u00ae\7g\2\2\u00ae\u00af\7")
        buf.write("c\2\2\u00af\u00b0\7m\2\2\u00b0\b\3\2\2\2\u00b1\u00b2\7")
        buf.write("E\2\2\u00b2\u00b3\7q\2\2\u00b3\u00b4\7p\2\2\u00b4\u00b5")
        buf.write("\7v\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8")
        buf.write("\7w\2\2\u00b8\u00b9\7g\2\2\u00b9\n\3\2\2\2\u00ba\u00bb")
        buf.write("\7K\2\2\u00bb\u00bc\7h\2\2\u00bc\f\3\2\2\2\u00bd\u00be")
        buf.write("\7G\2\2\u00be\u00bf\7n\2\2\u00bf\u00c0\7u\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7h\2\2\u00c3\16")
        buf.write("\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7")
        buf.write("\7u\2\2\u00c7\u00c8\7g\2\2\u00c8\20\3\2\2\2\u00c9\u00ca")
        buf.write("\7H\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd")
        buf.write("\7g\2\2\u00cd\u00ce\7c\2\2\u00ce\u00cf\7e\2\2\u00cf\u00d0")
        buf.write("\7j\2\2\u00d0\22\3\2\2\2\u00d1\u00d2\7V\2\2\u00d2\u00d3")
        buf.write("\7t\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7g\2\2\u00d5\24")
        buf.write("\3\2\2\2\u00d6\u00d7\7H\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9")
        buf.write("\7n\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db\26")
        buf.write("\3\2\2\2\u00dc\u00dd\7C\2\2\u00dd\u00de\7t\2\2\u00de\u00df")
        buf.write("\7t\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7{\2\2\u00e1\30")
        buf.write("\3\2\2\2\u00e2\u00e3\7K\2\2\u00e3\u00e4\7p\2\2\u00e4\32")
        buf.write("\3\2\2\2\u00e5\u00e6\7K\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\34\3\2\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb")
        buf.write("\7n\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7D\2\2\u00f0\u00f1")
        buf.write("\7q\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7p\2\2\u00f6 \3")
        buf.write("\2\2\2\u00f7\u00f8\7U\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7i\2\2\u00fd\"\3\2\2\2\u00fe\u00ff\7T\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\u0101\7v\2\2\u0101\u0102\7w\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7p\2\2\u0104$\3\2\2\2\u0105\u0106")
        buf.write("\7P\2\2\u0106\u0107\7w\2\2\u0107\u0108\7n\2\2\u0108\u0109")
        buf.write("\7n\2\2\u0109&\3\2\2\2\u010a\u010b\7E\2\2\u010b\u010c")
        buf.write("\7n\2\2\u010c\u010d\7c\2\2\u010d\u010e\7u\2\2\u010e\u010f")
        buf.write("\7u\2\2\u010f(\3\2\2\2\u0110\u0111\7X\2\2\u0111\u0112")
        buf.write("\7c\2\2\u0112\u0113\7n\2\2\u0113*\3\2\2\2\u0114\u0115")
        buf.write("\7X\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117,\3")
        buf.write("\2\2\2\u0118\u0119\7U\2\2\u0119\u011a\7g\2\2\u011a\u011b")
        buf.write("\7n\2\2\u011b\u011c\7h\2\2\u011c.\3\2\2\2\u011d\u011e")
        buf.write("\7E\2\2\u011e\u011f\7q\2\2\u011f\u0120\7p\2\2\u0120\u0121")
        buf.write("\7u\2\2\u0121\u0122\7v\2\2\u0122\u0123\7t\2\2\u0123\u0124")
        buf.write("\7w\2\2\u0124\u0125\7e\2\2\u0125\u0126\7v\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7t\2\2\u0128\60\3\2\2\2\u0129\u012a")
        buf.write("\7F\2\2\u012a\u012b\7g\2\2\u012b\u012c\7u\2\2\u012c\u012d")
        buf.write("\7v\2\2\u012d\u012e\7t\2\2\u012e\u012f\7w\2\2\u012f\u0130")
        buf.write("\7e\2\2\u0130\u0131\7v\2\2\u0131\u0132\7q\2\2\u0132\u0133")
        buf.write("\7t\2\2\u0133\62\3\2\2\2\u0134\u0135\7D\2\2\u0135\u0136")
        buf.write("\7{\2\2\u0136\64\3\2\2\2\u0137\u0138\7-\2\2\u0138\66\3")
        buf.write("\2\2\2\u0139\u013a\7/\2\2\u013a8\3\2\2\2\u013b\u013c\7")
        buf.write(",\2\2\u013c:\3\2\2\2\u013d\u013e\7\61\2\2\u013e<\3\2\2")
        buf.write("\2\u013f\u0140\7\'\2\2\u0140>\3\2\2\2\u0141\u0142\7#\2")
        buf.write("\2\u0142@\3\2\2\2\u0143\u0144\7(\2\2\u0144\u0145\7(\2")
        buf.write("\2\u0145B\3\2\2\2\u0146\u0147\7~\2\2\u0147\u0148\7~\2")
        buf.write("\2\u0148D\3\2\2\2\u0149\u014a\7?\2\2\u014a\u014b\7?\2")
        buf.write("\2\u014bF\3\2\2\2\u014c\u014d\7?\2\2\u014dH\3\2\2\2\u014e")
        buf.write("\u014f\7#\2\2\u014f\u0150\7?\2\2\u0150J\3\2\2\2\u0151")
        buf.write("\u0152\7>\2\2\u0152L\3\2\2\2\u0153\u0154\7>\2\2\u0154")
        buf.write("\u0155\7?\2\2\u0155N\3\2\2\2\u0156\u0157\7@\2\2\u0157")
        buf.write("P\3\2\2\2\u0158\u0159\7@\2\2\u0159\u015a\7?\2\2\u015a")
        buf.write("R\3\2\2\2\u015b\u015c\7?\2\2\u015c\u015d\7?\2\2\u015d")
        buf.write("\u015e\7\60\2\2\u015eT\3\2\2\2\u015f\u0160\7-\2\2\u0160")
        buf.write("\u0161\7\60\2\2\u0161V\3\2\2\2\u0162\u0163\7<\2\2\u0163")
        buf.write("\u0164\7<\2\2\u0164X\3\2\2\2\u0165\u0166\7P\2\2\u0166")
        buf.write("\u0167\7g\2\2\u0167\u0168\7y\2\2\u0168Z\3\2\2\2\u0169")
        buf.write("\u016a\7*\2\2\u016a\\\3\2\2\2\u016b\u016c\7+\2\2\u016c")
        buf.write("^\3\2\2\2\u016d\u016e\7}\2\2\u016e`\3\2\2\2\u016f\u0170")
        buf.write("\7\177\2\2\u0170b\3\2\2\2\u0171\u0172\7]\2\2\u0172d\3")
        buf.write("\2\2\2\u0173\u0174\7_\2\2\u0174f\3\2\2\2\u0175\u0176\7")
        buf.write("\60\2\2\u0176\u0177\7\60\2\2\u0177h\3\2\2\2\u0178\u0179")
        buf.write("\7\60\2\2\u0179j\3\2\2\2\u017a\u017b\7.\2\2\u017bl\3\2")
        buf.write("\2\2\u017c\u017d\7=\2\2\u017dn\3\2\2\2\u017e\u017f\7<")
        buf.write("\2\2\u017fp\3\2\2\2\u0180\u0185\5s:\2\u0181\u0185\5}?")
        buf.write("\2\u0182\u0185\5\177@\2\u0183\u0185\5\u0081A\2\u0184\u0180")
        buf.write("\3\2\2\2\u0184\u0181\3\2\2\2\u0184\u0182\3\2\2\2\u0184")
        buf.write("\u0183\3\2\2\2\u0185r\3\2\2\2\u0186\u0187\5u;\2\u0187")
        buf.write("\u0188\b:\3\2\u0188\u0193\3\2\2\2\u0189\u018a\5w<\2\u018a")
        buf.write("\u018b\b:\4\2\u018b\u0193\3\2\2\2\u018c\u018d\5y=\2\u018d")
        buf.write("\u018e\b:\5\2\u018e\u0193\3\2\2\2\u018f\u0190\5{>\2\u0190")
        buf.write("\u0191\b:\6\2\u0191\u0193\3\2\2\2\u0192\u0186\3\2\2\2")
        buf.write("\u0192\u0189\3\2\2\2\u0192\u018c\3\2\2\2\u0192\u018f\3")
        buf.write("\2\2\2\u0193t\3\2\2\2\u0194\u0196\5\u0083B\2\u0195\u0197")
        buf.write("\7a\2\2\u0196\u0195\3\2\2\2\u0196\u0197\3\2\2\2\u0197")
        buf.write("\u0199\3\2\2\2\u0198\u0194\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019bv\3\2\2")
        buf.write("\2\u019c\u01a1\t\2\2\2\u019d\u019f\t\3\2\2\u019e\u01a0")
        buf.write("\7a\2\2\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u01a2\3\2\2\2\u01a1\u019d\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4x\3\2\2")
        buf.write("\2\u01a5\u01a6\t\2\2\2\u01a6\u01ab\t\4\2\2\u01a7\u01a9")
        buf.write("\t\5\2\2\u01a8\u01aa\7a\2\2\u01a9\u01a8\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a7\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3")
        buf.write("\2\2\2\u01aez\3\2\2\2\u01af\u01b0\t\2\2\2\u01b0\u01b5")
        buf.write("\t\6\2\2\u01b1\u01b3\t\7\2\2\u01b2\u01b4\7a\2\2\u01b3")
        buf.write("\u01b2\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2")
        buf.write("\u01b5\u01b1\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3")
        buf.write("\2\2\2\u01b7\u01b8\3\2\2\2\u01b8|\3\2\2\2\u01b9\u01ba")
        buf.write("\5u;\2\u01ba\u01be\5i\65\2\u01bb\u01bd\5\u0083B\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bd\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2")
        buf.write("\u01be\u01bf\3\2\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01be\3")
        buf.write("\2\2\2\u01c1\u01c3\5\u0085C\2\u01c2\u01c1\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\b?\7\2")
        buf.write("\u01c5~\3\2\2\2\u01c6\u01c9\5\23\n\2\u01c7\u01c9\5\25")
        buf.write("\13\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2\u01c9\u0080")
        buf.write("\3\2\2\2\u01ca\u01cb\7$\2\2\u01cb\u01cc\5\u0097L\2\u01cc")
        buf.write("\u01cd\7$\2\2\u01cd\u01ce\bA\b\2\u01ce\u0082\3\2\2\2\u01cf")
        buf.write("\u01d0\t\b\2\2\u01d0\u0084\3\2\2\2\u01d1\u01d4\t\t\2\2")
        buf.write("\u01d2\u01d5\5\65\33\2\u01d3\u01d5\5\67\34\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d3\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5")
        buf.write("\u01d7\3\2\2\2\u01d6\u01d8\5\u0083B\2\u01d7\u01d6\3\2")
        buf.write("\2\2\u01d8\u01d9\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01da\u0086\3\2\2\2\u01db\u01df\t\n\2\2\u01dc")
        buf.write("\u01de\t\13\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2")
        buf.write("\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u0088")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e4\7&\2\2\u01e3")
        buf.write("\u01e5\t\13\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e6\3\2\2")
        buf.write("\2\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u008a")
        buf.write("\3\2\2\2\u01e8\u01ed\5\33\16\2\u01e9\u01ed\5\35\17\2\u01ea")
        buf.write("\u01ed\5\37\20\2\u01eb\u01ed\5!\21\2\u01ec\u01e8\3\2\2")
        buf.write("\2\u01ec\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u008c\3\2\2\2\u01ee\u01ef\5Y-\2\u01ef\u01f0")
        buf.write("\5\u0087D\2\u01f0\u01f1\5[.\2\u01f1\u01f2\5]/\2\u01f2")
        buf.write("\u008e\3\2\2\2\u01f3\u01f5\t\f\2\2\u01f4\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3")
        buf.write("\2\2\2\u01f7\u01f8\3\2\2\2\u01f8\u01f9\bH\2\2\u01f9\u0090")
        buf.write("\3\2\2\2\u01fa\u01fb\13\2\2\2\u01fb\u01fc\bI\t\2\u01fc")
        buf.write("\u0092\3\2\2\2\u01fd\u0201\7$\2\2\u01fe\u0200\5\u0097")
        buf.write("L\2\u01ff\u01fe\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0205\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0204\u0206\t\r\2\2\u0205\u0204\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0208\bJ\n\2\u0208\u0094\3")
        buf.write("\2\2\2\u0209\u020d\7$\2\2\u020a\u020c\5\u0097L\2\u020b")
        buf.write("\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d\u020b\3\2\2\2")
        buf.write("\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2\u020f\u020d\3")
        buf.write("\2\2\2\u0210\u0211\5\u009bN\2\u0211\u0212\bK\13\2\u0212")
        buf.write("\u0096\3\2\2\2\u0213\u0216\n\16\2\2\u0214\u0216\5\u0099")
        buf.write("M\2\u0215\u0213\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u0098")
        buf.write("\3\2\2\2\u0217\u0218\7^\2\2\u0218\u0219\t\17\2\2\u0219")
        buf.write("\u009a\3\2\2\2\u021a\u021b\7^\2\2\u021b\u021e\n\17\2\2")
        buf.write("\u021c\u021e\n\20\2\2\u021d\u021a\3\2\2\2\u021d\u021c")
        buf.write("\3\2\2\2\u021e\u009c\3\2\2\2\34\2\u00a1\u0184\u0192\u0196")
        buf.write("\u019a\u019f\u01a3\u01a9\u01ad\u01b3\u01b7\u01be\u01c2")
        buf.write("\u01c8\u01d4\u01d9\u01df\u01e6\u01ec\u01f6\u0201\u0205")
        buf.write("\u020d\u0215\u021d\f\b\2\2\3:\2\3:\3\3:\4\3:\5\3?\6\3")
        buf.write("A\7\3I\b\3J\t\3K\n")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    BREAK = 2
    CONTINUE = 3
    IF = 4
    ELSEIF = 5
    ELSE = 6
    FOREACH = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    SELF = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    BY = 24
    ADD = 25
    SUB_OP = 26
    MUL = 27
    DIV = 28
    PRCNT = 29
    NOT = 30
    AND = 31
    OR = 32
    EQ = 33
    ASSIGN = 34
    NOT_EQ = 35
    LESS = 36
    LESS_EQ = 37
    GREAT = 38
    GREAT_EQ = 39
    EQ_STR = 40
    CONCAT_STR = 41
    STATIC_ACC = 42
    OBJ_CREATE = 43
    LB = 44
    RB = 45
    LP = 46
    RP = 47
    LSB = 48
    RSB = 49
    DOTDOT = 50
    DOT = 51
    CM = 52
    SEMI = 53
    CL = 54
    LITERAL = 55
    INT_LIT = 56
    FLOAT_LIT = 57
    BOOL_LIT = 58
    STR_LIT = 59
    DIGIT = 60
    ID = 61
    STATIC_ID = 62
    PRIMITIVE_TYPE = 63
    CLASS_TYPE = 64
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
            "'Var'", "'Self'", "'Constructor'", "'Destructor'", "'By'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'='", "'!='", "'<'", "'<='", "'>'", "'>='", "'==.'", "'+.'", 
            "'::'", "'New'", "'('", "')'", "'{'", "'}'", "'['", "']'", "'..'", 
            "'.'", "','", "';'", "':'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
            "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
            "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "SELF", "CONSTRUCTOR", 
            "DESTRUCTOR", "BY", "ADD", "SUB_OP", "MUL", "DIV", "PRCNT", 
            "NOT", "AND", "OR", "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", 
            "GREAT", "GREAT_EQ", "EQ_STR", "CONCAT_STR", "STATIC_ACC", "OBJ_CREATE", 
            "LB", "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", "DOT", "CM", 
            "SEMI", "CL", "LITERAL", "INT_LIT", "FLOAT_LIT", "BOOL_LIT", 
            "STR_LIT", "DIGIT", "ID", "STATIC_ID", "PRIMITIVE_TYPE", "CLASS_TYPE", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "BLOCK_COMMENT", "CMT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "SELF", "CONSTRUCTOR", "DESTRUCTOR", "BY", 
                  "ADD", "SUB_OP", "MUL", "DIV", "PRCNT", "NOT", "AND", 
                  "OR", "EQ", "ASSIGN", "NOT_EQ", "LESS", "LESS_EQ", "GREAT", 
                  "GREAT_EQ", "EQ_STR", "CONCAT_STR", "STATIC_ACC", "OBJ_CREATE", 
                  "LB", "RB", "LP", "RP", "LSB", "RSB", "DOTDOT", "DOT", 
                  "CM", "SEMI", "CL", "LITERAL", "INT_LIT", "DECIMAL", "OCTAL", 
                  "HEX", "BINARY", "FLOAT_LIT", "BOOL_LIT", "STR_LIT", "DIGIT", 
                  "EXPONENT", "ID", "STATIC_ID", "PRIMITIVE_TYPE", "CLASS_TYPE", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL" ]

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
            actions[56] = self.INT_LIT_action 
            actions[61] = self.FLOAT_LIT_action 
            actions[63] = self.STR_LIT_action 
            actions[71] = self.ERROR_CHAR_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

        if actionIndex == 2:
            self.text = self.text.replace('_','')
     

        if actionIndex == 3:
            self.text = self.text.replace('_','')
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('_','')
     

    def STR_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            	raise ErrorToken(self.text)	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
             raise UncloseString(self.text) 
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            		raise IllegalEscape(self.text)
            	
     


