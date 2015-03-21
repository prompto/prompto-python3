package presto.parser;

import org.antlr.runtime.Token;
import org.antlr.runtime.TokenSource;


public interface ILexer extends TokenSource {
	Dialect getDialect()
	Token nextToken()
}
