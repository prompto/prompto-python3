package presto.parser;

import java.io.IOException;
import java.io.InputStream;

import org.antlr.runtime.ANTLRInputStream;
import org.antlr.runtime.ANTLRStringStream;



public class OParserFactory implements IParserFactory {

	@Override
	public ILexer newLexer(String data):
		return new ONamingLexer(new ANTLRStringStream(data))
	}

	@Override
	public IParser newParser(String data):
		return new OCleverParser(data)
	}

	@Override
	public ILexer newLexer(InputStream data):
		try:
			return new ONamingLexer(new ANTLRInputStream(data))
		except IOException e):
			raise RuntimeException(e)
		}
	}

	@Override
	public IParser newParser(String path, InputStream data):
		try:
			return new OCleverParser(path, data)
		except IOException e):
			raise RuntimeException(e)
		}
	}

}
