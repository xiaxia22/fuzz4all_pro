# Interface Name

**Source:** `java.naming\javax\naming\Name.html`

### Class Description

```java
public interface
Name

extends
Cloneable
,
Serializable
,
Comparable
<
Object
>
```

The

Name

interface represents a generic name -- an ordered
sequence of components. It can be a composite name (names that
span multiple namespaces), or a compound name (names that are
used within individual hierarchical naming systems).

There can be different implementations of

Name

; for example,
composite names, URLs, or namespace-specific compound names.

The components of a name are numbered. The indexes of a name
with N components range from 0 up to, but not including, N. This
range may be written as [0,N).
The most significant component is at index 0.
An empty name has no components.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

**All Superinterfaces:** Cloneable

,

Comparable

<

Object

>

,

Serializable

---

### Field Details

#### static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### Object
clone()

Generates a new copy of this name.
Subsequent changes to the components of this name will not
affect the new copy, and vice versa.

**Returns:**
- a copy of this name

**See Also:**
- Object.clone()

---

#### int compareTo​(
Object
obj)

Compares this name with another name for order.
Returns a negative integer, zero, or a positive integer as this
name is less than, equal to, or greater than the given name.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>

**Parameters:**
- obj

- the non-null object to compare against.

**Returns:**
- a negative integer, zero, or a positive integer as this name
is less than, equal to, or greater than the given name

**Throws:**
- ClassCastException

- if obj is not a

Name

of a
type that may be compared with this name

**See Also:**
- Comparable.compareTo(Object)

---

#### int size()

Returns the number of components in this name.

**Returns:**
- the number of components in this name

---

#### boolean isEmpty()

Determines whether this name is empty.
An empty name is one with zero components.

**Returns:**
- true if this name is empty, false otherwise

---

#### Enumeration
<
String
> getAll()

Retrieves the components of this name as an enumeration
of strings. The effect on the enumeration of updates to
this name is undefined. If the name has zero components,
an empty (non-null) enumeration is returned.

**Returns:**
- an enumeration of the components of this name, each a string

---

#### String
get​(int posn)

Retrieves a component of this name.

**Parameters:**
- posn

- the 0-based index of the component to retrieve.
Must be in the range [0,size()).

**Returns:**
- the component at index posn

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### Name
getPrefix​(int posn)

Creates a name whose components consist of a prefix of the
components of this name. Subsequent changes to
this name will not affect the name that is returned and vice versa.

**Parameters:**
- posn

- the 0-based index of the component at which to stop.
Must be in the range [0,size()].

**Returns:**
- a name consisting of the components at indexes in
the range [0,posn).

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### Name
getSuffix​(int posn)

Creates a name whose components consist of a suffix of the
components in this name. Subsequent changes to
this name do not affect the name that is returned and vice versa.

**Parameters:**
- posn

- the 0-based index of the component at which to start.
Must be in the range [0,size()].

**Returns:**
- a name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty name is returned.

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### boolean startsWith​(
Name
n)

Determines whether this name starts with a specified prefix.
A name

n

is a prefix if it is equal to

getPrefix(n.size())

.

**Parameters:**
- n

- the name to check

**Returns:**
- true if

n

is a prefix of this name, false otherwise

---

#### boolean endsWith​(
Name
n)

Determines whether this name ends with a specified suffix.
A name

n

is a suffix if it is equal to

getSuffix(size()-n.size())

.

**Parameters:**
- n

- the name to check

**Returns:**
- true if

n

is a suffix of this name, false otherwise

---

#### Name
addAll​(
Name
suffix)
throws
InvalidNameException

Adds the components of a name -- in order -- to the end of this name.

**Parameters:**
- suffix

- the components to add

**Returns:**
- the updated name (not a new one)

**Throws:**
- InvalidNameException

- if

suffix

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

---

#### Name
addAll​(int posn,

Name
n)
throws
InvalidNameException

Adds the components of a name -- in order -- at a specified position
within this name.
Components of this name at or after the index of the first new
component are shifted up (away from 0) to accommodate the new
components.

**Parameters:**
- n

- the components to add
- posn

- the index in this name at which to add the new
components. Must be in the range [0,size()].

**Returns:**
- the updated name (not a new one)

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range
- InvalidNameException

- if

n

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

---

#### Name
add​(
String
comp)
throws
InvalidNameException

Adds a single component to the end of this name.

**Parameters:**
- comp

- the component to add

**Returns:**
- the updated name (not a new one)

**Throws:**
- InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

---

#### Name
add​(int posn,

String
comp)
throws
InvalidNameException

Adds a single component at a specified position within this name.
Components of this name at or after the index of the new component
are shifted up by one (away from index 0) to accommodate the new
component.

**Parameters:**
- comp

- the component to add
- posn

- the index at which to add the new component.
Must be in the range [0,size()].

**Returns:**
- the updated name (not a new one)

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range
- InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

---

#### Object
remove​(int posn)
throws
InvalidNameException

Removes a component from this name.
The component of this name at the specified position is removed.
Components with indexes greater than this position
are shifted down (toward index 0) by one.

**Parameters:**
- posn

- the index of the component to remove.
Must be in the range [0,size()).

**Returns:**
- the component removed (a String)

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the specified range
- InvalidNameException

- if deleting the component
would violate the syntax rules of the name

---

### Additional Sections

#### Interface Name

**All Superinterfaces:** Cloneable

,

Comparable

<

Object

>

,

Serializable

**All Known Implementing Classes:** CompositeName

,

CompoundName

,

LdapName

```java
public interface
Name

extends
Cloneable
,
Serializable
,
Comparable
<
Object
>
```

The

Name

interface represents a generic name -- an ordered
sequence of components. It can be a composite name (names that
span multiple namespaces), or a compound name (names that are
used within individual hierarchical naming systems).

There can be different implementations of

Name

; for example,
composite names, URLs, or namespace-specific compound names.

The components of a name are numbered. The indexes of a name
with N components range from 0 up to, but not including, N. This
range may be written as [0,N).
The most significant component is at index 0.
An empty name has no components.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

**Since:** 1.3

public interface

Name

extends

Cloneable

,

Serializable

,

Comparable

<

Object

>

The

Name

interface represents a generic name -- an ordered
sequence of components. It can be a composite name (names that
span multiple namespaces), or a compound name (names that are
used within individual hierarchical naming systems).

There can be different implementations of

Name

; for example,
composite names, URLs, or namespace-specific compound names.

The components of a name are numbered. The indexes of a name
with N components range from 0 up to, but not including, N. This
range may be written as [0,N).
The most significant component is at index 0.
An empty name has no components.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

There can be different implementations of

Name

; for example,
composite names, URLs, or namespace-specific compound names.

The components of a name are numbered. The indexes of a name
with N components range from 0 up to, but not including, N. This
range may be written as [0,N).
The most significant component is at index 0.
An empty name has no components.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

The components of a name are numbered. The indexes of a name
with N components range from 0 up to, but not including, N. This
range may be written as [0,N).
The most significant component is at index 0.
An empty name has no components.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

None of the methods in this interface accept null as a valid
value for a parameter that is a name or a name component.
Likewise, methods that return a name or name component never return null.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

An instance of a

Name

may not be synchronized against
concurrent multithreaded access if that access is not read-only.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Name

add

​(int posn,

String

comp)

Adds a single component at a specified position within this name.

Name

add

​(

String

comp)

Adds a single component to the end of this name.

Name

addAll

​(int posn,

Name

n)

Adds the components of a name -- in order -- at a specified position
within this name.

Name

addAll

​(

Name

suffix)

Adds the components of a name -- in order -- to the end of this name.

Object

clone

()

Generates a new copy of this name.

int

compareTo

​(

Object

obj)

Compares this name with another name for order.

boolean

endsWith

​(

Name

n)

Determines whether this name ends with a specified suffix.

String

get

​(int posn)

Retrieves a component of this name.

Enumeration

<

String

>

getAll

()

Retrieves the components of this name as an enumeration
of strings.

Name

getPrefix

​(int posn)

Creates a name whose components consist of a prefix of the
components of this name.

Name

getSuffix

​(int posn)

Creates a name whose components consist of a suffix of the
components in this name.

boolean

isEmpty

()

Determines whether this name is empty.

Object

remove

​(int posn)

Removes a component from this name.

int

size

()

Returns the number of components in this name.

boolean

startsWith

​(

Name

n)

Determines whether this name starts with a specified prefix.

Field Summary

Fields

Modifier and Type

Field

Description

static long

serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

---

#### Field Summary

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Name

add

​(int posn,

String

comp)

Adds a single component at a specified position within this name.

Name

add

​(

String

comp)

Adds a single component to the end of this name.

Name

addAll

​(int posn,

Name

n)

Adds the components of a name -- in order -- at a specified position
within this name.

Name

addAll

​(

Name

suffix)

Adds the components of a name -- in order -- to the end of this name.

Object

clone

()

Generates a new copy of this name.

int

compareTo

​(

Object

obj)

Compares this name with another name for order.

boolean

endsWith

​(

Name

n)

Determines whether this name ends with a specified suffix.

String

get

​(int posn)

Retrieves a component of this name.

Enumeration

<

String

>

getAll

()

Retrieves the components of this name as an enumeration
of strings.

Name

getPrefix

​(int posn)

Creates a name whose components consist of a prefix of the
components of this name.

Name

getSuffix

​(int posn)

Creates a name whose components consist of a suffix of the
components in this name.

boolean

isEmpty

()

Determines whether this name is empty.

Object

remove

​(int posn)

Removes a component from this name.

int

size

()

Returns the number of components in this name.

boolean

startsWith

​(

Name

n)

Determines whether this name starts with a specified prefix.

---

#### Method Summary

Adds a single component at a specified position within this name.

Adds a single component to the end of this name.

Adds the components of a name -- in order -- at a specified position
within this name.

Adds the components of a name -- in order -- to the end of this name.

Generates a new copy of this name.

Compares this name with another name for order.

Determines whether this name ends with a specified suffix.

Retrieves a component of this name.

Retrieves the components of this name as an enumeration
of strings.

Creates a name whose components consist of a prefix of the
components of this name.

Creates a name whose components consist of a suffix of the
components in this name.

Determines whether this name is empty.

Removes a component from this name.

Returns the number of components in this name.

Determines whether this name starts with a specified prefix.

============ FIELD DETAIL ===========

- Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- clone

```java
Object
clone()
```

Generates a new copy of this name.
Subsequent changes to the components of this name will not
affect the new copy, and vice versa.

**Returns:** a copy of this name
**See Also:** Object.clone()

- compareTo

```java
int compareTo​(
Object
obj)
```

Compares this name with another name for order.
Returns a negative integer, zero, or a positive integer as this
name is less than, equal to, or greater than the given name.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this name
is less than, equal to, or greater than the given name
**Throws:** ClassCastException

- if obj is not a

Name

of a
type that may be compared with this name
**See Also:** Comparable.compareTo(Object)

- size

```java
int size()
```

Returns the number of components in this name.

**Returns:** the number of components in this name

- isEmpty

```java
boolean isEmpty()
```

Determines whether this name is empty.
An empty name is one with zero components.

**Returns:** true if this name is empty, false otherwise

- getAll

```java
Enumeration
<
String
> getAll()
```

Retrieves the components of this name as an enumeration
of strings. The effect on the enumeration of updates to
this name is undefined. If the name has zero components,
an empty (non-null) enumeration is returned.

**Returns:** an enumeration of the components of this name, each a string

- get

```java
String
get​(int posn)
```

Retrieves a component of this name.

**Parameters:** posn

- the 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** the component at index posn
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- getPrefix

```java
Name
getPrefix​(int posn)
```

Creates a name whose components consist of a prefix of the
components of this name. Subsequent changes to
this name will not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- getSuffix

```java
Name
getSuffix​(int posn)
```

Creates a name whose components consist of a suffix of the
components in this name. Subsequent changes to
this name do not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- startsWith

```java
boolean startsWith​(
Name
n)
```

Determines whether this name starts with a specified prefix.
A name

n

is a prefix if it is equal to

getPrefix(n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a prefix of this name, false otherwise

- endsWith

```java
boolean endsWith​(
Name
n)
```

Determines whether this name ends with a specified suffix.
A name

n

is a suffix if it is equal to

getSuffix(size()-n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a suffix of this name, false otherwise

- addAll

```java
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a name -- in order -- to the end of this name.

**Parameters:** suffix

- the components to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if

suffix

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

- addAll

```java
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a name -- in order -- at a specified position
within this name.
Components of this name at or after the index of the first new
component are shifted up (away from 0) to accommodate the new
components.

**Parameters:** n

- the components to add
**Parameters:** posn

- the index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if

n

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

- add

```java
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this name.

**Parameters:** comp

- the component to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

- add

```java
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this name.
Components of this name at or after the index of the new component
are shifted up by one (away from index 0) to accommodate the new
component.

**Parameters:** comp

- the component to add
**Parameters:** posn

- the index at which to add the new component.
Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

- remove

```java
Object
remove​(int posn)
throws
InvalidNameException
```

Removes a component from this name.
The component of this name at the specified position is removed.
Components with indexes greater than this position
are shifted down (toward index 0) by one.

**Parameters:** posn

- the index of the component to remove.
Must be in the range [0,size()).
**Returns:** the component removed (a String)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if deleting the component
would violate the syntax rules of the name

Field Detail

- serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### Field Detail

serialVersionUID

```java
static final long serialVersionUID
```

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

**See Also:** Constant Field Values

---

#### serialVersionUID

static final long serialVersionUID

The class fingerprint that is set to indicate
serialization compatibility with a previous
version of the class.

Method Detail

- clone

```java
Object
clone()
```

Generates a new copy of this name.
Subsequent changes to the components of this name will not
affect the new copy, and vice versa.

**Returns:** a copy of this name
**See Also:** Object.clone()

- compareTo

```java
int compareTo​(
Object
obj)
```

Compares this name with another name for order.
Returns a negative integer, zero, or a positive integer as this
name is less than, equal to, or greater than the given name.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this name
is less than, equal to, or greater than the given name
**Throws:** ClassCastException

- if obj is not a

Name

of a
type that may be compared with this name
**See Also:** Comparable.compareTo(Object)

- size

```java
int size()
```

Returns the number of components in this name.

**Returns:** the number of components in this name

- isEmpty

```java
boolean isEmpty()
```

Determines whether this name is empty.
An empty name is one with zero components.

**Returns:** true if this name is empty, false otherwise

- getAll

```java
Enumeration
<
String
> getAll()
```

Retrieves the components of this name as an enumeration
of strings. The effect on the enumeration of updates to
this name is undefined. If the name has zero components,
an empty (non-null) enumeration is returned.

**Returns:** an enumeration of the components of this name, each a string

- get

```java
String
get​(int posn)
```

Retrieves a component of this name.

**Parameters:** posn

- the 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** the component at index posn
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- getPrefix

```java
Name
getPrefix​(int posn)
```

Creates a name whose components consist of a prefix of the
components of this name. Subsequent changes to
this name will not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- getSuffix

```java
Name
getSuffix​(int posn)
```

Creates a name whose components consist of a suffix of the
components in this name. Subsequent changes to
this name do not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

- startsWith

```java
boolean startsWith​(
Name
n)
```

Determines whether this name starts with a specified prefix.
A name

n

is a prefix if it is equal to

getPrefix(n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a prefix of this name, false otherwise

- endsWith

```java
boolean endsWith​(
Name
n)
```

Determines whether this name ends with a specified suffix.
A name

n

is a suffix if it is equal to

getSuffix(size()-n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a suffix of this name, false otherwise

- addAll

```java
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a name -- in order -- to the end of this name.

**Parameters:** suffix

- the components to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if

suffix

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

- addAll

```java
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a name -- in order -- at a specified position
within this name.
Components of this name at or after the index of the first new
component are shifted up (away from 0) to accommodate the new
components.

**Parameters:** n

- the components to add
**Parameters:** posn

- the index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if

n

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

- add

```java
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this name.

**Parameters:** comp

- the component to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

- add

```java
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this name.
Components of this name at or after the index of the new component
are shifted up by one (away from index 0) to accommodate the new
component.

**Parameters:** comp

- the component to add
**Parameters:** posn

- the index at which to add the new component.
Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

- remove

```java
Object
remove​(int posn)
throws
InvalidNameException
```

Removes a component from this name.
The component of this name at the specified position is removed.
Components with indexes greater than this position
are shifted down (toward index 0) by one.

**Parameters:** posn

- the index of the component to remove.
Must be in the range [0,size()).
**Returns:** the component removed (a String)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if deleting the component
would violate the syntax rules of the name

---

#### Method Detail

clone

```java
Object
clone()
```

Generates a new copy of this name.
Subsequent changes to the components of this name will not
affect the new copy, and vice versa.

**Returns:** a copy of this name
**See Also:** Object.clone()

---

#### clone

Object

clone()

Generates a new copy of this name.
Subsequent changes to the components of this name will not
affect the new copy, and vice versa.

compareTo

```java
int compareTo​(
Object
obj)
```

Compares this name with another name for order.
Returns a negative integer, zero, or a positive integer as this
name is less than, equal to, or greater than the given name.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Parameters:** obj

- the non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this name
is less than, equal to, or greater than the given name
**Throws:** ClassCastException

- if obj is not a

Name

of a
type that may be compared with this name
**See Also:** Comparable.compareTo(Object)

---

#### compareTo

int compareTo​(

Object

obj)

Compares this name with another name for order.
Returns a negative integer, zero, or a positive integer as this
name is less than, equal to, or greater than the given name.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

As with

Object.equals()

, the notion of ordering for names
depends on the class that implements this interface.
For example, the ordering may be
based on lexicographical ordering of the name components.
Specific attributes of the name, such as how it treats case,
may affect the ordering. In general, two names of different
classes may not be compared.

size

```java
int size()
```

Returns the number of components in this name.

**Returns:** the number of components in this name

---

#### size

int size()

Returns the number of components in this name.

isEmpty

```java
boolean isEmpty()
```

Determines whether this name is empty.
An empty name is one with zero components.

**Returns:** true if this name is empty, false otherwise

---

#### isEmpty

boolean isEmpty()

Determines whether this name is empty.
An empty name is one with zero components.

getAll

```java
Enumeration
<
String
> getAll()
```

Retrieves the components of this name as an enumeration
of strings. The effect on the enumeration of updates to
this name is undefined. If the name has zero components,
an empty (non-null) enumeration is returned.

**Returns:** an enumeration of the components of this name, each a string

---

#### getAll

Enumeration

<

String

> getAll()

Retrieves the components of this name as an enumeration
of strings. The effect on the enumeration of updates to
this name is undefined. If the name has zero components,
an empty (non-null) enumeration is returned.

get

```java
String
get​(int posn)
```

Retrieves a component of this name.

**Parameters:** posn

- the 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** the component at index posn
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### get

String

get​(int posn)

Retrieves a component of this name.

getPrefix

```java
Name
getPrefix​(int posn)
```

Creates a name whose components consist of a prefix of the
components of this name. Subsequent changes to
this name will not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### getPrefix

Name

getPrefix​(int posn)

Creates a name whose components consist of a prefix of the
components of this name. Subsequent changes to
this name will not affect the name that is returned and vice versa.

getSuffix

```java
Name
getSuffix​(int posn)
```

Creates a name whose components consist of a suffix of the
components in this name. Subsequent changes to
this name do not affect the name that is returned and vice versa.

**Parameters:** posn

- the 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** a name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range

---

#### getSuffix

Name

getSuffix​(int posn)

Creates a name whose components consist of a suffix of the
components in this name. Subsequent changes to
this name do not affect the name that is returned and vice versa.

startsWith

```java
boolean startsWith​(
Name
n)
```

Determines whether this name starts with a specified prefix.
A name

n

is a prefix if it is equal to

getPrefix(n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a prefix of this name, false otherwise

---

#### startsWith

boolean startsWith​(

Name

n)

Determines whether this name starts with a specified prefix.
A name

n

is a prefix if it is equal to

getPrefix(n.size())

.

endsWith

```java
boolean endsWith​(
Name
n)
```

Determines whether this name ends with a specified suffix.
A name

n

is a suffix if it is equal to

getSuffix(size()-n.size())

.

**Parameters:** n

- the name to check
**Returns:** true if

n

is a suffix of this name, false otherwise

---

#### endsWith

boolean endsWith​(

Name

n)

Determines whether this name ends with a specified suffix.
A name

n

is a suffix if it is equal to

getSuffix(size()-n.size())

.

addAll

```java
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a name -- in order -- to the end of this name.

**Parameters:** suffix

- the components to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if

suffix

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

---

#### addAll

Name

addAll​(

Name

suffix)
throws

InvalidNameException

Adds the components of a name -- in order -- to the end of this name.

addAll

```java
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a name -- in order -- at a specified position
within this name.
Components of this name at or after the index of the first new
component are shifted up (away from 0) to accommodate the new
components.

**Parameters:** n

- the components to add
**Parameters:** posn

- the index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if

n

is not a valid name,
or if the addition of the components would violate the syntax
rules of this name

---

#### addAll

Name

addAll​(int posn,

Name

n)
throws

InvalidNameException

Adds the components of a name -- in order -- at a specified position
within this name.
Components of this name at or after the index of the first new
component are shifted up (away from 0) to accommodate the new
components.

add

```java
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this name.

**Parameters:** comp

- the component to add
**Returns:** the updated name (not a new one)
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

---

#### add

Name

add​(

String

comp)
throws

InvalidNameException

Adds a single component to the end of this name.

add

```java
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this name.
Components of this name at or after the index of the new component
are shifted up by one (away from index 0) to accommodate the new
component.

**Parameters:** comp

- the component to add
**Parameters:** posn

- the index at which to add the new component.
Must be in the range [0,size()].
**Returns:** the updated name (not a new one)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if adding

comp

would violate
the syntax rules of this name

---

#### add

Name

add​(int posn,

String

comp)
throws

InvalidNameException

Adds a single component at a specified position within this name.
Components of this name at or after the index of the new component
are shifted up by one (away from index 0) to accommodate the new
component.

remove

```java
Object
remove​(int posn)
throws
InvalidNameException
```

Removes a component from this name.
The component of this name at the specified position is removed.
Components with indexes greater than this position
are shifted down (toward index 0) by one.

**Parameters:** posn

- the index of the component to remove.
Must be in the range [0,size()).
**Returns:** the component removed (a String)
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the specified range
**Throws:** InvalidNameException

- if deleting the component
would violate the syntax rules of the name

---

#### remove

Object

remove​(int posn)
throws

InvalidNameException

Removes a component from this name.
The component of this name at the specified position is removed.
Components with indexes greater than this position
are shifted down (toward index 0) by one.

---

