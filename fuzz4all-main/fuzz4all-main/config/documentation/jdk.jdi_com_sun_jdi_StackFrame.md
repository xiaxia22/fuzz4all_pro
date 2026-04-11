# Interface StackFrame

**Source:** `jdk.jdi\com\sun\jdi\StackFrame.html`

### Class Description

```java
public interface
StackFrame

extends
Mirror
,
Locatable
```

The state of one method invocation on a thread's call stack.
As a thread executes, stack frames are pushed and popped from
its call stack as methods are invoked and then return. A StackFrame
mirrors one such frame from a target VM at some point in its
thread's execution. The call stack is, then, simply a List of
StackFrame objects. The call stack can be obtained any time a thread
is suspended through a call to

ThreadReference.frames()

StackFrames provide access to a method's local variables and their
current values.

The lifetime of a StackFrame is very limited. It is available only
for suspended threads and becomes invalid once its thread is resumed.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

**All Superinterfaces:** Locatable

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Location
location()

Returns the

Location

of the current instruction in the frame.
The method for which this frame was created can also be accessed
through the returned location.
For the top frame in the stack, this location identifies the
next instruction to be executed. For all other frames, this
location identifies the instruction that caused the next frame's
method to be invoked.
If the frame represents a native method invocation, the returned
location indicates the class and method, but the code index will
not be valid (-1).

**Specified by:**
- location

in interface

Locatable

**Returns:**
- the

Location

of the current instruction.

**Throws:**
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### ThreadReference
thread()

Returns the thread under which this frame's method is running.

**Returns:**
- a

ThreadReference

which mirrors the frame's thread.

**Throws:**
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### ObjectReference
thisObject()

Returns the value of 'this' for the current frame.
The

ObjectReference

for 'this' is only available for
non-native instance methods.

**Returns:**
- an

ObjectReference

, or null if the frame represents
a native or static method.

**Throws:**
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### List
<
LocalVariable
> visibleVariables()
throws
AbsentInformationException

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

**Returns:**
- the list of

LocalVariable

objects currently visible;
the list will be empty if there are no visible variables;
specifically, frames in native methods will always return a
zero-length list.

**Throws:**
- AbsentInformationException

- if there is no local variable
information for this method.
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
- NativeMethodException

- if the current method is native.

---

#### LocalVariable
visibleVariableByName​(
String
name)
throws
AbsentInformationException

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.
See

visibleVariables()

for more information on visibility.

**Parameters:**
- name

- the variable name to find

**Returns:**
- the matching

LocalVariable

, or null if there is no
visible variable with the given name; frames in native methods
will always return null.

**Throws:**
- AbsentInformationException

- if there is no local variable
information for this method.
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
- NativeMethodException

- if the current method is native.

---

#### Value
getValue​(
LocalVariable
variable)

Gets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:**
- variable

- the

LocalVariable

to be accessed

**Returns:**
- the

Value

of the instance field.

**Throws:**
- IllegalArgumentException

- if the variable is
either invalid for this frame's method or not visible.
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### Map
<
LocalVariable
,​
Value
> getValues​(
List
<? extends
LocalVariable
> variables)

Returns the values of multiple local variables in this frame.
Each variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:**
- variables

- a list of

LocalVariable

objects to be accessed

**Returns:**
- a map associating each

LocalVariable

with
its

Value

**Throws:**
- IllegalArgumentException

- if any variable is
either invalid for this frame's method or not visible.
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### void setValue​(
LocalVariable
variable,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException

Sets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:**
- variable

- the field containing the requested value
- value

- the new value to assign

**Throws:**
- IllegalArgumentException

- if the field is not valid for
this object's class.
- InvalidTypeException

- if the value's type does not match
the variable's type.
- ClassNotLoadedException

- if the variable type has not yet been loaded
through the appropriate class loader.
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### List
<
Value
> getArgumentValues()

Returns the values of all arguments in this frame. Values are
returned even if no local variable information is present.

**Returns:**
- a list containing a

Value

object for each argument
to this frame, in the order in which the arguments were
declared. If the method corresponding to this frame has
no arguments, an empty list is returned.

**Throws:**
- InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

**Since:**
- 1.6

---

### Additional Sections

#### Interface StackFrame

**All Superinterfaces:** Locatable

,

Mirror

```java
public interface
StackFrame

extends
Mirror
,
Locatable
```

The state of one method invocation on a thread's call stack.
As a thread executes, stack frames are pushed and popped from
its call stack as methods are invoked and then return. A StackFrame
mirrors one such frame from a target VM at some point in its
thread's execution. The call stack is, then, simply a List of
StackFrame objects. The call stack can be obtained any time a thread
is suspended through a call to

ThreadReference.frames()

StackFrames provide access to a method's local variables and their
current values.

The lifetime of a StackFrame is very limited. It is available only
for suspended threads and becomes invalid once its thread is resumed.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

**Since:** 1.3

public interface

StackFrame

extends

Mirror

,

Locatable

The state of one method invocation on a thread's call stack.
As a thread executes, stack frames are pushed and popped from
its call stack as methods are invoked and then return. A StackFrame
mirrors one such frame from a target VM at some point in its
thread's execution. The call stack is, then, simply a List of
StackFrame objects. The call stack can be obtained any time a thread
is suspended through a call to

ThreadReference.frames()

StackFrames provide access to a method's local variables and their
current values.

The lifetime of a StackFrame is very limited. It is available only
for suspended threads and becomes invalid once its thread is resumed.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

StackFrames provide access to a method's local variables and their
current values.

The lifetime of a StackFrame is very limited. It is available only
for suspended threads and becomes invalid once its thread is resumed.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

The lifetime of a StackFrame is very limited. It is available only
for suspended threads and becomes invalid once its thread is resumed.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMDisconnectedException

if the target VM is
disconnected and the

VMDisconnectEvent

has been or is
available to be read from the

EventQueue

.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

Any method on

StackFrame

which
takes

StackFrame

as an parameter may throw

VMOutOfMemoryException

if the target VM has run out of memory.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

Value

>

getArgumentValues

()

Returns the values of all arguments in this frame.

Value

getValue

​(

LocalVariable

variable)

Gets the

Value

of a

LocalVariable

in this frame.

Map

<

LocalVariable

,​

Value

>

getValues

​(

List

<? extends

LocalVariable

> variables)

Returns the values of multiple local variables in this frame.

Location

location

()

Returns the

Location

of the current instruction in the frame.

void

setValue

​(

LocalVariable

variable,

Value

value)

Sets the

Value

of a

LocalVariable

in this frame.

ObjectReference

thisObject

()

Returns the value of 'this' for the current frame.

ThreadReference

thread

()

Returns the thread under which this frame's method is running.

LocalVariable

visibleVariableByName

​(

String

name)

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.

List

<

LocalVariable

>

visibleVariables

()

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

Value

>

getArgumentValues

()

Returns the values of all arguments in this frame.

Value

getValue

​(

LocalVariable

variable)

Gets the

Value

of a

LocalVariable

in this frame.

Map

<

LocalVariable

,​

Value

>

getValues

​(

List

<? extends

LocalVariable

> variables)

Returns the values of multiple local variables in this frame.

Location

location

()

Returns the

Location

of the current instruction in the frame.

void

setValue

​(

LocalVariable

variable,

Value

value)

Sets the

Value

of a

LocalVariable

in this frame.

ObjectReference

thisObject

()

Returns the value of 'this' for the current frame.

ThreadReference

thread

()

Returns the thread under which this frame's method is running.

LocalVariable

visibleVariableByName

​(

String

name)

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.

List

<

LocalVariable

>

visibleVariables

()

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the values of all arguments in this frame.

Gets the

Value

of a

LocalVariable

in this frame.

Returns the values of multiple local variables in this frame.

Returns the

Location

of the current instruction in the frame.

Sets the

Value

of a

LocalVariable

in this frame.

Returns the value of 'this' for the current frame.

Returns the thread under which this frame's method is running.

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- location

```java
Location
location()
```

Returns the

Location

of the current instruction in the frame.
The method for which this frame was created can also be accessed
through the returned location.
For the top frame in the stack, this location identifies the
next instruction to be executed. For all other frames, this
location identifies the instruction that caused the next frame's
method to be invoked.
If the frame represents a native method invocation, the returned
location indicates the class and method, but the code index will
not be valid (-1).

**Specified by:** location

in interface

Locatable
**Returns:** the

Location

of the current instruction.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- thread

```java
ThreadReference
thread()
```

Returns the thread under which this frame's method is running.

**Returns:** a

ThreadReference

which mirrors the frame's thread.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- thisObject

```java
ObjectReference
thisObject()
```

Returns the value of 'this' for the current frame.
The

ObjectReference

for 'this' is only available for
non-native instance methods.

**Returns:** an

ObjectReference

, or null if the frame represents
a native or static method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- visibleVariables

```java
List
<
LocalVariable
> visibleVariables()
throws
AbsentInformationException
```

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

**Returns:** the list of

LocalVariable

objects currently visible;
the list will be empty if there are no visible variables;
specifically, frames in native methods will always return a
zero-length list.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

- visibleVariableByName

```java
LocalVariable
visibleVariableByName​(
String
name)
throws
AbsentInformationException
```

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.
See

visibleVariables()

for more information on visibility.

**Parameters:** name

- the variable name to find
**Returns:** the matching

LocalVariable

, or null if there is no
visible variable with the given name; frames in native methods
will always return null.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

- getValue

```java
Value
getValue​(
LocalVariable
variable)
```

Gets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variable

- the

LocalVariable

to be accessed
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- getValues

```java
Map
<
LocalVariable
,​
Value
> getValues​(
List
<? extends
LocalVariable
> variables)
```

Returns the values of multiple local variables in this frame.
Each variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variables

- a list of

LocalVariable

objects to be accessed
**Returns:** a map associating each

LocalVariable

with
its

Value
**Throws:** IllegalArgumentException

- if any variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- setValue

```java
void setValue​(
LocalVariable
variable,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Sets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** variable

- the field containing the requested value
**Parameters:** value

- the new value to assign
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.
**Throws:** InvalidTypeException

- if the value's type does not match
the variable's type.
**Throws:** ClassNotLoadedException

- if the variable type has not yet been loaded
through the appropriate class loader.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- getArgumentValues

```java
List
<
Value
> getArgumentValues()
```

Returns the values of all arguments in this frame. Values are
returned even if no local variable information is present.

**Returns:** a list containing a

Value

object for each argument
to this frame, in the order in which the arguments were
declared. If the method corresponding to this frame has
no arguments, an empty list is returned.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Since:** 1.6

Method Detail

- location

```java
Location
location()
```

Returns the

Location

of the current instruction in the frame.
The method for which this frame was created can also be accessed
through the returned location.
For the top frame in the stack, this location identifies the
next instruction to be executed. For all other frames, this
location identifies the instruction that caused the next frame's
method to be invoked.
If the frame represents a native method invocation, the returned
location indicates the class and method, but the code index will
not be valid (-1).

**Specified by:** location

in interface

Locatable
**Returns:** the

Location

of the current instruction.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- thread

```java
ThreadReference
thread()
```

Returns the thread under which this frame's method is running.

**Returns:** a

ThreadReference

which mirrors the frame's thread.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- thisObject

```java
ObjectReference
thisObject()
```

Returns the value of 'this' for the current frame.
The

ObjectReference

for 'this' is only available for
non-native instance methods.

**Returns:** an

ObjectReference

, or null if the frame represents
a native or static method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- visibleVariables

```java
List
<
LocalVariable
> visibleVariables()
throws
AbsentInformationException
```

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

**Returns:** the list of

LocalVariable

objects currently visible;
the list will be empty if there are no visible variables;
specifically, frames in native methods will always return a
zero-length list.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

- visibleVariableByName

```java
LocalVariable
visibleVariableByName​(
String
name)
throws
AbsentInformationException
```

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.
See

visibleVariables()

for more information on visibility.

**Parameters:** name

- the variable name to find
**Returns:** the matching

LocalVariable

, or null if there is no
visible variable with the given name; frames in native methods
will always return null.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

- getValue

```java
Value
getValue​(
LocalVariable
variable)
```

Gets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variable

- the

LocalVariable

to be accessed
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- getValues

```java
Map
<
LocalVariable
,​
Value
> getValues​(
List
<? extends
LocalVariable
> variables)
```

Returns the values of multiple local variables in this frame.
Each variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variables

- a list of

LocalVariable

objects to be accessed
**Returns:** a map associating each

LocalVariable

with
its

Value
**Throws:** IllegalArgumentException

- if any variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

- setValue

```java
void setValue​(
LocalVariable
variable,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Sets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** variable

- the field containing the requested value
**Parameters:** value

- the new value to assign
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.
**Throws:** InvalidTypeException

- if the value's type does not match
the variable's type.
**Throws:** ClassNotLoadedException

- if the variable type has not yet been loaded
through the appropriate class loader.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- getArgumentValues

```java
List
<
Value
> getArgumentValues()
```

Returns the values of all arguments in this frame. Values are
returned even if no local variable information is present.

**Returns:** a list containing a

Value

object for each argument
to this frame, in the order in which the arguments were
declared. If the method corresponding to this frame has
no arguments, an empty list is returned.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Since:** 1.6

---

#### Method Detail

location

```java
Location
location()
```

Returns the

Location

of the current instruction in the frame.
The method for which this frame was created can also be accessed
through the returned location.
For the top frame in the stack, this location identifies the
next instruction to be executed. For all other frames, this
location identifies the instruction that caused the next frame's
method to be invoked.
If the frame represents a native method invocation, the returned
location indicates the class and method, but the code index will
not be valid (-1).

**Specified by:** location

in interface

Locatable
**Returns:** the

Location

of the current instruction.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### location

Location

location()

Returns the

Location

of the current instruction in the frame.
The method for which this frame was created can also be accessed
through the returned location.
For the top frame in the stack, this location identifies the
next instruction to be executed. For all other frames, this
location identifies the instruction that caused the next frame's
method to be invoked.
If the frame represents a native method invocation, the returned
location indicates the class and method, but the code index will
not be valid (-1).

thread

```java
ThreadReference
thread()
```

Returns the thread under which this frame's method is running.

**Returns:** a

ThreadReference

which mirrors the frame's thread.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### thread

ThreadReference

thread()

Returns the thread under which this frame's method is running.

thisObject

```java
ObjectReference
thisObject()
```

Returns the value of 'this' for the current frame.
The

ObjectReference

for 'this' is only available for
non-native instance methods.

**Returns:** an

ObjectReference

, or null if the frame represents
a native or static method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### thisObject

ObjectReference

thisObject()

Returns the value of 'this' for the current frame.
The

ObjectReference

for 'this' is only available for
non-native instance methods.

visibleVariables

```java
List
<
LocalVariable
> visibleVariables()
throws
AbsentInformationException
```

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

**Returns:** the list of

LocalVariable

objects currently visible;
the list will be empty if there are no visible variables;
specifically, frames in native methods will always return a
zero-length list.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

---

#### visibleVariables

List

<

LocalVariable

> visibleVariables()
throws

AbsentInformationException

Returns a list containing each

LocalVariable

that can be accessed from this frame's location.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

Visibility is based on the code index of the current instruction of
this StackFrame. Each variable has a range of byte code indices in which
it is accessible.
If this stack frame's method
matches this variable's method and if the code index of this
StackFrame is within the variable's byte code range, the variable is
visible.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

A variable's byte code range is at least as large as the scope of
that variable, but can continue beyond the end of the scope under
certain circumstances:

- the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

The advantage of an extended range is that variables from recently
exited scopes may remain available for examination (this is especially
useful for loop indices). If, as a result of the extensions above,
the current frame location is contained within the range
of multiple local variables of the same name, the variable with the
highest-starting range is chosen for the returned list.

the compiler/VM does not immediately reuse the variable's slot.

the compiler/VM is implemented to report the extended range that
would result from the item above.

visibleVariableByName

```java
LocalVariable
visibleVariableByName​(
String
name)
throws
AbsentInformationException
```

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.
See

visibleVariables()

for more information on visibility.

**Parameters:** name

- the variable name to find
**Returns:** the matching

LocalVariable

, or null if there is no
visible variable with the given name; frames in native methods
will always return null.
**Throws:** AbsentInformationException

- if there is no local variable
information for this method.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** NativeMethodException

- if the current method is native.

---

#### visibleVariableByName

LocalVariable

visibleVariableByName​(

String

name)
throws

AbsentInformationException

Finds a

LocalVariable

that matches the given name and is
visible at the current frame location.
See

visibleVariables()

for more information on visibility.

getValue

```java
Value
getValue​(
LocalVariable
variable)
```

Gets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variable

- the

LocalVariable

to be accessed
**Returns:** the

Value

of the instance field.
**Throws:** IllegalArgumentException

- if the variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### getValue

Value

getValue​(

LocalVariable

variable)

Gets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

getValues

```java
Map
<
LocalVariable
,​
Value
> getValues​(
List
<? extends
LocalVariable
> variables)
```

Returns the values of multiple local variables in this frame.
Each variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

**Parameters:** variables

- a list of

LocalVariable

objects to be accessed
**Returns:** a map associating each

LocalVariable

with
its

Value
**Throws:** IllegalArgumentException

- if any variable is
either invalid for this frame's method or not visible.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.

---

#### getValues

Map

<

LocalVariable

,​

Value

> getValues​(

List

<? extends

LocalVariable

> variables)

Returns the values of multiple local variables in this frame.
Each variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

setValue

```java
void setValue​(
LocalVariable
variable,

Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
```

Sets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

**Parameters:** variable

- the field containing the requested value
**Parameters:** value

- the new value to assign
**Throws:** IllegalArgumentException

- if the field is not valid for
this object's class.
**Throws:** InvalidTypeException

- if the value's type does not match
the variable's type.
**Throws:** ClassNotLoadedException

- if the variable type has not yet been loaded
through the appropriate class loader.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### setValue

void setValue​(

LocalVariable

variable,

Value

value)
throws

InvalidTypeException

,

ClassNotLoadedException

Sets the

Value

of a

LocalVariable

in this frame.
The variable must be valid for this frame's method and visible
according to the rules described in

visibleVariables()

.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Object values must be assignment compatible with the variable type
(This implies that the variable type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the variable type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

getArgumentValues

```java
List
<
Value
> getArgumentValues()
```

Returns the values of all arguments in this frame. Values are
returned even if no local variable information is present.

**Returns:** a list containing a

Value

object for each argument
to this frame, in the order in which the arguments were
declared. If the method corresponding to this frame has
no arguments, an empty list is returned.
**Throws:** InvalidStackFrameException

- if this stack frame has become
invalid. Once the frame's thread is resumed, the stack frame is
no longer valid.
**Since:** 1.6

---

#### getArgumentValues

List

<

Value

> getArgumentValues()

Returns the values of all arguments in this frame. Values are
returned even if no local variable information is present.

---

