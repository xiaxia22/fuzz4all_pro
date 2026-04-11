# Interface Resolver

**Source:** `java.naming\javax\naming\spi\Resolver.html`

### Class Description

```java
public interface
Resolver
```

This interface represents an "intermediate context" for name resolution.

The Resolver interface contains methods that are implemented by contexts
that do not support subtypes of Context, but which can act as
intermediate contexts for resolution purposes.

A

Name

parameter passed to any method is owned
by the caller. The service provider will not modify the object
or keep a reference to it.
A

ResolveResult

object returned by any
method is owned by the caller. The caller may subsequently modify it;
the service provider may not.

**Since:** 1.3

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ResolveResult
resolveToClass​(
Name
name,

Class
<? extends
Context
> contextType)
throws
NamingException

Partially resolves a name. Stops at the first
context that is an instance of a given subtype of

Context

.

**Parameters:**
- name

- the name to resolve
- contextType

- the type of object to resolve. This should
be a subtype of

Context

.

**Returns:**
- the object that was found, along with the unresolved
suffix of

name

. Cannot be null.

**Throws:**
- NotContextException

- if no context of the appropriate type is found
- NamingException

- if a naming exception was encountered

**See Also:**
- resolveToClass(String, Class)

---

#### ResolveResult
resolveToClass​(
String
name,

Class
<? extends
Context
> contextType)
throws
NamingException

Partially resolves a name.
See

resolveToClass(Name, Class)

for details.

**Parameters:**
- name

- the name to resolve
- contextType

- the type of object to resolve. This should
be a subtype of

Context

.

**Returns:**
- the object that was found, along with the unresolved
suffix of

name

. Cannot be null.

**Throws:**
- NotContextException

- if no context of the appropriate type is found
- NamingException

- if a naming exception was encountered

---

### Additional Sections

#### Interface Resolver

```java
public interface
Resolver
```

This interface represents an "intermediate context" for name resolution.

The Resolver interface contains methods that are implemented by contexts
that do not support subtypes of Context, but which can act as
intermediate contexts for resolution purposes.

A

Name

parameter passed to any method is owned
by the caller. The service provider will not modify the object
or keep a reference to it.
A

ResolveResult

object returned by any
method is owned by the caller. The caller may subsequently modify it;
the service provider may not.

**Since:** 1.3

public interface

Resolver

This interface represents an "intermediate context" for name resolution.

The Resolver interface contains methods that are implemented by contexts
that do not support subtypes of Context, but which can act as
intermediate contexts for resolution purposes.

A

Name

parameter passed to any method is owned
by the caller. The service provider will not modify the object
or keep a reference to it.
A

ResolveResult

object returned by any
method is owned by the caller. The caller may subsequently modify it;
the service provider may not.

The Resolver interface contains methods that are implemented by contexts
that do not support subtypes of Context, but which can act as
intermediate contexts for resolution purposes.

A

Name

parameter passed to any method is owned
by the caller. The service provider will not modify the object
or keep a reference to it.
A

ResolveResult

object returned by any
method is owned by the caller. The caller may subsequently modify it;
the service provider may not.

A

Name

parameter passed to any method is owned
by the caller. The service provider will not modify the object
or keep a reference to it.
A

ResolveResult

object returned by any
method is owned by the caller. The caller may subsequently modify it;
the service provider may not.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ResolveResult

resolveToClass

​(

String

name,

Class

<? extends

Context

> contextType)

Partially resolves a name.

ResolveResult

resolveToClass

​(

Name

name,

Class

<? extends

Context

> contextType)

Partially resolves a name.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ResolveResult

resolveToClass

​(

String

name,

Class

<? extends

Context

> contextType)

Partially resolves a name.

ResolveResult

resolveToClass

​(

Name

name,

Class

<? extends

Context

> contextType)

Partially resolves a name.

---

#### Method Summary

Partially resolves a name.

============ METHOD DETAIL ==========

- Method Detail

- resolveToClass

```java
ResolveResult
resolveToClass​(
Name
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name. Stops at the first
context that is an instance of a given subtype of

Context

.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered
**See Also:** resolveToClass(String, Class)

- resolveToClass

```java
ResolveResult
resolveToClass​(
String
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name.
See

resolveToClass(Name, Class)

for details.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered

Method Detail

- resolveToClass

```java
ResolveResult
resolveToClass​(
Name
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name. Stops at the first
context that is an instance of a given subtype of

Context

.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered
**See Also:** resolveToClass(String, Class)

- resolveToClass

```java
ResolveResult
resolveToClass​(
String
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name.
See

resolveToClass(Name, Class)

for details.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered

---

#### Method Detail

resolveToClass

```java
ResolveResult
resolveToClass​(
Name
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name. Stops at the first
context that is an instance of a given subtype of

Context

.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered
**See Also:** resolveToClass(String, Class)

---

#### resolveToClass

ResolveResult

resolveToClass​(

Name

name,

Class

<? extends

Context

> contextType)
throws

NamingException

Partially resolves a name. Stops at the first
context that is an instance of a given subtype of

Context

.

resolveToClass

```java
ResolveResult
resolveToClass​(
String
name,

Class
<? extends
Context
> contextType)
throws
NamingException
```

Partially resolves a name.
See

resolveToClass(Name, Class)

for details.

**Parameters:** name

- the name to resolve
**Parameters:** contextType

- the type of object to resolve. This should
be a subtype of

Context

.
**Returns:** the object that was found, along with the unresolved
suffix of

name

. Cannot be null.
**Throws:** NotContextException

- if no context of the appropriate type is found
**Throws:** NamingException

- if a naming exception was encountered

---

#### resolveToClass

ResolveResult

resolveToClass​(

String

name,

Class

<? extends

Context

> contextType)
throws

NamingException

Partially resolves a name.
See

resolveToClass(Name, Class)

for details.

---

