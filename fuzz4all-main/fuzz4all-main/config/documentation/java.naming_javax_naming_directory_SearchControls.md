# Class SearchControls

**Source:** `java.naming\javax\naming\directory\SearchControls.html`

### Class Description

```java
public class
SearchControls

extends
Object

implements
Serializable
```

This class encapsulates
factors that determine scope of search and what gets returned
as a result of the search.

A SearchControls instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single SearchControls instance should lock the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int OBJECT_SCOPE

Search the named object.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

**See Also:**
- Constant Field Values

---

#### public static final int ONELEVEL_SCOPE

Search one level of the named context.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

**See Also:**
- Constant Field Values

---

#### public static final int SUBTREE_SCOPE

Search the entire subtree rooted at the named object.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public SearchControls()

Constructs a search constraints using defaults.

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

---

#### public SearchControls​(int scope,
long countlim,
int timelim,

String
[] attrs,
boolean retobj,
boolean deref)

Constructs a search constraints using arguments.

**Parameters:**
- scope

- The search scope. One of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.
- timelim

- The number of milliseconds to wait before returning.
If 0, wait indefinitely.
- deref

- If true, dereference links during search.
- countlim

- The maximum number of entries to return. If 0, return
all entries that satisfy filter.
- retobj

- If true, return the object bound to the name of the
entry; if false, do not return object.
- attrs

- The identifiers of the attributes to return along with
the entry. If null, return all attributes. If empty
return no attributes.

---

### Method Details

#### public int getSearchScope()

Retrieves the search scope of these SearchControls.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Returns:**
- The search scope of this SearchControls.

**See Also:**
- setSearchScope(int)

---

#### public int getTimeLimit()

Retrieves the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Returns:**
- The time limit of these SearchControls in milliseconds.

**See Also:**
- setTimeLimit(int)

---

#### public boolean getDerefLinkFlag()

Determines whether links will be dereferenced during the search.

**Returns:**
- true if links will be dereferenced; false otherwise.

**See Also:**
- setDerefLinkFlag(boolean)

---

#### public boolean getReturningObjFlag()

Determines whether objects will be returned as part of the result.

**Returns:**
- true if objects will be returned; false otherwise.

**See Also:**
- setReturningObjFlag(boolean)

---

#### public long getCountLimit()

Retrieves the maximum number of entries that will be returned
as a result of the search.

0 indicates that all entries will be returned.

**Returns:**
- The maximum number of entries that will be returned.

**See Also:**
- setCountLimit(long)

---

#### public
String
[] getReturningAttributes()

Retrieves the attributes that will be returned as part of the search.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

**Returns:**
- An array of attribute ids identifying the attributes that
will be returned. Can be null.

**See Also:**
- setReturningAttributes(java.lang.String[])

---

#### public void setSearchScope​(int scope)

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Parameters:**
- scope

- The search scope of this SearchControls.

**See Also:**
- getSearchScope()

---

#### public void setTimeLimit​(int ms)

Sets the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Parameters:**
- ms

- The time limit of these SearchControls in milliseconds.

**See Also:**
- getTimeLimit()

---

#### public void setDerefLinkFlag​(boolean on)

Enables/disables link dereferencing during the search.

**Parameters:**
- on

- if true links will be dereferenced; if false, not followed.

**See Also:**
- getDerefLinkFlag()

---

#### public void setReturningObjFlag​(boolean on)

Enables/disables returning objects returned as part of the result.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

**Parameters:**
- on

- if true, objects will be returned; if false,
objects will not be returned.

**See Also:**
- getReturningObjFlag()

---

#### public void setCountLimit​(long limit)

Sets the maximum number of entries to be returned
as a result of the search.

0 indicates no limit: all entries will be returned.

**Parameters:**
- limit

- The maximum number of entries that will be returned.

**See Also:**
- getCountLimit()

---

#### public void setReturningAttributes​(
String
[] attrs)

Specifies the attributes that will be returned as part of the search.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

**Parameters:**
- attrs

- An array of attribute ids identifying the attributes that
will be returned. Can be null.

**See Also:**
- getReturningAttributes()

---

### Additional Sections

#### Class SearchControls

java.lang.Object

- javax.naming.directory.SearchControls

javax.naming.directory.SearchControls

**All Implemented Interfaces:** Serializable

```java
public class
SearchControls

extends
Object

implements
Serializable
```

This class encapsulates
factors that determine scope of search and what gets returned
as a result of the search.

A SearchControls instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single SearchControls instance should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

SearchControls

extends

Object

implements

Serializable

This class encapsulates
factors that determine scope of search and what gets returned
as a result of the search.

A SearchControls instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single SearchControls instance should lock the object.

A SearchControls instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify
a single SearchControls instance should lock the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

OBJECT_SCOPE

Search the named object.

static int

ONELEVEL_SCOPE

Search one level of the named context.

static int

SUBTREE_SCOPE

Search the entire subtree rooted at the named object.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SearchControls

()

Constructs a search constraints using defaults.

SearchControls

​(int scope,
long countlim,
int timelim,

String

[] attrs,
boolean retobj,
boolean deref)

Constructs a search constraints using arguments.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getCountLimit

()

Retrieves the maximum number of entries that will be returned
as a result of the search.

boolean

getDerefLinkFlag

()

Determines whether links will be dereferenced during the search.

String

[]

getReturningAttributes

()

Retrieves the attributes that will be returned as part of the search.

boolean

getReturningObjFlag

()

Determines whether objects will be returned as part of the result.

int

getSearchScope

()

Retrieves the search scope of these SearchControls.

int

getTimeLimit

()

Retrieves the time limit of these SearchControls in milliseconds.

void

setCountLimit

​(long limit)

Sets the maximum number of entries to be returned
as a result of the search.

void

setDerefLinkFlag

​(boolean on)

Enables/disables link dereferencing during the search.

void

setReturningAttributes

​(

String

[] attrs)

Specifies the attributes that will be returned as part of the search.

void

setReturningObjFlag

​(boolean on)

Enables/disables returning objects returned as part of the result.

void

setSearchScope

​(int scope)

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

void

setTimeLimit

​(int ms)

Sets the time limit of these SearchControls in milliseconds.

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

Field Summary

Fields

Modifier and Type

Field

Description

static int

OBJECT_SCOPE

Search the named object.

static int

ONELEVEL_SCOPE

Search one level of the named context.

static int

SUBTREE_SCOPE

Search the entire subtree rooted at the named object.

---

#### Field Summary

Search the named object.

Search one level of the named context.

Search the entire subtree rooted at the named object.

Constructor Summary

Constructors

Constructor

Description

SearchControls

()

Constructs a search constraints using defaults.

SearchControls

​(int scope,
long countlim,
int timelim,

String

[] attrs,
boolean retobj,
boolean deref)

Constructs a search constraints using arguments.

---

#### Constructor Summary

Constructs a search constraints using defaults.

Constructs a search constraints using arguments.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

long

getCountLimit

()

Retrieves the maximum number of entries that will be returned
as a result of the search.

boolean

getDerefLinkFlag

()

Determines whether links will be dereferenced during the search.

String

[]

getReturningAttributes

()

Retrieves the attributes that will be returned as part of the search.

boolean

getReturningObjFlag

()

Determines whether objects will be returned as part of the result.

int

getSearchScope

()

Retrieves the search scope of these SearchControls.

int

getTimeLimit

()

Retrieves the time limit of these SearchControls in milliseconds.

void

setCountLimit

​(long limit)

Sets the maximum number of entries to be returned
as a result of the search.

void

setDerefLinkFlag

​(boolean on)

Enables/disables link dereferencing during the search.

void

setReturningAttributes

​(

String

[] attrs)

Specifies the attributes that will be returned as part of the search.

void

setReturningObjFlag

​(boolean on)

Enables/disables returning objects returned as part of the result.

void

setSearchScope

​(int scope)

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

void

setTimeLimit

​(int ms)

Sets the time limit of these SearchControls in milliseconds.

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

Retrieves the maximum number of entries that will be returned
as a result of the search.

Determines whether links will be dereferenced during the search.

Retrieves the attributes that will be returned as part of the search.

Determines whether objects will be returned as part of the result.

Retrieves the search scope of these SearchControls.

Retrieves the time limit of these SearchControls in milliseconds.

Sets the maximum number of entries to be returned
as a result of the search.

Enables/disables link dereferencing during the search.

Specifies the attributes that will be returned as part of the search.

Enables/disables returning objects returned as part of the result.

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

Sets the time limit of these SearchControls in milliseconds.

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

============ FIELD DETAIL ===========

- Field Detail

- OBJECT_SCOPE

```java
public static final int OBJECT_SCOPE
```

Search the named object.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

**See Also:** Constant Field Values

- ONELEVEL_SCOPE

```java
public static final int ONELEVEL_SCOPE
```

Search one level of the named context.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

**See Also:** Constant Field Values

- SUBTREE_SCOPE

```java
public static final int SUBTREE_SCOPE
```

Search the entire subtree rooted at the named object.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SearchControls

```java
public SearchControls()
```

Constructs a search constraints using defaults.

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

- SearchControls

```java
public SearchControls​(int scope,
long countlim,
int timelim,

String
[] attrs,
boolean retobj,
boolean deref)
```

Constructs a search constraints using arguments.

**Parameters:** scope

- The search scope. One of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.
**Parameters:** timelim

- The number of milliseconds to wait before returning.
If 0, wait indefinitely.
**Parameters:** deref

- If true, dereference links during search.
**Parameters:** countlim

- The maximum number of entries to return. If 0, return
all entries that satisfy filter.
**Parameters:** retobj

- If true, return the object bound to the name of the
entry; if false, do not return object.
**Parameters:** attrs

- The identifiers of the attributes to return along with
the entry. If null, return all attributes. If empty
return no attributes.

============ METHOD DETAIL ==========

- Method Detail

- getSearchScope

```java
public int getSearchScope()
```

Retrieves the search scope of these SearchControls.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Returns:** The search scope of this SearchControls.
**See Also:** setSearchScope(int)

- getTimeLimit

```java
public int getTimeLimit()
```

Retrieves the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Returns:** The time limit of these SearchControls in milliseconds.
**See Also:** setTimeLimit(int)

- getDerefLinkFlag

```java
public boolean getDerefLinkFlag()
```

Determines whether links will be dereferenced during the search.

**Returns:** true if links will be dereferenced; false otherwise.
**See Also:** setDerefLinkFlag(boolean)

- getReturningObjFlag

```java
public boolean getReturningObjFlag()
```

Determines whether objects will be returned as part of the result.

**Returns:** true if objects will be returned; false otherwise.
**See Also:** setReturningObjFlag(boolean)

- getCountLimit

```java
public long getCountLimit()
```

Retrieves the maximum number of entries that will be returned
as a result of the search.

0 indicates that all entries will be returned.

**Returns:** The maximum number of entries that will be returned.
**See Also:** setCountLimit(long)

- getReturningAttributes

```java
public
String
[] getReturningAttributes()
```

Retrieves the attributes that will be returned as part of the search.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

**Returns:** An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** setReturningAttributes(java.lang.String[])

- setSearchScope

```java
public void setSearchScope​(int scope)
```

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Parameters:** scope

- The search scope of this SearchControls.
**See Also:** getSearchScope()

- setTimeLimit

```java
public void setTimeLimit​(int ms)
```

Sets the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Parameters:** ms

- The time limit of these SearchControls in milliseconds.
**See Also:** getTimeLimit()

- setDerefLinkFlag

```java
public void setDerefLinkFlag​(boolean on)
```

Enables/disables link dereferencing during the search.

**Parameters:** on

- if true links will be dereferenced; if false, not followed.
**See Also:** getDerefLinkFlag()

- setReturningObjFlag

```java
public void setReturningObjFlag​(boolean on)
```

Enables/disables returning objects returned as part of the result.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

**Parameters:** on

- if true, objects will be returned; if false,
objects will not be returned.
**See Also:** getReturningObjFlag()

- setCountLimit

```java
public void setCountLimit​(long limit)
```

Sets the maximum number of entries to be returned
as a result of the search.

0 indicates no limit: all entries will be returned.

**Parameters:** limit

- The maximum number of entries that will be returned.
**See Also:** getCountLimit()

- setReturningAttributes

```java
public void setReturningAttributes​(
String
[] attrs)
```

Specifies the attributes that will be returned as part of the search.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

**Parameters:** attrs

- An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** getReturningAttributes()

Field Detail

- OBJECT_SCOPE

```java
public static final int OBJECT_SCOPE
```

Search the named object.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

**See Also:** Constant Field Values

- ONELEVEL_SCOPE

```java
public static final int ONELEVEL_SCOPE
```

Search one level of the named context.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

**See Also:** Constant Field Values

- SUBTREE_SCOPE

```java
public static final int SUBTREE_SCOPE
```

Search the entire subtree rooted at the named object.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

**See Also:** Constant Field Values

---

#### Field Detail

OBJECT_SCOPE

```java
public static final int OBJECT_SCOPE
```

Search the named object.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

**See Also:** Constant Field Values

---

#### OBJECT_SCOPE

public static final int OBJECT_SCOPE

Search the named object.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

The NamingEnumeration that results from search()
using OBJECT_SCOPE will contain one or zero element.
The enumeration contains one element if the named object satisfies
the search filter specified in search().
The element will have as its name the empty string because the names
of elements in the NamingEnumeration are relative to the
target context--in this case, the target context is the named object.
It contains zero element if the named object does not satisfy
the search filter specified in search().

The value of this constant is

0

.

The value of this constant is

0

.

ONELEVEL_SCOPE

```java
public static final int ONELEVEL_SCOPE
```

Search one level of the named context.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

**See Also:** Constant Field Values

---

#### ONELEVEL_SCOPE

public static final int ONELEVEL_SCOPE

Search one level of the named context.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

The NamingEnumeration that results from search()
using ONELEVEL_SCOPE contains elements with
objects in the named context that satisfy
the search filter specified in search().
The names of elements in the NamingEnumeration are atomic names
relative to the named context.

The value of this constant is

1

.

The value of this constant is

1

.

SUBTREE_SCOPE

```java
public static final int SUBTREE_SCOPE
```

Search the entire subtree rooted at the named object.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

**See Also:** Constant Field Values

---

#### SUBTREE_SCOPE

public static final int SUBTREE_SCOPE

Search the entire subtree rooted at the named object.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

If the named object is not a DirContext, search only the object.
If the named object is a DirContext, search the subtree
rooted at the named object, including the named object itself.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

The search will not cross naming system boundaries.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

The NamingEnumeration that results from search()
using SUBTREE_SCOPE contains elements of objects
from the subtree (including the named context)
that satisfy the search filter specified in search().
The names of elements in the NamingEnumeration are either
relative to the named context or is a URL string.
If the named context satisfies the search filter, it is
included in the enumeration with the empty string as
its name.

The value of this constant is

2

.

The value of this constant is

2

.

Constructor Detail

- SearchControls

```java
public SearchControls()
```

Constructs a search constraints using defaults.

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

- SearchControls

```java
public SearchControls​(int scope,
long countlim,
int timelim,

String
[] attrs,
boolean retobj,
boolean deref)
```

Constructs a search constraints using arguments.

**Parameters:** scope

- The search scope. One of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.
**Parameters:** timelim

- The number of milliseconds to wait before returning.
If 0, wait indefinitely.
**Parameters:** deref

- If true, dereference links during search.
**Parameters:** countlim

- The maximum number of entries to return. If 0, return
all entries that satisfy filter.
**Parameters:** retobj

- If true, return the object bound to the name of the
entry; if false, do not return object.
**Parameters:** attrs

- The identifiers of the attributes to return along with
the entry. If null, return all attributes. If empty
return no attributes.

---

#### Constructor Detail

SearchControls

```java
public SearchControls()
```

Constructs a search constraints using defaults.

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

---

#### SearchControls

public SearchControls()

Constructs a search constraints using defaults.

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

The defaults are:

- search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

search one level

no maximum return limit for search results

no time limit for search

return all attributes associated with objects that satisfy
the search filter.

do not return named object (return only name and class)

do not dereference links during search

SearchControls

```java
public SearchControls​(int scope,
long countlim,
int timelim,

String
[] attrs,
boolean retobj,
boolean deref)
```

Constructs a search constraints using arguments.

**Parameters:** scope

- The search scope. One of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.
**Parameters:** timelim

- The number of milliseconds to wait before returning.
If 0, wait indefinitely.
**Parameters:** deref

- If true, dereference links during search.
**Parameters:** countlim

- The maximum number of entries to return. If 0, return
all entries that satisfy filter.
**Parameters:** retobj

- If true, return the object bound to the name of the
entry; if false, do not return object.
**Parameters:** attrs

- The identifiers of the attributes to return along with
the entry. If null, return all attributes. If empty
return no attributes.

---

#### SearchControls

public SearchControls​(int scope,
long countlim,
int timelim,

String

[] attrs,
boolean retobj,
boolean deref)

Constructs a search constraints using arguments.

Method Detail

- getSearchScope

```java
public int getSearchScope()
```

Retrieves the search scope of these SearchControls.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Returns:** The search scope of this SearchControls.
**See Also:** setSearchScope(int)

- getTimeLimit

```java
public int getTimeLimit()
```

Retrieves the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Returns:** The time limit of these SearchControls in milliseconds.
**See Also:** setTimeLimit(int)

- getDerefLinkFlag

```java
public boolean getDerefLinkFlag()
```

Determines whether links will be dereferenced during the search.

**Returns:** true if links will be dereferenced; false otherwise.
**See Also:** setDerefLinkFlag(boolean)

- getReturningObjFlag

```java
public boolean getReturningObjFlag()
```

Determines whether objects will be returned as part of the result.

**Returns:** true if objects will be returned; false otherwise.
**See Also:** setReturningObjFlag(boolean)

- getCountLimit

```java
public long getCountLimit()
```

Retrieves the maximum number of entries that will be returned
as a result of the search.

0 indicates that all entries will be returned.

**Returns:** The maximum number of entries that will be returned.
**See Also:** setCountLimit(long)

- getReturningAttributes

```java
public
String
[] getReturningAttributes()
```

Retrieves the attributes that will be returned as part of the search.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

**Returns:** An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** setReturningAttributes(java.lang.String[])

- setSearchScope

```java
public void setSearchScope​(int scope)
```

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Parameters:** scope

- The search scope of this SearchControls.
**See Also:** getSearchScope()

- setTimeLimit

```java
public void setTimeLimit​(int ms)
```

Sets the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Parameters:** ms

- The time limit of these SearchControls in milliseconds.
**See Also:** getTimeLimit()

- setDerefLinkFlag

```java
public void setDerefLinkFlag​(boolean on)
```

Enables/disables link dereferencing during the search.

**Parameters:** on

- if true links will be dereferenced; if false, not followed.
**See Also:** getDerefLinkFlag()

- setReturningObjFlag

```java
public void setReturningObjFlag​(boolean on)
```

Enables/disables returning objects returned as part of the result.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

**Parameters:** on

- if true, objects will be returned; if false,
objects will not be returned.
**See Also:** getReturningObjFlag()

- setCountLimit

```java
public void setCountLimit​(long limit)
```

Sets the maximum number of entries to be returned
as a result of the search.

0 indicates no limit: all entries will be returned.

**Parameters:** limit

- The maximum number of entries that will be returned.
**See Also:** getCountLimit()

- setReturningAttributes

```java
public void setReturningAttributes​(
String
[] attrs)
```

Specifies the attributes that will be returned as part of the search.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

**Parameters:** attrs

- An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** getReturningAttributes()

---

#### Method Detail

getSearchScope

```java
public int getSearchScope()
```

Retrieves the search scope of these SearchControls.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Returns:** The search scope of this SearchControls.
**See Also:** setSearchScope(int)

---

#### getSearchScope

public int getSearchScope()

Retrieves the search scope of these SearchControls.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

One of OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

getTimeLimit

```java
public int getTimeLimit()
```

Retrieves the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Returns:** The time limit of these SearchControls in milliseconds.
**See Also:** setTimeLimit(int)

---

#### getTimeLimit

public int getTimeLimit()

Retrieves the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

If the value is 0, this means to wait indefinitely.

getDerefLinkFlag

```java
public boolean getDerefLinkFlag()
```

Determines whether links will be dereferenced during the search.

**Returns:** true if links will be dereferenced; false otherwise.
**See Also:** setDerefLinkFlag(boolean)

---

#### getDerefLinkFlag

public boolean getDerefLinkFlag()

Determines whether links will be dereferenced during the search.

getReturningObjFlag

```java
public boolean getReturningObjFlag()
```

Determines whether objects will be returned as part of the result.

**Returns:** true if objects will be returned; false otherwise.
**See Also:** setReturningObjFlag(boolean)

---

#### getReturningObjFlag

public boolean getReturningObjFlag()

Determines whether objects will be returned as part of the result.

getCountLimit

```java
public long getCountLimit()
```

Retrieves the maximum number of entries that will be returned
as a result of the search.

0 indicates that all entries will be returned.

**Returns:** The maximum number of entries that will be returned.
**See Also:** setCountLimit(long)

---

#### getCountLimit

public long getCountLimit()

Retrieves the maximum number of entries that will be returned
as a result of the search.

0 indicates that all entries will be returned.

0 indicates that all entries will be returned.

getReturningAttributes

```java
public
String
[] getReturningAttributes()
```

Retrieves the attributes that will be returned as part of the search.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

**Returns:** An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** setReturningAttributes(java.lang.String[])

---

#### getReturningAttributes

public

String

[] getReturningAttributes()

Retrieves the attributes that will be returned as part of the search.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

A value of null indicates that all attributes will be returned.
An empty array indicates that no attributes are to be returned.

setSearchScope

```java
public void setSearchScope​(int scope)
```

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

**Parameters:** scope

- The search scope of this SearchControls.
**See Also:** getSearchScope()

---

#### setSearchScope

public void setSearchScope​(int scope)

Sets the search scope to one of:
OBJECT_SCOPE, ONELEVEL_SCOPE, SUBTREE_SCOPE.

setTimeLimit

```java
public void setTimeLimit​(int ms)
```

Sets the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

**Parameters:** ms

- The time limit of these SearchControls in milliseconds.
**See Also:** getTimeLimit()

---

#### setTimeLimit

public void setTimeLimit​(int ms)

Sets the time limit of these SearchControls in milliseconds.

If the value is 0, this means to wait indefinitely.

If the value is 0, this means to wait indefinitely.

setDerefLinkFlag

```java
public void setDerefLinkFlag​(boolean on)
```

Enables/disables link dereferencing during the search.

**Parameters:** on

- if true links will be dereferenced; if false, not followed.
**See Also:** getDerefLinkFlag()

---

#### setDerefLinkFlag

public void setDerefLinkFlag​(boolean on)

Enables/disables link dereferencing during the search.

setReturningObjFlag

```java
public void setReturningObjFlag​(boolean on)
```

Enables/disables returning objects returned as part of the result.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

**Parameters:** on

- if true, objects will be returned; if false,
objects will not be returned.
**See Also:** getReturningObjFlag()

---

#### setReturningObjFlag

public void setReturningObjFlag​(boolean on)

Enables/disables returning objects returned as part of the result.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

If disabled, only the name and class of the object is returned.
If enabled, the object will be returned.

setCountLimit

```java
public void setCountLimit​(long limit)
```

Sets the maximum number of entries to be returned
as a result of the search.

0 indicates no limit: all entries will be returned.

**Parameters:** limit

- The maximum number of entries that will be returned.
**See Also:** getCountLimit()

---

#### setCountLimit

public void setCountLimit​(long limit)

Sets the maximum number of entries to be returned
as a result of the search.

0 indicates no limit: all entries will be returned.

0 indicates no limit: all entries will be returned.

setReturningAttributes

```java
public void setReturningAttributes​(
String
[] attrs)
```

Specifies the attributes that will be returned as part of the search.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

**Parameters:** attrs

- An array of attribute ids identifying the attributes that
will be returned. Can be null.
**See Also:** getReturningAttributes()

---

#### setReturningAttributes

public void setReturningAttributes​(

String

[] attrs)

Specifies the attributes that will be returned as part of the search.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

null indicates that all attributes will be returned.
An empty array indicates no attributes are returned.

---

