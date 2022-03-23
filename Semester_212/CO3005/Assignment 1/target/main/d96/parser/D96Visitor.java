// Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link D96Parser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface D96Visitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link D96Parser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(D96Parser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#class_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_decl(D96Parser.Class_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#mem_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMem_list(D96Parser.Mem_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#attri_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttri_decl(D96Parser.Attri_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#attri_decl_wo_assign}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttri_decl_wo_assign(D96Parser.Attri_decl_wo_assignContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#attri_decl_w_assign}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttri_decl_w_assign(D96Parser.Attri_decl_w_assignContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#attri_recurse}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAttri_recurse(D96Parser.Attri_recurseContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#id_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitId_list(D96Parser.Id_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#method_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod_decl(D96Parser.Method_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#param_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam_list(D96Parser.Param_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr_list}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr_list(D96Parser.Expr_listContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr(D96Parser.ExprContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr1}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr1(D96Parser.Expr1Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr2}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr2(D96Parser.Expr2Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr3}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr3(D96Parser.Expr3Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr4}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr4(D96Parser.Expr4Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr5}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr5(D96Parser.Expr5Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr6}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr6(D96Parser.Expr6Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr7}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr7(D96Parser.Expr7Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#idx_op}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdx_op(D96Parser.Idx_opContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr8}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr8(D96Parser.Expr8Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr9}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr9(D96Parser.Expr9Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr10}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr10(D96Parser.Expr10Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#expr11}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpr11(D96Parser.Expr11Context ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#operand}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperand(D96Parser.OperandContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#func_call}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunc_call(D96Parser.Func_callContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStmt(D96Parser.StmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#var_const_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_const_stmt(D96Parser.Var_const_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#assign_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssign_stmt(D96Parser.Assign_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#if_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIf_stmt(D96Parser.If_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#for_in_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFor_in_stmt(D96Parser.For_in_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#break_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBreak_stmt(D96Parser.Break_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#cont_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCont_stmt(D96Parser.Cont_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#rtrn_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRtrn_stmt(D96Parser.Rtrn_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#method_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMethod_stmt(D96Parser.Method_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#block_stmt}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitBlock_stmt(D96Parser.Block_stmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#idx_arr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdx_arr(D96Parser.Idx_arrContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#mul_dim_arr}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMul_dim_arr(D96Parser.Mul_dim_arrContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#data_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitData_type(D96Parser.Data_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#array_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArray_type(D96Parser.Array_typeContext ctx);
	/**
	 * Visit a parse tree produced by {@link D96Parser#class_type}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitClass_type(D96Parser.Class_typeContext ctx);
}