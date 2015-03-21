# package presto.debug;
#
# import static org.junit.Assert.assertEquals;
#
# import java.lang.Thread.State;
#
# import org.junit.After;
# import org.junit.Before;
# import unittest
#
# import presto.debug.Debugger;
# import presto.debug.Debugger.Status;
# import presto.declaration.ConcreteMethodDeclaration;
# import presto.error.PrestoError;
# import presto.parser.ISection;
# import presto.parser.e.BaseEParserTest;
# import presto.runtime.Context;
# import presto.runtime.Interpreter;
# import presto.runtime.Context.MethodDeclarationMap;
# import presto.runtime.utils.Out;
#
#
# public class TestDebugger extends BaseEParserTest {
#
# 	protected Thread thread; // in debug mode
# 	protected Debugger debugger;
#
# 	@Before
# 	def setUp(self):
# 		Out.init()
# 	}
#
# 	@After
# 	def tearDown(self):
# 		Out.restore()
# 	}
#
# 	protected void debugResource(String resourceName) throws Exception {
# 		loadResource(resourceName)
# 		debugger = new Debugger()
# 		final Context local = context.newLocalContext()
# 		local.setDebugger(debugger)
# 		thread = new Thread(new Runnable():
# 			@Override
# 			public void run():
# 				try:
# 					Interpreter.interpretMainNoArgs(local)
# 				except PrestoError e):
# 					// TODO Auto-generated catch block
# 				}
# 			}
# 		})
#
# 	}
#
# 	void waitBlocked() throws InterruptedException {
# 		while(thread.getState()!=State.WAITING)
# 			Thread.sleep(10)
# 	}
#
# 	@Test
# 	def testStackNoDebug(self):
# 		runResource("e/debug/stack.e")
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# 	@Test
# 	def testResume(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# 	@Test
# 	def testStepOver(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(17, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(18, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# 	@Test
# 	def testStepInto(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(17, debugger.getLine())
# 		debugger.stepInto() // printLevel1
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(12, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(13, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# 	@Test
# 	def testSilentStepInto(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(17, debugger.getLine())
# 		debugger.stepInto() // printLevel1
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(12, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(13, debugger.getLine())
# 		debugger.stepInto() // value = value + "1", should step over
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(14, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
#
# 	@Test
# 	def testStepOut(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(17, debugger.getLine())
# 		debugger.stepInto() // printLevel1
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(12, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(13, debugger.getLine())
# 		debugger.stepOver()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(14, debugger.getLine())
# 		debugger.stepInto() // printLevel2
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(8, debugger.getLine())
# 		debugger.stepOut() // printLevel1
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(14, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# 	@Test
# 	def testBreakpoint(self):
# 		debugResource("e/debug/stack.e")
# 		thread.start()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(16, debugger.getLine())
# 		MethodDeclarationMap mdm = context.getRegisteredDeclaration(MethodDeclarationMap.class, "printLevel2")
# 		ConcreteMethodDeclaration cmd = (ConcreteMethodDeclaration)mdm.values().iterator().next()
# 		ISection section = cmd.getStatements().get(0)
# 		assertEquals(9, section.getStart().getLine())
# 		section.setAsBreakpoint(True)
# 		debugger.resume()
# 		waitBlocked()
# 		assertEquals(Status.SUSPENDED, debugger.getStatus())
# 		assertEquals(9, debugger.getLine())
# 		debugger.resume()
# 		thread.join()
# 		assertEquals("test123-ok", Out.read())
# 	}
#
# }
