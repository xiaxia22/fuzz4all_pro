# Class JShell

**Source:** `jdk.jshell\jdk\jshell\JShell.html`

### Class Description

```java
public class
JShell

extends
Object

implements
AutoCloseable
```

The JShell evaluation state engine. This is the central class in the JShell
API. A

JShell

instance holds the evolving compilation and
execution state. The state is changed with the instance methods

eval(String)

,

drop(Snippet)

and

addToClasspath(String)

.
The majority of methods query the state.
A

JShell

instance also allows registering for events with

onSnippetEvent(Consumer)

and

onShutdown(Consumer)

, which
are unregistered with

unsubscribe(Subscription)

.
Access to the source analysis utilities is via

sourceCodeAnalysis()

.
When complete the instance should be closed to free resources --

close()

.

An instance of

JShell

is created with

JShell.create()

.

This class is not thread safe, except as noted, all access should be through
a single thread.

**All Implemented Interfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
JShell
create()
throws
IllegalStateException

Create a new JShell state engine.
That is, create an instance of

JShell

.

Equivalent to

JShell.builder()

.build()

.

**Returns:**
- an instance of

JShell

.

**Throws:**
- IllegalStateException

- if the

JShell

instance could not be created.

---

#### public static
JShell.Builder
builder()

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.
Create a default instance of

JShell

with

JShell.builder().build()

. For more construction options
see

JShell.Builder

.

**Returns:**
- an instance of

Builder

.

**See Also:**
- JShell.Builder

---

#### public
SourceCodeAnalysis
sourceCodeAnalysis()

Access to source code analysis functionality.
An instance of

JShell

will always return the same

SourceCodeAnalysis

instance from

sourceCodeAnalysis()

.

**Returns:**
- an instance of

SourceCodeAnalysis

which can be used for source analysis such as completion detection and
completion suggestions.

---

#### public
List
<
SnippetEvent
> eval​(
String
input)
throws
IllegalStateException

Evaluate the input String, including definition and/or execution, if
applicable. The input is checked for errors, unless the errors can be
deferred (as is the case with some unresolvedDependencies references),
errors will abort evaluation.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

**Parameters:**
- input

- The input String to evaluate

**Returns:**
- the list of events directly or indirectly caused by this evaluation.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.

**See Also:**
- SourceCodeAnalysis.analyzeCompletion(String)

,

onShutdown(java.util.function.Consumer)

---

#### public
List
<
SnippetEvent
> drop​(
Snippet
snippet)
throws
IllegalStateException

Remove a declaration from the state. That is, if the snippet is an

active

persistent

snippet, remove the
snippet and update the JShell evaluation state accordingly.
For all active snippets, change the

status

to

DROPPED

.

**Parameters:**
- snippet

- The snippet to remove

**Returns:**
- The list of events from updating declarations dependent on the
dropped snippet.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.
- IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### public void addToClasspath​(
String
path)

The specified path is added to the end of the classpath used in eval().
Note that the unnamed package is not accessible from the package in which

eval(String)

code is placed.

**Parameters:**
- path

- the path to add to the classpath.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.

---

#### public void stop()

Attempt to stop currently running evaluation. When called while
the

eval(java.lang.String)

method is running and the
user's code being executed, an attempt will be made to stop user's code.
Note that typically this method needs to be called from a different thread
than the one running the

eval

method.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

---

#### public void close()

Close this state engine. Frees resources. Should be called when this
state engine is no longer needed.

**Specified by:**
- close

in interface

AutoCloseable

---

#### public
Stream
<
Snippet
> snippets()

Return all snippets.

**Returns:**
- the snippets for all current snippets in id order.

---

#### public
Stream
<
VarSnippet
> variables()

Returns the active variable snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.VARIABLE

and cast to

VarSnippet

.

**Returns:**
- the active declared variables.

---

#### public
Stream
<
MethodSnippet
> methods()

Returns the active method snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.METHOD

and cast to MethodSnippet.

**Returns:**
- the active declared methods.

---

#### public
Stream
<
TypeDeclSnippet
> types()

Returns the active type declaration (class, interface, annotation type, and enum) snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.TYPE_DECL

and cast to TypeDeclSnippet.

**Returns:**
- the active declared type declarations.

---

#### public
Stream
<
ImportSnippet
> imports()

Returns the active import snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.IMPORT

and cast to ImportSnippet.

**Returns:**
- the active declared import declarations.

---

#### public
Snippet.Status
status​(
Snippet
snippet)

Return the status of the snippet.
This is updated either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:**
- snippet

- the

Snippet

to look up

**Returns:**
- the status corresponding to this snippet

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.
- IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### public
Stream
<
Diag
> diagnostics​(
Snippet
snippet)

Return the diagnostics of the most recent evaluation of the snippet.
The evaluation can either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:**
- snippet

- the

Snippet

to look up

**Returns:**
- the diagnostics corresponding to this snippet. This does not
include unresolvedDependencies references reported in

unresolvedDependencies()

.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.
- IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### public
Stream
<
String
> unresolvedDependencies​(
DeclarationSnippet
snippet)

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.
The returned value of this method, for a given method may change when an

eval()

or

drop()

of another snippet causes
an update of a dependency.

**Parameters:**
- snippet

- the declaration

Snippet

to look up

**Returns:**
- a stream of symbol names that are currently unresolvedDependencies.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.
- IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### public
String
varValue​(
VarSnippet
snippet)
throws
IllegalStateException

Get the current value of a variable.

**Parameters:**
- snippet

- the variable Snippet whose value is queried.

**Returns:**
- the current value of the variable referenced by snippet.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.
- IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.
- IllegalArgumentException

- if the variable's status is anything but

Snippet.Status.VALID

.

---

#### public
JShell.Subscription
onSnippetEvent​(
Consumer
<
SnippetEvent
> listener)
throws
IllegalStateException

Register a callback to be called when the Status of a snippet changes.
Each call adds a new subscription.

**Parameters:**
- listener

- Action to perform when the Status changes.

**Returns:**
- A token which can be used to

unsubscribe

this subscription.

**Throws:**
- IllegalStateException

- if this

JShell

instance is closed.

---

#### public
JShell.Subscription
onShutdown​(
Consumer
<
JShell
> listener)
throws
IllegalStateException

Register a callback to be called when this JShell instance terminates.
This occurs either because the client process has ended (e.g. called System.exit(0))
or the connection has been shutdown, as by close().
Each call adds a new subscription.

**Parameters:**
- listener

- Action to perform when the state terminates.

**Returns:**
- A token which can be used to

unsubscribe

this subscription.

**Throws:**
- IllegalStateException

- if this JShell instance is closed

---

#### public void unsubscribe​(
JShell.Subscription
token)

Cancel a callback subscription.

**Parameters:**
- token

- The token corresponding to the subscription to be unsubscribed.

---

### Additional Sections

#### Class JShell

java.lang.Object

- jdk.jshell.JShell

jdk.jshell.JShell

**All Implemented Interfaces:** AutoCloseable

```java
public class
JShell

extends
Object

implements
AutoCloseable
```

The JShell evaluation state engine. This is the central class in the JShell
API. A

JShell

instance holds the evolving compilation and
execution state. The state is changed with the instance methods

eval(String)

,

drop(Snippet)

and

addToClasspath(String)

.
The majority of methods query the state.
A

JShell

instance also allows registering for events with

onSnippetEvent(Consumer)

and

onShutdown(Consumer)

, which
are unregistered with

unsubscribe(Subscription)

.
Access to the source analysis utilities is via

sourceCodeAnalysis()

.
When complete the instance should be closed to free resources --

close()

.

An instance of

JShell

is created with

JShell.create()

.

This class is not thread safe, except as noted, all access should be through
a single thread.

**Since:** 9

public class

JShell

extends

Object

implements

AutoCloseable

The JShell evaluation state engine. This is the central class in the JShell
API. A

JShell

instance holds the evolving compilation and
execution state. The state is changed with the instance methods

eval(String)

,

drop(Snippet)

and

addToClasspath(String)

.
The majority of methods query the state.
A

JShell

instance also allows registering for events with

onSnippetEvent(Consumer)

and

onShutdown(Consumer)

, which
are unregistered with

unsubscribe(Subscription)

.
Access to the source analysis utilities is via

sourceCodeAnalysis()

.
When complete the instance should be closed to free resources --

close()

.

An instance of

JShell

is created with

JShell.create()

.

This class is not thread safe, except as noted, all access should be through
a single thread.

An instance of

JShell

is created with

JShell.create()

.

This class is not thread safe, except as noted, all access should be through
a single thread.

This class is not thread safe, except as noted, all access should be through
a single thread.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

JShell.Builder

Builder for

JShell

instances.

class

JShell.Subscription

Subscription is a token for referring to subscriptions so they can
be

unsubscribed

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

The specified path is added to the end of the classpath used in eval().

static

JShell.Builder

builder

()

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.

void

close

()

Close this state engine.

static

JShell

create

()

Create a new JShell state engine.

Stream

<

Diag

>

diagnostics

​(

Snippet

snippet)

Return the diagnostics of the most recent evaluation of the snippet.

List

<

SnippetEvent

>

drop

​(

Snippet

snippet)

Remove a declaration from the state.

List

<

SnippetEvent

>

eval

​(

String

input)

Evaluate the input String, including definition and/or execution, if
applicable.

Stream

<

ImportSnippet

>

imports

()

Returns the active import snippets.

Stream

<

MethodSnippet

>

methods

()

Returns the active method snippets.

JShell.Subscription

onShutdown

​(

Consumer

<

JShell

> listener)

Register a callback to be called when this JShell instance terminates.

JShell.Subscription

onSnippetEvent

​(

Consumer

<

SnippetEvent

> listener)

Register a callback to be called when the Status of a snippet changes.

Stream

<

Snippet

>

snippets

()

Return all snippets.

SourceCodeAnalysis

sourceCodeAnalysis

()

Access to source code analysis functionality.

Snippet.Status

status

​(

Snippet

snippet)

Return the status of the snippet.

void

stop

()

Attempt to stop currently running evaluation.

Stream

<

TypeDeclSnippet

>

types

()

Returns the active type declaration (class, interface, annotation type, and enum) snippets.

Stream

<

String

>

unresolvedDependencies

​(

DeclarationSnippet

snippet)

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.

void

unsubscribe

​(

JShell.Subscription

token)

Cancel a callback subscription.

Stream

<

VarSnippet

>

variables

()

Returns the active variable snippets.

String

varValue

​(

VarSnippet

snippet)

Get the current value of a variable.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

JShell.Builder

Builder for

JShell

instances.

class

JShell.Subscription

Subscription is a token for referring to subscriptions so they can
be

unsubscribed

.

---

#### Nested Class Summary

Builder for

JShell

instances.

Subscription is a token for referring to subscriptions so they can
be

unsubscribed

.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

The specified path is added to the end of the classpath used in eval().

static

JShell.Builder

builder

()

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.

void

close

()

Close this state engine.

static

JShell

create

()

Create a new JShell state engine.

Stream

<

Diag

>

diagnostics

​(

Snippet

snippet)

Return the diagnostics of the most recent evaluation of the snippet.

List

<

SnippetEvent

>

drop

​(

Snippet

snippet)

Remove a declaration from the state.

List

<

SnippetEvent

>

eval

​(

String

input)

Evaluate the input String, including definition and/or execution, if
applicable.

Stream

<

ImportSnippet

>

imports

()

Returns the active import snippets.

Stream

<

MethodSnippet

>

methods

()

Returns the active method snippets.

JShell.Subscription

onShutdown

​(

Consumer

<

JShell

> listener)

Register a callback to be called when this JShell instance terminates.

JShell.Subscription

onSnippetEvent

​(

Consumer

<

SnippetEvent

> listener)

Register a callback to be called when the Status of a snippet changes.

Stream

<

Snippet

>

snippets

()

Return all snippets.

SourceCodeAnalysis

sourceCodeAnalysis

()

Access to source code analysis functionality.

Snippet.Status

status

​(

Snippet

snippet)

Return the status of the snippet.

void

stop

()

Attempt to stop currently running evaluation.

Stream

<

TypeDeclSnippet

>

types

()

Returns the active type declaration (class, interface, annotation type, and enum) snippets.

Stream

<

String

>

unresolvedDependencies

​(

DeclarationSnippet

snippet)

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.

void

unsubscribe

​(

JShell.Subscription

token)

Cancel a callback subscription.

Stream

<

VarSnippet

>

variables

()

Returns the active variable snippets.

String

varValue

​(

VarSnippet

snippet)

Get the current value of a variable.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

The specified path is added to the end of the classpath used in eval().

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.

Close this state engine.

Create a new JShell state engine.

Return the diagnostics of the most recent evaluation of the snippet.

Remove a declaration from the state.

Evaluate the input String, including definition and/or execution, if
applicable.

Returns the active import snippets.

Returns the active method snippets.

Register a callback to be called when this JShell instance terminates.

Register a callback to be called when the Status of a snippet changes.

Return all snippets.

Access to source code analysis functionality.

Return the status of the snippet.

Attempt to stop currently running evaluation.

Returns the active type declaration (class, interface, annotation type, and enum) snippets.

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.

Cancel a callback subscription.

Returns the active variable snippets.

Get the current value of a variable.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ METHOD DETAIL ==========

- Method Detail

- create

```java
public static
JShell
create()
throws
IllegalStateException
```

Create a new JShell state engine.
That is, create an instance of

JShell

.

Equivalent to

JShell.builder()

.build()

.

**Returns:** an instance of

JShell

.
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

- builder

```java
public static
JShell.Builder
builder()
```

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.
Create a default instance of

JShell

with

JShell.builder().build()

. For more construction options
see

JShell.Builder

.

**Returns:** an instance of

Builder

.
**See Also:** JShell.Builder

- sourceCodeAnalysis

```java
public
SourceCodeAnalysis
sourceCodeAnalysis()
```

Access to source code analysis functionality.
An instance of

JShell

will always return the same

SourceCodeAnalysis

instance from

sourceCodeAnalysis()

.

**Returns:** an instance of

SourceCodeAnalysis

which can be used for source analysis such as completion detection and
completion suggestions.

- eval

```java
public
List
<
SnippetEvent
> eval​(
String
input)
throws
IllegalStateException
```

Evaluate the input String, including definition and/or execution, if
applicable. The input is checked for errors, unless the errors can be
deferred (as is the case with some unresolvedDependencies references),
errors will abort evaluation.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

**Parameters:** input

- The input String to evaluate
**Returns:** the list of events directly or indirectly caused by this evaluation.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**See Also:** SourceCodeAnalysis.analyzeCompletion(String)

,

onShutdown(java.util.function.Consumer)

- drop

```java
public
List
<
SnippetEvent
> drop​(
Snippet
snippet)
throws
IllegalStateException
```

Remove a declaration from the state. That is, if the snippet is an

active

persistent

snippet, remove the
snippet and update the JShell evaluation state accordingly.
For all active snippets, change the

status

to

DROPPED

.

**Parameters:** snippet

- The snippet to remove
**Returns:** The list of events from updating declarations dependent on the
dropped snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- addToClasspath

```java
public void addToClasspath​(
String
path)
```

The specified path is added to the end of the classpath used in eval().
Note that the unnamed package is not accessible from the package in which

eval(String)

code is placed.

**Parameters:** path

- the path to add to the classpath.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

- stop

```java
public void stop()
```

Attempt to stop currently running evaluation. When called while
the

eval(java.lang.String)

method is running and the
user's code being executed, an attempt will be made to stop user's code.
Note that typically this method needs to be called from a different thread
than the one running the

eval

method.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

- close

```java
public void close()
```

Close this state engine. Frees resources. Should be called when this
state engine is no longer needed.

**Specified by:** close

in interface

AutoCloseable

- snippets

```java
public
Stream
<
Snippet
> snippets()
```

Return all snippets.

**Returns:** the snippets for all current snippets in id order.

- variables

```java
public
Stream
<
VarSnippet
> variables()
```

Returns the active variable snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.VARIABLE

and cast to

VarSnippet

.

**Returns:** the active declared variables.

- methods

```java
public
Stream
<
MethodSnippet
> methods()
```

Returns the active method snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.METHOD

and cast to MethodSnippet.

**Returns:** the active declared methods.

- types

```java
public
Stream
<
TypeDeclSnippet
> types()
```

Returns the active type declaration (class, interface, annotation type, and enum) snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.TYPE_DECL

and cast to TypeDeclSnippet.

**Returns:** the active declared type declarations.

- imports

```java
public
Stream
<
ImportSnippet
> imports()
```

Returns the active import snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.IMPORT

and cast to ImportSnippet.

**Returns:** the active declared import declarations.

- status

```java
public
Snippet.Status
status​(
Snippet
snippet)
```

Return the status of the snippet.
This is updated either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the status corresponding to this snippet
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- diagnostics

```java
public
Stream
<
Diag
> diagnostics​(
Snippet
snippet)
```

Return the diagnostics of the most recent evaluation of the snippet.
The evaluation can either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the diagnostics corresponding to this snippet. This does not
include unresolvedDependencies references reported in

unresolvedDependencies()

.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- unresolvedDependencies

```java
public
Stream
<
String
> unresolvedDependencies​(
DeclarationSnippet
snippet)
```

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.
The returned value of this method, for a given method may change when an

eval()

or

drop()

of another snippet causes
an update of a dependency.

**Parameters:** snippet

- the declaration

Snippet

to look up
**Returns:** a stream of symbol names that are currently unresolvedDependencies.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- varValue

```java
public
String
varValue​(
VarSnippet
snippet)
throws
IllegalStateException
```

Get the current value of a variable.

**Parameters:** snippet

- the variable Snippet whose value is queried.
**Returns:** the current value of the variable referenced by snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.
**Throws:** IllegalArgumentException

- if the variable's status is anything but

Snippet.Status.VALID

.

- onSnippetEvent

```java
public
JShell.Subscription
onSnippetEvent​(
Consumer
<
SnippetEvent
> listener)
throws
IllegalStateException
```

Register a callback to be called when the Status of a snippet changes.
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the Status changes.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

- onShutdown

```java
public
JShell.Subscription
onShutdown​(
Consumer
<
JShell
> listener)
throws
IllegalStateException
```

Register a callback to be called when this JShell instance terminates.
This occurs either because the client process has ended (e.g. called System.exit(0))
or the connection has been shutdown, as by close().
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the state terminates.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this JShell instance is closed

- unsubscribe

```java
public void unsubscribe​(
JShell.Subscription
token)
```

Cancel a callback subscription.

**Parameters:** token

- The token corresponding to the subscription to be unsubscribed.

Method Detail

- create

```java
public static
JShell
create()
throws
IllegalStateException
```

Create a new JShell state engine.
That is, create an instance of

JShell

.

Equivalent to

JShell.builder()

.build()

.

**Returns:** an instance of

JShell

.
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

- builder

```java
public static
JShell.Builder
builder()
```

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.
Create a default instance of

JShell

with

JShell.builder().build()

. For more construction options
see

JShell.Builder

.

**Returns:** an instance of

Builder

.
**See Also:** JShell.Builder

- sourceCodeAnalysis

```java
public
SourceCodeAnalysis
sourceCodeAnalysis()
```

Access to source code analysis functionality.
An instance of

JShell

will always return the same

SourceCodeAnalysis

instance from

sourceCodeAnalysis()

.

**Returns:** an instance of

SourceCodeAnalysis

which can be used for source analysis such as completion detection and
completion suggestions.

- eval

```java
public
List
<
SnippetEvent
> eval​(
String
input)
throws
IllegalStateException
```

Evaluate the input String, including definition and/or execution, if
applicable. The input is checked for errors, unless the errors can be
deferred (as is the case with some unresolvedDependencies references),
errors will abort evaluation.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

**Parameters:** input

- The input String to evaluate
**Returns:** the list of events directly or indirectly caused by this evaluation.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**See Also:** SourceCodeAnalysis.analyzeCompletion(String)

,

onShutdown(java.util.function.Consumer)

- drop

```java
public
List
<
SnippetEvent
> drop​(
Snippet
snippet)
throws
IllegalStateException
```

Remove a declaration from the state. That is, if the snippet is an

active

persistent

snippet, remove the
snippet and update the JShell evaluation state accordingly.
For all active snippets, change the

status

to

DROPPED

.

**Parameters:** snippet

- The snippet to remove
**Returns:** The list of events from updating declarations dependent on the
dropped snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- addToClasspath

```java
public void addToClasspath​(
String
path)
```

The specified path is added to the end of the classpath used in eval().
Note that the unnamed package is not accessible from the package in which

eval(String)

code is placed.

**Parameters:** path

- the path to add to the classpath.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

- stop

```java
public void stop()
```

Attempt to stop currently running evaluation. When called while
the

eval(java.lang.String)

method is running and the
user's code being executed, an attempt will be made to stop user's code.
Note that typically this method needs to be called from a different thread
than the one running the

eval

method.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

- close

```java
public void close()
```

Close this state engine. Frees resources. Should be called when this
state engine is no longer needed.

**Specified by:** close

in interface

AutoCloseable

- snippets

```java
public
Stream
<
Snippet
> snippets()
```

Return all snippets.

**Returns:** the snippets for all current snippets in id order.

- variables

```java
public
Stream
<
VarSnippet
> variables()
```

Returns the active variable snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.VARIABLE

and cast to

VarSnippet

.

**Returns:** the active declared variables.

- methods

```java
public
Stream
<
MethodSnippet
> methods()
```

Returns the active method snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.METHOD

and cast to MethodSnippet.

**Returns:** the active declared methods.

- types

```java
public
Stream
<
TypeDeclSnippet
> types()
```

Returns the active type declaration (class, interface, annotation type, and enum) snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.TYPE_DECL

and cast to TypeDeclSnippet.

**Returns:** the active declared type declarations.

- imports

```java
public
Stream
<
ImportSnippet
> imports()
```

Returns the active import snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.IMPORT

and cast to ImportSnippet.

**Returns:** the active declared import declarations.

- status

```java
public
Snippet.Status
status​(
Snippet
snippet)
```

Return the status of the snippet.
This is updated either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the status corresponding to this snippet
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- diagnostics

```java
public
Stream
<
Diag
> diagnostics​(
Snippet
snippet)
```

Return the diagnostics of the most recent evaluation of the snippet.
The evaluation can either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the diagnostics corresponding to this snippet. This does not
include unresolvedDependencies references reported in

unresolvedDependencies()

.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- unresolvedDependencies

```java
public
Stream
<
String
> unresolvedDependencies​(
DeclarationSnippet
snippet)
```

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.
The returned value of this method, for a given method may change when an

eval()

or

drop()

of another snippet causes
an update of a dependency.

**Parameters:** snippet

- the declaration

Snippet

to look up
**Returns:** a stream of symbol names that are currently unresolvedDependencies.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

- varValue

```java
public
String
varValue​(
VarSnippet
snippet)
throws
IllegalStateException
```

Get the current value of a variable.

**Parameters:** snippet

- the variable Snippet whose value is queried.
**Returns:** the current value of the variable referenced by snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.
**Throws:** IllegalArgumentException

- if the variable's status is anything but

Snippet.Status.VALID

.

- onSnippetEvent

```java
public
JShell.Subscription
onSnippetEvent​(
Consumer
<
SnippetEvent
> listener)
throws
IllegalStateException
```

Register a callback to be called when the Status of a snippet changes.
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the Status changes.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

- onShutdown

```java
public
JShell.Subscription
onShutdown​(
Consumer
<
JShell
> listener)
throws
IllegalStateException
```

Register a callback to be called when this JShell instance terminates.
This occurs either because the client process has ended (e.g. called System.exit(0))
or the connection has been shutdown, as by close().
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the state terminates.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this JShell instance is closed

- unsubscribe

```java
public void unsubscribe​(
JShell.Subscription
token)
```

Cancel a callback subscription.

**Parameters:** token

- The token corresponding to the subscription to be unsubscribed.

---

#### Method Detail

create

```java
public static
JShell
create()
throws
IllegalStateException
```

Create a new JShell state engine.
That is, create an instance of

JShell

.

Equivalent to

JShell.builder()

.build()

.

**Returns:** an instance of

JShell

.
**Throws:** IllegalStateException

- if the

JShell

instance could not be created.

---

#### create

public static

JShell

create()
throws

IllegalStateException

Create a new JShell state engine.
That is, create an instance of

JShell

.

Equivalent to

JShell.builder()

.build()

.

Equivalent to

JShell.builder()

.build()

.

builder

```java
public static
JShell.Builder
builder()
```

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.
Create a default instance of

JShell

with

JShell.builder().build()

. For more construction options
see

JShell.Builder

.

**Returns:** an instance of

Builder

.
**See Also:** JShell.Builder

---

#### builder

public static

JShell.Builder

builder()

Factory method for

JShell.Builder

which, in-turn, is used
for creating instances of

JShell

.
Create a default instance of

JShell

with

JShell.builder().build()

. For more construction options
see

JShell.Builder

.

sourceCodeAnalysis

```java
public
SourceCodeAnalysis
sourceCodeAnalysis()
```

Access to source code analysis functionality.
An instance of

JShell

will always return the same

SourceCodeAnalysis

instance from

sourceCodeAnalysis()

.

**Returns:** an instance of

SourceCodeAnalysis

which can be used for source analysis such as completion detection and
completion suggestions.

---

#### sourceCodeAnalysis

public

SourceCodeAnalysis

sourceCodeAnalysis()

Access to source code analysis functionality.
An instance of

JShell

will always return the same

SourceCodeAnalysis

instance from

sourceCodeAnalysis()

.

eval

```java
public
List
<
SnippetEvent
> eval​(
String
input)
throws
IllegalStateException
```

Evaluate the input String, including definition and/or execution, if
applicable. The input is checked for errors, unless the errors can be
deferred (as is the case with some unresolvedDependencies references),
errors will abort evaluation.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

**Parameters:** input

- The input String to evaluate
**Returns:** the list of events directly or indirectly caused by this evaluation.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**See Also:** SourceCodeAnalysis.analyzeCompletion(String)

,

onShutdown(java.util.function.Consumer)

---

#### eval

public

List

<

SnippetEvent

> eval​(

String

input)
throws

IllegalStateException

Evaluate the input String, including definition and/or execution, if
applicable. The input is checked for errors, unless the errors can be
deferred (as is the case with some unresolvedDependencies references),
errors will abort evaluation.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

The input should be
exactly one complete snippet of source code, that is, one expression,
statement, variable declaration, method declaration, class declaration,
or import.
To break arbitrary input into individual complete snippets, use

SourceCodeAnalysis.analyzeCompletion(String)

.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

For imports, the import is added. Classes, interfaces. methods,
and variables are defined. The initializer of variables, statements,
and expressions are executed.
The modifiers public, protected, private, static, and final are not
allowed on op-level declarations and are ignored with a warning.
Synchronized, native, abstract, and default top-level methods are not
allowed and are errors.
If a previous definition of a declaration is overwritten then there will
be an event showing its status changed to OVERWRITTEN, this will not
occur for dropped, rejected, or already overwritten declarations.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

If execution environment is out of process, as is the default case, then
if the evaluated code
causes the execution environment to terminate, this

JShell

instance will be closed but the calling process and VM remain valid.

drop

```java
public
List
<
SnippetEvent
> drop​(
Snippet
snippet)
throws
IllegalStateException
```

Remove a declaration from the state. That is, if the snippet is an

active

persistent

snippet, remove the
snippet and update the JShell evaluation state accordingly.
For all active snippets, change the

status

to

DROPPED

.

**Parameters:** snippet

- The snippet to remove
**Returns:** The list of events from updating declarations dependent on the
dropped snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### drop

public

List

<

SnippetEvent

> drop​(

Snippet

snippet)
throws

IllegalStateException

Remove a declaration from the state. That is, if the snippet is an

active

persistent

snippet, remove the
snippet and update the JShell evaluation state accordingly.
For all active snippets, change the

status

to

DROPPED

.

addToClasspath

```java
public void addToClasspath​(
String
path)
```

The specified path is added to the end of the classpath used in eval().
Note that the unnamed package is not accessible from the package in which

eval(String)

code is placed.

**Parameters:** path

- the path to add to the classpath.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

---

#### addToClasspath

public void addToClasspath​(

String

path)

The specified path is added to the end of the classpath used in eval().
Note that the unnamed package is not accessible from the package in which

eval(String)

code is placed.

stop

```java
public void stop()
```

Attempt to stop currently running evaluation. When called while
the

eval(java.lang.String)

method is running and the
user's code being executed, an attempt will be made to stop user's code.
Note that typically this method needs to be called from a different thread
than the one running the

eval

method.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

---

#### stop

public void stop()

Attempt to stop currently running evaluation. When called while
the

eval(java.lang.String)

method is running and the
user's code being executed, an attempt will be made to stop user's code.
Note that typically this method needs to be called from a different thread
than the one running the

eval

method.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

If the

eval(java.lang.String)

method is not running, does nothing.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

The attempt to stop the user's code may fail in some case, which may include
when the execution is blocked on an I/O operation, or when the user's code is
catching the

ThreadDeath

exception.

close

```java
public void close()
```

Close this state engine. Frees resources. Should be called when this
state engine is no longer needed.

**Specified by:** close

in interface

AutoCloseable

---

#### close

public void close()

Close this state engine. Frees resources. Should be called when this
state engine is no longer needed.

snippets

```java
public
Stream
<
Snippet
> snippets()
```

Return all snippets.

**Returns:** the snippets for all current snippets in id order.

---

#### snippets

public

Stream

<

Snippet

> snippets()

Return all snippets.

variables

```java
public
Stream
<
VarSnippet
> variables()
```

Returns the active variable snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.VARIABLE

and cast to

VarSnippet

.

**Returns:** the active declared variables.

---

#### variables

public

Stream

<

VarSnippet

> variables()

Returns the active variable snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.VARIABLE

and cast to

VarSnippet

.

methods

```java
public
Stream
<
MethodSnippet
> methods()
```

Returns the active method snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.METHOD

and cast to MethodSnippet.

**Returns:** the active declared methods.

---

#### methods

public

Stream

<

MethodSnippet

> methods()

Returns the active method snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.METHOD

and cast to MethodSnippet.

types

```java
public
Stream
<
TypeDeclSnippet
> types()
```

Returns the active type declaration (class, interface, annotation type, and enum) snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.TYPE_DECL

and cast to TypeDeclSnippet.

**Returns:** the active declared type declarations.

---

#### types

public

Stream

<

TypeDeclSnippet

> types()

Returns the active type declaration (class, interface, annotation type, and enum) snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.TYPE_DECL

and cast to TypeDeclSnippet.

imports

```java
public
Stream
<
ImportSnippet
> imports()
```

Returns the active import snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.IMPORT

and cast to ImportSnippet.

**Returns:** the active declared import declarations.

---

#### imports

public

Stream

<

ImportSnippet

> imports()

Returns the active import snippets.
This convenience method is equivalent to

snippets()

filtered for

status(snippet).isActive()

&& snippet.kind() == Kind.IMPORT

and cast to ImportSnippet.

status

```java
public
Snippet.Status
status​(
Snippet
snippet)
```

Return the status of the snippet.
This is updated either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the status corresponding to this snippet
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### status

public

Snippet.Status

status​(

Snippet

snippet)

Return the status of the snippet.
This is updated either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

diagnostics

```java
public
Stream
<
Diag
> diagnostics​(
Snippet
snippet)
```

Return the diagnostics of the most recent evaluation of the snippet.
The evaluation can either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

**Parameters:** snippet

- the

Snippet

to look up
**Returns:** the diagnostics corresponding to this snippet. This does not
include unresolvedDependencies references reported in

unresolvedDependencies()

.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### diagnostics

public

Stream

<

Diag

> diagnostics​(

Snippet

snippet)

Return the diagnostics of the most recent evaluation of the snippet.
The evaluation can either because of an explicit

eval()

call or
an automatic update triggered by a dependency.

unresolvedDependencies

```java
public
Stream
<
String
> unresolvedDependencies​(
DeclarationSnippet
snippet)
```

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.
The returned value of this method, for a given method may change when an

eval()

or

drop()

of another snippet causes
an update of a dependency.

**Parameters:** snippet

- the declaration

Snippet

to look up
**Returns:** a stream of symbol names that are currently unresolvedDependencies.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.

---

#### unresolvedDependencies

public

Stream

<

String

> unresolvedDependencies​(

DeclarationSnippet

snippet)

For

RECOVERABLE_DEFINED

or

RECOVERABLE_NOT_DEFINED

declarations, the names of current unresolved dependencies for
the snippet.
The returned value of this method, for a given method may change when an

eval()

or

drop()

of another snippet causes
an update of a dependency.

varValue

```java
public
String
varValue​(
VarSnippet
snippet)
throws
IllegalStateException
```

Get the current value of a variable.

**Parameters:** snippet

- the variable Snippet whose value is queried.
**Returns:** the current value of the variable referenced by snippet.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.
**Throws:** IllegalArgumentException

- if the snippet is not associated with
this

JShell

instance.
**Throws:** IllegalArgumentException

- if the variable's status is anything but

Snippet.Status.VALID

.

---

#### varValue

public

String

varValue​(

VarSnippet

snippet)
throws

IllegalStateException

Get the current value of a variable.

onSnippetEvent

```java
public
JShell.Subscription
onSnippetEvent​(
Consumer
<
SnippetEvent
> listener)
throws
IllegalStateException
```

Register a callback to be called when the Status of a snippet changes.
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the Status changes.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this

JShell

instance is closed.

---

#### onSnippetEvent

public

JShell.Subscription

onSnippetEvent​(

Consumer

<

SnippetEvent

> listener)
throws

IllegalStateException

Register a callback to be called when the Status of a snippet changes.
Each call adds a new subscription.

onShutdown

```java
public
JShell.Subscription
onShutdown​(
Consumer
<
JShell
> listener)
throws
IllegalStateException
```

Register a callback to be called when this JShell instance terminates.
This occurs either because the client process has ended (e.g. called System.exit(0))
or the connection has been shutdown, as by close().
Each call adds a new subscription.

**Parameters:** listener

- Action to perform when the state terminates.
**Returns:** A token which can be used to

unsubscribe

this subscription.
**Throws:** IllegalStateException

- if this JShell instance is closed

---

#### onShutdown

public

JShell.Subscription

onShutdown​(

Consumer

<

JShell

> listener)
throws

IllegalStateException

Register a callback to be called when this JShell instance terminates.
This occurs either because the client process has ended (e.g. called System.exit(0))
or the connection has been shutdown, as by close().
Each call adds a new subscription.

unsubscribe

```java
public void unsubscribe​(
JShell.Subscription
token)
```

Cancel a callback subscription.

**Parameters:** token

- The token corresponding to the subscription to be unsubscribed.

---

#### unsubscribe

public void unsubscribe​(

JShell.Subscription

token)

Cancel a callback subscription.

---

