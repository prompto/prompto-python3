package presto.parser;

import java.io.IOException;
import java.io.InputStream;

import org.antlr.runtime.ANTLRInputStream;
import org.antlr.runtime.ANTLRStringStream;



public class EParserFactory implements IParserFactory {

	@Override
	public ILexer newLexer(String data):
		return new EIndentingLexer(new ANTLRStringStream(data))
	}

	@Override
	public IParser newParser(String data):
		return new ECleverParser(data)
	}

	@Override
	public ILexer newLexer(InputStream data):
		try:
			return new EIndentingLexer(new ANTLRInputStream(data))
		except IOException e):
			raise RuntimeException(e)
		}
	}

	@Override
	public IParser newParser(String path, InputStream data):
		try:
			return new ECleverParser(path, data)
		except IOException e):
			raise RuntimeException(e)
		}
	}

}
