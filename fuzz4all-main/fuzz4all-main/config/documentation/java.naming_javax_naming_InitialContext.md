# Class InitialContext

**Source:** `java.naming\javax\naming\InitialContext.html`

### Class Description

```java
public class
InitialContext

extends
Object

implements
Context
```

This class is the starting context for performing naming operations.

All naming operations are relative to a context.
The initial context implements the Context interface and
provides the starting point for resolution of names.

When the initial context is constructed, its environment
is initialized with properties defined in the environment parameter
passed to the constructor, and in any

application resource files

.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

**All Implemented Interfaces:** Context

---

### Field Details

#### protected
Hashtable
<
Object
,​
Object
> myProps

The environment associated with this InitialContext.
It is initialized to null and is updated by the constructor
that accepts an environment or by the

init()

method.

**See Also:**
- Context.addToEnvironment(java.lang.String, java.lang.Object)

,

Context.removeFromEnvironment(java.lang.String)

,

Context.getEnvironment()

---

#### protected
Context
defaultInitCtx

Field holding the result of calling NamingManager.getInitialContext().
It is set by getDefaultInitCtx() the first time getDefaultInitCtx()
is called. Subsequent invocations of getDefaultInitCtx() return
the value of defaultInitCtx.

**See Also:**
- getDefaultInitCtx()

---

#### protected boolean gotDefault

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().
If true, its result is in

defaultInitCtx

.

---

### Constructor Details

#### protected InitialContext​(boolean lazy)
throws
NamingException

Constructs an initial context with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:**
- lazy

- true means do not initialize the initial context; false
is equivalent to calling

new InitialContext()

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- init(Hashtable)

**Since:**
- 1.3

---

#### public InitialContext()
throws
NamingException

Constructs an initial context.
No environment properties are supplied.
Equivalent to

new InitialContext(null)

.

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- InitialContext(Hashtable)

---

#### public InitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException

Constructs an initial context using the supplied environment.
Environment properties are discussed in the class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:**
- environment

- environment used to create the initial context.
Null indicates an empty environment.

**Throws:**
- NamingException

- if a naming exception is encountered

---

### Method Details

#### protected void init​(
Hashtable
<?,​?> environment)
throws
NamingException

Initializes the initial context using the supplied environment.
Environment properties are discussed in the class description.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

**Parameters:**
- environment

- environment used to create the initial context.
Null indicates an empty environment.

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- InitialContext(boolean)

**Since:**
- 1.3

---

#### public static <T> T doLookup​(
Name
name)
throws
NamingException

A static method to retrieve the named object.
This is a shortcut method equivalent to invoking:

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

**Parameters:**
- name

- the name of the object to look up

**Returns:**
- the object bound to

name

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- doLookup(String)

,

Context.lookup(Name)

**Since:**
- 1.6

**Type Parameters:**
- T

- the type of the returned object

---

#### public static <T> T doLookup​(
String
name)
throws
NamingException

A static method to retrieve the named object.
See

doLookup(Name)

for details.

**Parameters:**
- name

- the name of the object to look up

**Returns:**
- the object bound to

name

**Throws:**
- NamingException

- if a naming exception is encountered

**Since:**
- 1.6

**Type Parameters:**
- T

- the type of the returned object

---

#### protected
Context
getDefaultInitCtx()
throws
NamingException

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.
Set

gotDefault

so that we know we've tried this before.

**Returns:**
- The non-null cached initial context.

**Throws:**
- NoInitialContextException

- If cannot find an initial context.
- NamingException

- If a naming exception was encountered.

---

#### protected
Context
getURLOrDefaultInitCtx​(
String
name)
throws
NamingException

Retrieves a context for resolving the string name

name

.
If

name

name is a URL string, then attempt
to find a URL context for it. If none is found, or if

name

is not a URL string, then return

getDefaultInitCtx()

.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

**Parameters:**
- name

- The non-null name for which to get the context.

**Returns:**
- A URL context for

name

or the cached
initial context. The result cannot be null.

**Throws:**
- NoInitialContextException

- If cannot find an initial context.
- NamingException

- In a naming exception is encountered.

**See Also:**
- NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

---

#### protected
Context
getURLOrDefaultInitCtx​(
Name
name)
throws
NamingException

Retrieves a context for resolving

name

.
If the first component of

name

name is a URL string,
then attempt to find a URL context for it. If none is found, or if
the first component of

name

is not a URL string,
then return

getDefaultInitCtx()

.

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

**Parameters:**
- name

- The non-null name for which to get the context.

**Returns:**
- A URL context for

name

or the cached
initial context. The result cannot be null.

**Throws:**
- NoInitialContextException

- If cannot find an initial context.
- NamingException

- In a naming exception is encountered.

**See Also:**
- NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

---

#### public
String
composeName​(
String
name,

String
prefix)
throws
NamingException

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name (

""

).

**Specified by:**
- composeName

in interface

Context

**Parameters:**
- name

- a name relative to this context
- prefix

- the name of this context relative to one of its ancestors

**Returns:**
- the composition of

prefix

and

name

**Throws:**
- NamingException

- if a naming exception is encountered

---

#### public
Name
composeName​(
Name
name,

Name
prefix)
throws
NamingException

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name.

**Specified by:**
- composeName

in interface

Context

**Parameters:**
- name

- a name relative to this context
- prefix

- the name of this context relative to one of its ancestors

**Returns:**
- the composition of

prefix

and

name

**Throws:**
- NamingException

- if a naming exception is encountered

**See Also:**
- Context.composeName(String, String)

---

### Additional Sections

#### Class InitialContext

java.lang.Object

- javax.naming.InitialContext

javax.naming.InitialContext

**All Implemented Interfaces:** Context

**Direct Known Subclasses:** InitialDirContext

```java
public class
InitialContext

extends
Object

implements
Context
```

This class is the starting context for performing naming operations.

All naming operations are relative to a context.
The initial context implements the Context interface and
provides the starting point for resolution of names.

When the initial context is constructed, its environment
is initialized with properties defined in the environment parameter
passed to the constructor, and in any

application resource files

.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

**Since:** 1.3, JNDI 1.1
**See Also:** Context

,

NamingManager.setInitialContextFactoryBuilder

public class

InitialContext

extends

Object

implements

Context

This class is the starting context for performing naming operations.

All naming operations are relative to a context.
The initial context implements the Context interface and
provides the starting point for resolution of names.

When the initial context is constructed, its environment
is initialized with properties defined in the environment parameter
passed to the constructor, and in any

application resource files

.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

All naming operations are relative to a context.
The initial context implements the Context interface and
provides the starting point for resolution of names.

When the initial context is constructed, its environment
is initialized with properties defined in the environment parameter
passed to the constructor, and in any

application resource files

.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

When the initial context is constructed, its environment
is initialized with properties defined in the environment parameter
passed to the constructor, and in any

application resource files

.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

JNDI determines each property's value by merging
the values from the following two sources, in order:

- The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

For each property found in both of these two sources, or in
more than one application resource file, the property's value
is determined as follows. If the property is
one of the standard JNDI properties that specify a list of JNDI
factories (see

Context

),
all of the values are
concatenated into a single colon-separated list. For other
properties, only the first value found is used.

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

The first occurrence of the property from the constructor's
environment parameter and system properties.

The application resource files (

jndi.properties

).

The initial context implementation is determined at runtime.
The default policy uses the environment property
"

java.naming.factory.initial

",
which contains the class name of the initial context factory.
An exception to this policy is made when resolving URL strings, as described
below.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

When a URL string (a

String

of the form

scheme_id:rest_of_name

) is passed as a name parameter to
any method, a URL context factory for handling that scheme is
located and used to resolve the URL. If no such factory is found,
the initial context specified by

"java.naming.factory.initial"

is used. Similarly, when a

CompositeName

object whose first component is a URL string is
passed as a name parameter to any method, a URL context factory is
located and used to resolve the first name component.
See

NamingManager.getURLContext()

for a description of how URL
context factories are located.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

This default policy of locating the initial context and URL context
factories may be overridden
by calling

NamingManager.setInitialContextFactoryBuilder()

.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

NoInitialContextException is thrown when an initial context cannot
be instantiated. This exception can be thrown during any interaction
with the InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

When the environment property "java.naming.factory.initial" is
non-null, the InitialContext constructor will attempt to create the
initial context specified therein. At that time, the initial context factory
involved might throw an exception if a problem is encountered. However,
it is provider implementation-dependent when it verifies and indicates
to the users of the initial context any environment property- or
connection- related problems. It can do so lazily--delaying until
an operation is performed on the context, or eagerly, at the time
the context is constructed.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

An InitialContext instance is not synchronized against concurrent
access by multiple threads. Multiple threads each manipulating a
different InitialContext instance need not synchronize.
Threads that need to access a single InitialContext instance
concurrently should synchronize amongst themselves and provide the
necessary locking.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Context

defaultInitCtx

Field holding the result of calling NamingManager.getInitialContext().

protected boolean

gotDefault

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().

protected

Hashtable

<

Object

,​

Object

>

myProps

The environment associated with this InitialContext.

- Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

InitialContext

()

Constructs an initial context.

protected

InitialContext

​(boolean lazy)

Constructs an initial context with the option of not
initializing it.

InitialContext

​(

Hashtable

<?,​?> environment)

Constructs an initial context using the supplied environment.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

composeName

​(

String

name,

String

prefix)

Composes the name of this context with a name relative to
this context.

Name

composeName

​(

Name

name,

Name

prefix)

Composes the name of this context with a name relative to
this context.

static <T> T

doLookup

​(

String

name)

A static method to retrieve the named object.

static <T> T

doLookup

​(

Name

name)

A static method to retrieve the named object.

protected

Context

getDefaultInitCtx

()

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.

protected

Context

getURLOrDefaultInitCtx

​(

String

name)

Retrieves a context for resolving the string name

name

.

protected

Context

getURLOrDefaultInitCtx

​(

Name

name)

Retrieves a context for resolving

name

.

protected void

init

​(

Hashtable

<?,​?> environment)

Initializes the initial context using the supplied environment.

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

- Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

Field Summary

Fields

Modifier and Type

Field

Description

protected

Context

defaultInitCtx

Field holding the result of calling NamingManager.getInitialContext().

protected boolean

gotDefault

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().

protected

Hashtable

<

Object

,​

Object

>

myProps

The environment associated with this InitialContext.

- Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

---

#### Field Summary

Field holding the result of calling NamingManager.getInitialContext().

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().

The environment associated with this InitialContext.

Fields declared in interface javax.naming.

Context

APPLET

,

AUTHORITATIVE

,

BATCHSIZE

,

DNS_URL

,

INITIAL_CONTEXT_FACTORY

,

LANGUAGE

,

OBJECT_FACTORIES

,

PROVIDER_URL

,

REFERRAL

,

SECURITY_AUTHENTICATION

,

SECURITY_CREDENTIALS

,

SECURITY_PRINCIPAL

,

SECURITY_PROTOCOL

,

STATE_FACTORIES

,

URL_PKG_PREFIXES

---

#### Fields declared in interface javax.naming. Context

Constructor Summary

Constructors

Modifier

Constructor

Description

InitialContext

()

Constructs an initial context.

protected

InitialContext

​(boolean lazy)

Constructs an initial context with the option of not
initializing it.

InitialContext

​(

Hashtable

<?,​?> environment)

Constructs an initial context using the supplied environment.

---

#### Constructor Summary

Constructs an initial context.

Constructs an initial context with the option of not
initializing it.

Constructs an initial context using the supplied environment.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

composeName

​(

String

name,

String

prefix)

Composes the name of this context with a name relative to
this context.

Name

composeName

​(

Name

name,

Name

prefix)

Composes the name of this context with a name relative to
this context.

static <T> T

doLookup

​(

String

name)

A static method to retrieve the named object.

static <T> T

doLookup

​(

Name

name)

A static method to retrieve the named object.

protected

Context

getDefaultInitCtx

()

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.

protected

Context

getURLOrDefaultInitCtx

​(

String

name)

Retrieves a context for resolving the string name

name

.

protected

Context

getURLOrDefaultInitCtx

​(

Name

name)

Retrieves a context for resolving

name

.

protected void

init

​(

Hashtable

<?,​?> environment)

Initializes the initial context using the supplied environment.

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

- Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

---

#### Method Summary

Composes the name of this context with a name relative to
this context.

A static method to retrieve the named object.

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.

Retrieves a context for resolving the string name

name

.

Retrieves a context for resolving

name

.

Initializes the initial context using the supplied environment.

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

Methods declared in interface javax.naming.

Context

addToEnvironment

,

bind

,

bind

,

close

,

createSubcontext

,

createSubcontext

,

destroySubcontext

,

destroySubcontext

,

getEnvironment

,

getNameInNamespace

,

getNameParser

,

getNameParser

,

list

,

list

,

listBindings

,

listBindings

,

lookup

,

lookup

,

lookupLink

,

lookupLink

,

rebind

,

rebind

,

removeFromEnvironment

,

rename

,

rename

,

unbind

,

unbind

---

#### Methods declared in interface javax.naming. Context

============ FIELD DETAIL ===========

- Field Detail

- myProps

```java
protected
Hashtable
<
Object
,​
Object
> myProps
```

The environment associated with this InitialContext.
It is initialized to null and is updated by the constructor
that accepts an environment or by the

init()

method.

**See Also:** Context.addToEnvironment(java.lang.String, java.lang.Object)

,

Context.removeFromEnvironment(java.lang.String)

,

Context.getEnvironment()

- defaultInitCtx

```java
protected
Context
defaultInitCtx
```

Field holding the result of calling NamingManager.getInitialContext().
It is set by getDefaultInitCtx() the first time getDefaultInitCtx()
is called. Subsequent invocations of getDefaultInitCtx() return
the value of defaultInitCtx.

**See Also:** getDefaultInitCtx()

- gotDefault

```java
protected boolean gotDefault
```

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().
If true, its result is in

defaultInitCtx

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InitialContext

```java
protected InitialContext​(boolean lazy)
throws
NamingException
```

Constructs an initial context with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial context; false
is equivalent to calling

new InitialContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** init(Hashtable)

- InitialContext

```java
public InitialContext()
throws
NamingException
```

Constructs an initial context.
No environment properties are supplied.
Equivalent to

new InitialContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialContext(Hashtable)

- InitialContext

```java
public InitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial context using the supplied environment.
Environment properties are discussed in the class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

============ METHOD DETAIL ==========

- Method Detail

- init

```java
protected void init​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Initializes the initial context using the supplied environment.
Environment properties are discussed in the class description.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext(boolean)

- doLookup

```java
public static <T> T doLookup​(
Name
name)
throws
NamingException
```

A static method to retrieve the named object.
This is a shortcut method equivalent to invoking:

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6
**See Also:** doLookup(String)

,

Context.lookup(Name)

- doLookup

```java
public static <T> T doLookup​(
String
name)
throws
NamingException
```

A static method to retrieve the named object.
See

doLookup(Name)

for details.

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6

- getDefaultInitCtx

```java
protected
Context
getDefaultInitCtx()
throws
NamingException
```

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.
Set

gotDefault

so that we know we've tried this before.

**Returns:** The non-null cached initial context.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- If a naming exception was encountered.

- getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
String
name)
throws
NamingException
```

Retrieves a context for resolving the string name

name

.
If

name

name is a URL string, then attempt
to find a URL context for it. If none is found, or if

name

is not a URL string, then return

getDefaultInitCtx()

.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

- getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
Name
name)
throws
NamingException
```

Retrieves a context for resolving

name

.
If the first component of

name

name is a URL string,
then attempt to find a URL context for it. If none is found, or if
the first component of

name

is not a URL string,
then return

getDefaultInitCtx()

.

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

- composeName

```java
public
String
composeName​(
String
name,

String
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name (

""

).

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered

- composeName

```java
public
Name
composeName​(
Name
name,

Name
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name.

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** Context.composeName(String, String)

Field Detail

- myProps

```java
protected
Hashtable
<
Object
,​
Object
> myProps
```

The environment associated with this InitialContext.
It is initialized to null and is updated by the constructor
that accepts an environment or by the

init()

method.

**See Also:** Context.addToEnvironment(java.lang.String, java.lang.Object)

,

Context.removeFromEnvironment(java.lang.String)

,

Context.getEnvironment()

- defaultInitCtx

```java
protected
Context
defaultInitCtx
```

Field holding the result of calling NamingManager.getInitialContext().
It is set by getDefaultInitCtx() the first time getDefaultInitCtx()
is called. Subsequent invocations of getDefaultInitCtx() return
the value of defaultInitCtx.

**See Also:** getDefaultInitCtx()

- gotDefault

```java
protected boolean gotDefault
```

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().
If true, its result is in

defaultInitCtx

.

---

#### Field Detail

myProps

```java
protected
Hashtable
<
Object
,​
Object
> myProps
```

The environment associated with this InitialContext.
It is initialized to null and is updated by the constructor
that accepts an environment or by the

init()

method.

**See Also:** Context.addToEnvironment(java.lang.String, java.lang.Object)

,

Context.removeFromEnvironment(java.lang.String)

,

Context.getEnvironment()

---

#### myProps

protected

Hashtable

<

Object

,​

Object

> myProps

The environment associated with this InitialContext.
It is initialized to null and is updated by the constructor
that accepts an environment or by the

init()

method.

defaultInitCtx

```java
protected
Context
defaultInitCtx
```

Field holding the result of calling NamingManager.getInitialContext().
It is set by getDefaultInitCtx() the first time getDefaultInitCtx()
is called. Subsequent invocations of getDefaultInitCtx() return
the value of defaultInitCtx.

**See Also:** getDefaultInitCtx()

---

#### defaultInitCtx

protected

Context

defaultInitCtx

Field holding the result of calling NamingManager.getInitialContext().
It is set by getDefaultInitCtx() the first time getDefaultInitCtx()
is called. Subsequent invocations of getDefaultInitCtx() return
the value of defaultInitCtx.

gotDefault

```java
protected boolean gotDefault
```

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().
If true, its result is in

defaultInitCtx

.

---

#### gotDefault

protected boolean gotDefault

Field indicating whether the initial context has been obtained
by calling NamingManager.getInitialContext().
If true, its result is in

defaultInitCtx

.

Constructor Detail

- InitialContext

```java
protected InitialContext​(boolean lazy)
throws
NamingException
```

Constructs an initial context with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial context; false
is equivalent to calling

new InitialContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** init(Hashtable)

- InitialContext

```java
public InitialContext()
throws
NamingException
```

Constructs an initial context.
No environment properties are supplied.
Equivalent to

new InitialContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialContext(Hashtable)

- InitialContext

```java
public InitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial context using the supplied environment.
Environment properties are discussed in the class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

---

#### Constructor Detail

InitialContext

```java
protected InitialContext​(boolean lazy)
throws
NamingException
```

Constructs an initial context with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

**Parameters:** lazy

- true means do not initialize the initial context; false
is equivalent to calling

new InitialContext()
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** init(Hashtable)

---

#### InitialContext

protected InitialContext​(boolean lazy)
throws

NamingException

Constructs an initial context with the option of not
initializing it. This may be used by a constructor in
a subclass when the value of the environment parameter
is not yet known at the time the

InitialContext

constructor is called. The subclass's constructor will
call this constructor, compute the value of the environment,
and then call

init()

before returning.

InitialContext

```java
public InitialContext()
throws
NamingException
```

Constructs an initial context.
No environment properties are supplied.
Equivalent to

new InitialContext(null)

.

**Throws:** NamingException

- if a naming exception is encountered
**See Also:** InitialContext(Hashtable)

---

#### InitialContext

public InitialContext()
throws

NamingException

Constructs an initial context.
No environment properties are supplied.
Equivalent to

new InitialContext(null)

.

InitialContext

```java
public InitialContext​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Constructs an initial context using the supplied environment.
Environment properties are discussed in the class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered

---

#### InitialContext

public InitialContext​(

Hashtable

<?,​?> environment)
throws

NamingException

Constructs an initial context using the supplied environment.
Environment properties are discussed in the class description.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

This constructor will not modify

environment

or save a reference to it, but may save a clone.
Caller should not modify mutable keys and values in

environment

after it has been passed to the constructor.

Method Detail

- init

```java
protected void init​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Initializes the initial context using the supplied environment.
Environment properties are discussed in the class description.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext(boolean)

- doLookup

```java
public static <T> T doLookup​(
Name
name)
throws
NamingException
```

A static method to retrieve the named object.
This is a shortcut method equivalent to invoking:

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6
**See Also:** doLookup(String)

,

Context.lookup(Name)

- doLookup

```java
public static <T> T doLookup​(
String
name)
throws
NamingException
```

A static method to retrieve the named object.
See

doLookup(Name)

for details.

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6

- getDefaultInitCtx

```java
protected
Context
getDefaultInitCtx()
throws
NamingException
```

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.
Set

gotDefault

so that we know we've tried this before.

**Returns:** The non-null cached initial context.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- If a naming exception was encountered.

- getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
String
name)
throws
NamingException
```

Retrieves a context for resolving the string name

name

.
If

name

name is a URL string, then attempt
to find a URL context for it. If none is found, or if

name

is not a URL string, then return

getDefaultInitCtx()

.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

- getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
Name
name)
throws
NamingException
```

Retrieves a context for resolving

name

.
If the first component of

name

name is a URL string,
then attempt to find a URL context for it. If none is found, or if
the first component of

name

is not a URL string,
then return

getDefaultInitCtx()

.

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

- composeName

```java
public
String
composeName​(
String
name,

String
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name (

""

).

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered

- composeName

```java
public
Name
composeName​(
Name
name,

Name
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name.

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** Context.composeName(String, String)

---

#### Method Detail

init

```java
protected void init​(
Hashtable
<?,​?> environment)
throws
NamingException
```

Initializes the initial context using the supplied environment.
Environment properties are discussed in the class description.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

**Parameters:** environment

- environment used to create the initial context.
Null indicates an empty environment.
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.3
**See Also:** InitialContext(boolean)

---

#### init

protected void init​(

Hashtable

<?,​?> environment)
throws

NamingException

Initializes the initial context using the supplied environment.
Environment properties are discussed in the class description.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

This method will modify

environment

and save
a reference to it. The caller may no longer modify it.

doLookup

```java
public static <T> T doLookup​(
Name
name)
throws
NamingException
```

A static method to retrieve the named object.
This is a shortcut method equivalent to invoking:

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6
**See Also:** doLookup(String)

,

Context.lookup(Name)

---

#### doLookup

public static <T> T doLookup​(

Name

name)
throws

NamingException

A static method to retrieve the named object.
This is a shortcut method equivalent to invoking:

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

InitialContext ic = new InitialContext();
Object obj = ic.lookup();

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

If

name

is empty, returns a new instance of this context
(which represents the same naming context as this context, but its
environment may be modified independently and it may be accessed
concurrently).

doLookup

```java
public static <T> T doLookup​(
String
name)
throws
NamingException
```

A static method to retrieve the named object.
See

doLookup(Name)

for details.

**Type Parameters:** T

- the type of the returned object
**Parameters:** name

- the name of the object to look up
**Returns:** the object bound to

name
**Throws:** NamingException

- if a naming exception is encountered
**Since:** 1.6

---

#### doLookup

public static <T> T doLookup​(

String

name)
throws

NamingException

A static method to retrieve the named object.
See

doLookup(Name)

for details.

getDefaultInitCtx

```java
protected
Context
getDefaultInitCtx()
throws
NamingException
```

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.
Set

gotDefault

so that we know we've tried this before.

**Returns:** The non-null cached initial context.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- If a naming exception was encountered.

---

#### getDefaultInitCtx

protected

Context

getDefaultInitCtx()
throws

NamingException

Retrieves the initial context by calling

NamingManager.getInitialContext()

and cache it in defaultInitCtx.
Set

gotDefault

so that we know we've tried this before.

getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
String
name)
throws
NamingException
```

Retrieves a context for resolving the string name

name

.
If

name

name is a URL string, then attempt
to find a URL context for it. If none is found, or if

name

is not a URL string, then return

getDefaultInitCtx()

.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

---

#### getURLOrDefaultInitCtx

protected

Context

getURLOrDefaultInitCtx​(

String

name)
throws

NamingException

Retrieves a context for resolving the string name

name

.
If

name

name is a URL string, then attempt
to find a URL context for it. If none is found, or if

name

is not a URL string, then return

getDefaultInitCtx()

.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

See getURLOrDefaultInitCtx(Name) for description
of how a subclass should use this method.

getURLOrDefaultInitCtx

```java
protected
Context
getURLOrDefaultInitCtx​(
Name
name)
throws
NamingException
```

Retrieves a context for resolving

name

.
If the first component of

name

name is a URL string,
then attempt to find a URL context for it. If none is found, or if
the first component of

name

is not a URL string,
then return

getDefaultInitCtx()

.

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

**Parameters:** name

- The non-null name for which to get the context.
**Returns:** A URL context for

name

or the cached
initial context. The result cannot be null.
**Throws:** NoInitialContextException

- If cannot find an initial context.
**Throws:** NamingException

- In a naming exception is encountered.
**See Also:** NamingManager.getURLContext(java.lang.String, java.util.Hashtable<?, ?>)

---

#### getURLOrDefaultInitCtx

protected

Context

getURLOrDefaultInitCtx​(

Name

name)
throws

NamingException

Retrieves a context for resolving

name

.
If the first component of

name

name is a URL string,
then attempt to find a URL context for it. If none is found, or if
the first component of

name

is not a URL string,
then return

getDefaultInitCtx()

.

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

When creating a subclass of InitialContext, use this method as
follows.
Define a new method that uses this method to get an initial
context of the desired subclass.

```java
protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}
```

When providing implementations for the new methods in the subclass,
use this newly defined method to get the initial context.

```java
public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}
```

protected XXXContext getURLOrDefaultInitXXXCtx(Name name)
throws NamingException {
Context answer = getURLOrDefaultInitCtx(name);
if (!(answer instanceof XXXContext)) {
if (answer == null) {
throw new NoInitialContextException();
} else {
throw new NotContextException("Not an XXXContext");
}
}
return (XXXContext)answer;
}

public Object XXXMethod1(Name name, ...) {
throws NamingException {
return getURLOrDefaultInitXXXCtx(name).XXXMethod1(name, ...);
}

composeName

```java
public
String
composeName​(
String
name,

String
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name (

""

).

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered

---

#### composeName

public

String

composeName​(

String

name,

String

prefix)
throws

NamingException

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name (

""

).

composeName

```java
public
Name
composeName​(
Name
name,

Name
prefix)
throws
NamingException
```

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name.

**Specified by:** composeName

in interface

Context
**Parameters:** name

- a name relative to this context
**Parameters:** prefix

- the name of this context relative to one of its ancestors
**Returns:** the composition of

prefix

and

name
**Throws:** NamingException

- if a naming exception is encountered
**See Also:** Context.composeName(String, String)

---

#### composeName

public

Name

composeName​(

Name

name,

Name

prefix)
throws

NamingException

Composes the name of this context with a name relative to
this context.
Since an initial context may never be named relative
to any context other than itself, the value of the

prefix

parameter must be an empty name.

---

