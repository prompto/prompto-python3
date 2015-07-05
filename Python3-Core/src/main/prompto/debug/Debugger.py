# class Debugger {
#
# 	Stack stack = new Stack()
# 	Object blocker = new Object()
# 	Status status = Status.STARTING;
# 	ResumeReason resumeReason;
# 	IDebugEventListener listener;
# 	// positive for stepping on enterXXX
# 	// negative for stepping on leaveXXX
# 	// necessary to avoid stepping twice on the same statement
# 	int stepDepth = 1;
# 	boolean suspended = False
# 	boolean terminated = False
#
# 	public static enum Status {
# 		STARTING,
# 		RUNNING,
# 		SUSPENDED,
# 		TERMINATING,
# 		TERMINATED;
#
# 		@Override
# 		public String toString():
# 			return name().substring(0,1) + name().substring(1).toLowerCase()
# 		}
# 	}
#
# 	public Stack getStack():
# 		return stack;
# 	}
#
# 	public Status getStatus():
# 		return status;
# 	}
#
# 	public void suspend():
# 		suspended = True
# 	}
#
# 	public boolean isTerminated():
# 		return status==Status.TERMINATED;
# 	}
#
# 	public void terminate():
# 		terminated = True
# 	}
#
# 	public IDebugEventListener getListener():
# 		return listener;
# 	}
#
# 	public void setListener(IDebugEventListener listener):
# 		self.listener = listener;
# 	}
#
# 	public void enterMethod(self, context, IMethodDeclaration method):
# 		terminateIfRequested()
# 		stack.push(new StackFrame(context, method.getName(), method))
# 		if(stack.size()>0 && stack.size()<=stepDepth)
# 			suspend(SuspendReason.STEPPING, context, method)
# 		elif(method.isBreakpoint())
# 			suspend(SuspendReason.BREAKPOINT, context, method)
# 		else
# 			suspendIfRequested(context, method)
# 		terminateIfRequested()
# 	}
#
# 	public void leaveMethod(self, context, ISection section):
# 		terminateIfRequested()
# 		if(stack.size()>0 && stack.size()==-stepDepth)
# 			suspend(SuspendReason.STEPPING, context, section)
# 		else
# 			suspendIfRequested(context, section)
# 		stack.pop()
# 		terminateIfRequested()
# 	}
#
# 	public void enterStatement(self, context, ISection section):
# 		terminateIfRequested()
# 		StackFrame previous = stack.pop()
# 		stack.push(new StackFrame(context, previous.getMethodName(), section))
# 		if(stack.size()>0 && stack.size()<=stepDepth)
# 			suspend(SuspendReason.STEPPING, context, section)
# 		elif(section.isBreakpoint())
# 			suspend(SuspendReason.BREAKPOINT, context, section)
# 		else
# 			suspendIfRequested(context, section)
# 		terminateIfRequested()
# 	}
#
# 	public void leaveStatement(self, context, ISection section):
# 		terminateIfRequested()
# 		if(stack.size()>0 && stack.size()==-stepDepth)
# 			suspend(SuspendReason.STEPPING, context, section)
# 		else
# 			suspendIfRequested(context, section)
# 		terminateIfRequested()
# 	}
#
# 	private void terminateIfRequested() throws TerminatedError {
# 		if(terminated):
# 			status = Status.TERMINATING;
# 			raise TerminatedError()
# 		}
# 	}
#
# 	private void suspendIfRequested(self, context, ISection section):
# 		if(suspended):
# 			suspended = False
# 			suspend(SuspendReason.SUSPENDED, context, section)
# 		}
#
# 	}
#
# 	public void suspend(SuspendReason reason, final Context context, ISection section):
# 		synchronized(blocker):
# 			status = Status.SUSPENDED;
# 			if(listener is not None)
# 				listener.handleSuspendEvent(reason, context, section)
# 			try:
# 				blocker.wait()
# 			except InterruptedException e):
# 				// TODO Auto-generated catch block
# 				e.printStackTrace()
# 			} finally {
# 				status = Status.RUNNING;
# 				if(listener is not None)
# 					listener.handleResumeEvent(resumeReason, context, section)
# 			}
# 		}
# 	}
#
# 	public boolean isStepping():
# 		return stepDepth!=0;
# 	}
#
# 	public boolean canSuspend():
# 		return !isSuspended()
# 	}
#
# 	public boolean isSuspended():
# 		return status==Status.SUSPENDED;
# 	}
#
# 	public boolean canResume():
# 		return isSuspended()
# 	}
#
# 	public void resume():
# 		stepDepth = 0;
# 		doResume(ResumeReason.RESUMED)
# 	}
#
# 	public boolean canStepOver():
# 		return isSuspended()
# 	}
#
# 	public void stepOver():
# 		stepDepth = stack.size()
# 		doResume(ResumeReason.STEP_OVER)
# 	}
#
# 	public boolean canStepInto():
# 		return isSuspended()
# 	}
#
# 	public void stepInto():
# 		stepDepth = Math.abs(stepDepth) + 1;
# 		doResume(ResumeReason.STEP_INTO)
# 	}
#
# 	public boolean canStepOut():
# 		return isSuspended()
# 	}
#
# 	public void stepOut():
# 		stepDepth = -(Math.abs(stepDepth) - 1)
# 		doResume(ResumeReason.STEP_OUT)
# 	}
#
# 	public void doResume(ResumeReason reason):
# 		self.resumeReason = reason;
# 		synchronized(blocker):
# 			blocker.notify()
# 		}
# 	}
#
# 	public int getLine():
# 		StackFrame frame = stack.peek()
# 		return frame is None ? -1 : frame.getLine()
# 	}
#
# 	public void terminated():
# 		status = Status.TERMINATED;
# 		if(listener is not None)
# 			listener.handleTerminateEvent()
# 	}
#
# }
