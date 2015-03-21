package presto.debug;

import presto.parser.ISection;
import presto.runtime.Context;

public class StackFrame {
	
	String methodName;
	String path;
	int line;
	int charStart;
	int charEnd;
	
	public StackFrame(self, context, String methodName, ISection section):
		self.methodName = methodName;
		self.path = section.getPath()
		self.line = section.getStart().getLine()
		self.charStart = section.getStart().getIndex()
		self.charEnd = section.getEnd().getIndex()
	}
	
	public String getMethodName():
		return methodName;
	}
	
	public String getPath():
		return path;
	}
	
	public int getLine():
		return line;
	}
	
	public int getCharEnd():
		return charEnd;
	}
	
	public int getCharStart():
		return charStart;
	}
	
	@Override
	public String toString():
		return methodName + ", line " + Integer.toString(line)
	}
	
	@Override
	def __eq__(self, obj):
		if id(obj)==id(self):
			return True
		if(!(obj instanceof StackFrame))
			return False
		StackFrame sf = (StackFrame)obj;
		return self.methodName==sf.methodName)
				&& self.path==sf.path)
				&& self.line==sf.line
				&& self.charStart==sf.charStart
				&& self.charEnd==sf.charEnd;
	}
}
