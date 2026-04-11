# Class CompoundName

**Source:** `java.naming\javax\naming\CompoundName.html`

### Class Description

```java
public class
CompoundName

extends
Object

implements
Name
```

This class represents a compound name -- a name from
a hierarchical name space.
Each component in a compound name is an atomic name.

The components of a compound name are numbered. The indexes of a
compound name with N components range from 0 up to, but not including, N.
This range may be written as [0,N).
The most significant component is at index 0.
An empty compound name has no components.

Compound Name Syntax

The syntax of a compound name is specified using a set of properties:

These properties are interpreted according to the following rules:

- In a string without quotes or escapes, any instance of the
separator delimits two atomic names. Each atomic name is referred
to as a

component

.

A separator, quote or escape is escaped if preceded immediately
(on the left) by the escape.

If there are two sets of quotes, a specific begin-quote must be matched
by its corresponding end-quote.

A non-escaped begin-quote which precedes a component must be
matched by a non-escaped end-quote at the end of the component.
A component thus quoted is referred to as a

quoted component

. It is parsed by
removing the being- and end- quotes, and by treating the intervening
characters as ordinary characters unless one of the rules involving
quoted components listed below applies.

Quotes embedded in non-quoted components are treated as ordinary strings
and need not be matched.

A separator that is escaped or appears between non-escaped
quotes is treated as an ordinary string and not a separator.

An escape string within a quoted component acts as an escape only when
followed by the corresponding end-quote string.
This can be used to embed an escaped quote within a quoted component.

An escaped escape string is not treated as an escape string.

An escape string that does not precede a meta string (quotes or separator)
and is not at the end of a component is treated as an ordinary string.

A leading separator (the compound name string begins with
a separator) denotes a leading empty atomic component (consisting
of an empty string).
A trailing separator (the compound name string ends with
a separator) denotes a trailing empty atomic component.
Adjacent separators denote an empty atomic component.

The string form of the compound name follows the syntax described above.
When the components of the compound name are turned into their
string representation, the reserved syntax rules described above are
applied (e.g. embedded separators are escaped or quoted)
so that when the same string is parsed, it will yield the same components
of the original compound name.

Multithreaded Access

A

CompoundName

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

CompoundName

should lock the object.

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Comparable

<

Object

>

,

Name

---

### Field Details

#### protected transient
Properties
mySyntax

Syntax properties for this compound name.
This field is initialized by the constructors and cannot be null.
It should be treated as a read-only variable by subclasses.
Any necessary changes to mySyntax should be made within constructors
and not after the compound name has been instantiated.

---

### Constructor Details

#### protected CompoundName​(
Enumeration
<
String
> comps,

Properties
syntax)

Constructs a new compound name instance using the components
specified in comps and syntax. This protected method is intended
to be used by subclasses of CompoundName when they override
methods such as clone(), getPrefix(), getSuffix().

**Parameters:**
- comps

- A non-null enumeration of the components to add.
Each element of the enumeration is of class String.
The enumeration will be consumed to extract its
elements.
- syntax

- A non-null properties that specify the syntax of
this compound name. See class description for
contents of properties.

---

#### public CompoundName​(
String
n,

Properties
syntax)
throws
InvalidNameException

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

**Parameters:**
- n

- The non-null string to parse.
- syntax

- A non-null list of properties that specify the syntax of
this compound name. See class description for
contents of properties.

**Throws:**
- InvalidNameException

- If 'n' violates the syntax specified
by

syntax

.

---

### Method Details

#### public
String
toString()

Generates the string representation of this compound name, using
the syntax rules of the compound name. The syntax rules
are described in the class description.
An empty component is represented by an empty string.

The string representation thus generated can be passed to
the CompoundName constructor with the same syntax properties
to create a new equivalent compound name.

**Overrides:**
- toString

in class

Object

**Returns:**
- A non-null string representation of this compound name.

---

#### public boolean equals​(
Object
obj)

Determines whether obj is syntactically equal to this compound name.
If obj is null or not a CompoundName, false is returned.
Two compound names are equal if each component in one is "equal"
to the corresponding component in the other.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The possibly null object to compare against.

**Returns:**
- true if obj is equal to this compound name, false otherwise.

**See Also:**
- compareTo(java.lang.Object obj)

---

#### public int hashCode()

Computes the hash code of this compound name.
The hash code is the sum of the hash codes of the "canonicalized"
forms of individual components of this compound name.
Each component is "canonicalized" according to the
compound name's syntax before its hash code is computed.
For a case-insensitive name, for example, the uppercased form of
a name has the same hash code as its lowercased equivalent.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- An int representing the hash code of this name.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public
Object
clone()

Creates a copy of this compound name.
Changes to the components of this compound name won't
affect the new copy and vice versa.
The clone and this compound name share the same syntax.

**Specified by:**
- clone

in interface

Name

**Overrides:**
- clone

in class

Object

**Returns:**
- A non-null copy of this compound name.

**See Also:**
- Cloneable

---

#### public int compareTo​(
Object
obj)

Compares this CompoundName with the specified Object for order.
Returns a
negative integer, zero, or a positive integer as this Name is less
than, equal to, or greater than the given Object.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

**Specified by:**
- compareTo

in interface

Comparable

<

Object

>
- compareTo

in interface

Name

**Parameters:**
- obj

- The non-null object to compare against.

**Returns:**
- a negative integer, zero, or a positive integer as this Name
is less than, equal to, or greater than the given Object.

**Throws:**
- ClassCastException

- if obj is not a CompoundName.

**See Also:**
- equals(java.lang.Object)

---

#### public int size()

Retrieves the number of components in this compound name.

**Specified by:**
- size

in interface

Name

**Returns:**
- The nonnegative number of components in this compound name.

---

#### public boolean isEmpty()

Determines whether this compound name is empty.
A compound name is empty if it has zero components.

**Specified by:**
- isEmpty

in interface

Name

**Returns:**
- true if this compound name is empty, false otherwise.

---

#### public
Enumeration
<
String
> getAll()

Retrieves the components of this compound name as an enumeration
of strings.
The effects of updates to this compound name on this enumeration
is undefined.

**Specified by:**
- getAll

in interface

Name

**Returns:**
- A non-null enumeration of the components of this
compound name. Each element of the enumeration is of class String.

---

#### public
String
get​(int posn)

Retrieves a component of this compound name.

**Specified by:**
- get

in interface

Name

**Parameters:**
- posn

- The 0-based index of the component to retrieve.
Must be in the range [0,size()).

**Returns:**
- The component at index posn.

**Throws:**
- ArrayIndexOutOfBoundsException

- if posn is outside the
specified range.

---

#### public
Name
getPrefix​(int posn)

Creates a compound name whose components consist of a prefix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned and
vice versa.

**Specified by:**
- getPrefix

in interface

Name

**Parameters:**
- posn

- The 0-based index of the component at which to stop.
Must be in the range [0,size()].

**Returns:**
- A compound name consisting of the components at indexes in
the range [0,posn).

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

---

#### public
Name
getSuffix​(int posn)

Creates a compound name whose components consist of a suffix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned.

**Specified by:**
- getSuffix

in interface

Name

**Parameters:**
- posn

- The 0-based index of the component at which to start.
Must be in the range [0,size()].

**Returns:**
- A compound name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty compound name is returned.

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

---

#### public boolean startsWith​(
Name
n)

Determines whether a compound name is a prefix of this compound name.
A compound name 'n' is a prefix if it is equal to
getPrefix(n.size())--in other words, this compound name
starts with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:**
- startsWith

in interface

Name

**Parameters:**
- n

- The possibly null compound name to check.

**Returns:**
- true if n is a CompoundName and
is a prefix of this compound name, false otherwise.

---

#### public boolean endsWith​(
Name
n)

Determines whether a compound name is a suffix of this compound name.
A compound name 'n' is a suffix if it is equal to
getSuffix(size()-n.size())--in other words, this
compound name ends with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:**
- endsWith

in interface

Name

**Parameters:**
- n

- The possibly null compound name to check.

**Returns:**
- true if n is a CompoundName and
is a suffix of this compound name, false otherwise.

---

#### public
Name
addAll​(
Name
suffix)
throws
InvalidNameException

Adds the components of a compound name -- in order -- to the end of
this compound name.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:**
- addAll

in interface

Name

**Parameters:**
- suffix

- The non-null components to add.

**Returns:**
- The updated CompoundName, not a new one. Cannot be null.

**Throws:**
- InvalidNameException

- If suffix is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

---

#### public
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException

Adds the components of a compound name -- in order -- at a specified
position within this compound name.
Components of this compound name at or after the index of the first
new component are shifted up (away from index 0)
to accommodate the new components.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:**
- addAll

in interface

Name

**Parameters:**
- n

- The non-null components to add.
- posn

- The index in this name at which to add the new
components. Must be in the range [0,size()].

**Returns:**
- The updated CompoundName, not a new one. Cannot be null.

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
- InvalidNameException

- If n is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

---

#### public
Name
add​(
String
comp)
throws
InvalidNameException

Adds a single component to the end of this compound name.

**Specified by:**
- add

in interface

Name

**Parameters:**
- comp

- The non-null component to add.

**Returns:**
- The updated CompoundName, not a new one. Cannot be null.

**Throws:**
- InvalidNameException

- If adding comp at end of the name
would violate the compound name's syntax.

---

#### public
Name
add​(int posn,

String
comp)
throws
InvalidNameException

Adds a single component at a specified position within this
compound name.
Components of this compound name at or after the index of the new
component are shifted up by one (away from index 0)
to accommodate the new component.

**Specified by:**
- add

in interface

Name

**Parameters:**
- comp

- The non-null component to add.
- posn

- The index at which to add the new component.
Must be in the range [0,size()].

**Returns:**
- The updated CompoundName, not a new one. Cannot be null.

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
- InvalidNameException

- If adding comp at the specified position
would violate the compound name's syntax.

---

#### public
Object
remove​(int posn)
throws
InvalidNameException

Deletes a component from this compound name.
The component of this compound name at position 'posn' is removed,
and components at indices greater than 'posn'
are shifted down (towards index 0) by one.

**Specified by:**
- remove

in interface

Name

**Parameters:**
- posn

- The index of the component to delete.
Must be in the range [0,size()).

**Returns:**
- The component removed (a String).

**Throws:**
- ArrayIndexOutOfBoundsException

- If posn is outside the specified range (includes case where
compound name is empty).
- InvalidNameException

- If deleting the component
would violate the compound name's syntax.

---

### Additional Sections

#### Class CompoundName

java.lang.Object

- javax.naming.CompoundName

javax.naming.CompoundName

**All Implemented Interfaces:** Serializable

,

Cloneable

,

Comparable

<

Object

>

,

Name

```java
public class
CompoundName

extends
Object

implements
Name
```

This class represents a compound name -- a name from
a hierarchical name space.
Each component in a compound name is an atomic name.

The components of a compound name are numbered. The indexes of a
compound name with N components range from 0 up to, but not including, N.
This range may be written as [0,N).
The most significant component is at index 0.
An empty compound name has no components.

Compound Name Syntax

The syntax of a compound name is specified using a set of properties:

These properties are interpreted according to the following rules:

- In a string without quotes or escapes, any instance of the
separator delimits two atomic names. Each atomic name is referred
to as a

component

.

A separator, quote or escape is escaped if preceded immediately
(on the left) by the escape.

If there are two sets of quotes, a specific begin-quote must be matched
by its corresponding end-quote.

A non-escaped begin-quote which precedes a component must be
matched by a non-escaped end-quote at the end of the component.
A component thus quoted is referred to as a

quoted component

. It is parsed by
removing the being- and end- quotes, and by treating the intervening
characters as ordinary characters unless one of the rules involving
quoted components listed below applies.

Quotes embedded in non-quoted components are treated as ordinary strings
and need not be matched.

A separator that is escaped or appears between non-escaped
quotes is treated as an ordinary string and not a separator.

An escape string within a quoted component acts as an escape only when
followed by the corresponding end-quote string.
This can be used to embed an escaped quote within a quoted component.

An escaped escape string is not treated as an escape string.

An escape string that does not precede a meta string (quotes or separator)
and is not at the end of a component is treated as an ordinary string.

A leading separator (the compound name string begins with
a separator) denotes a leading empty atomic component (consisting
of an empty string).
A trailing separator (the compound name string ends with
a separator) denotes a trailing empty atomic component.
Adjacent separators denote an empty atomic component.

The string form of the compound name follows the syntax described above.
When the components of the compound name are turned into their
string representation, the reserved syntax rules described above are
applied (e.g. embedded separators are escaped or quoted)
so that when the same string is parsed, it will yield the same components
of the original compound name.

Multithreaded Access

A

CompoundName

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

CompoundName

should lock the object.

**Since:** 1.3
**See Also:** Serialized Form

public class

CompoundName

extends

Object

implements

Name

This class represents a compound name -- a name from
a hierarchical name space.
Each component in a compound name is an atomic name.

The components of a compound name are numbered. The indexes of a
compound name with N components range from 0 up to, but not including, N.
This range may be written as [0,N).
The most significant component is at index 0.
An empty compound name has no components.

Compound Name Syntax

The syntax of a compound name is specified using a set of properties:

These properties are interpreted according to the following rules:

- In a string without quotes or escapes, any instance of the
separator delimits two atomic names. Each atomic name is referred
to as a

component

.

A separator, quote or escape is escaped if preceded immediately
(on the left) by the escape.

If there are two sets of quotes, a specific begin-quote must be matched
by its corresponding end-quote.

A non-escaped begin-quote which precedes a component must be
matched by a non-escaped end-quote at the end of the component.
A component thus quoted is referred to as a

quoted component

. It is parsed by
removing the being- and end- quotes, and by treating the intervening
characters as ordinary characters unless one of the rules involving
quoted components listed below applies.

Quotes embedded in non-quoted components are treated as ordinary strings
and need not be matched.

A separator that is escaped or appears between non-escaped
quotes is treated as an ordinary string and not a separator.

An escape string within a quoted component acts as an escape only when
followed by the corresponding end-quote string.
This can be used to embed an escaped quote within a quoted component.

An escaped escape string is not treated as an escape string.

An escape string that does not precede a meta string (quotes or separator)
and is not at the end of a component is treated as an ordinary string.

A leading separator (the compound name string begins with
a separator) denotes a leading empty atomic component (consisting
of an empty string).
A trailing separator (the compound name string ends with
a separator) denotes a trailing empty atomic component.
Adjacent separators denote an empty atomic component.

The string form of the compound name follows the syntax described above.
When the components of the compound name are turned into their
string representation, the reserved syntax rules described above are
applied (e.g. embedded separators are escaped or quoted)
so that when the same string is parsed, it will yield the same components
of the original compound name.

Multithreaded Access

A

CompoundName

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

CompoundName

should lock the object.

The components of a compound name are numbered. The indexes of a
compound name with N components range from 0 up to, but not including, N.
This range may be written as [0,N).
The most significant component is at index 0.
An empty compound name has no components.

Compound Name Syntax

The syntax of a compound name is specified using a set of properties:

These properties are interpreted according to the following rules:

- In a string without quotes or escapes, any instance of the
separator delimits two atomic names. Each atomic name is referred
to as a

component

.

A separator, quote or escape is escaped if preceded immediately
(on the left) by the escape.

If there are two sets of quotes, a specific begin-quote must be matched
by its corresponding end-quote.

A non-escaped begin-quote which precedes a component must be
matched by a non-escaped end-quote at the end of the component.
A component thus quoted is referred to as a

quoted component

. It is parsed by
removing the being- and end- quotes, and by treating the intervening
characters as ordinary characters unless one of the rules involving
quoted components listed below applies.

Quotes embedded in non-quoted components are treated as ordinary strings
and need not be matched.

A separator that is escaped or appears between non-escaped
quotes is treated as an ordinary string and not a separator.

An escape string within a quoted component acts as an escape only when
followed by the corresponding end-quote string.
This can be used to embed an escaped quote within a quoted component.

An escaped escape string is not treated as an escape string.

An escape string that does not precede a meta string (quotes or separator)
and is not at the end of a component is treated as an ordinary string.

A leading separator (the compound name string begins with
a separator) denotes a leading empty atomic component (consisting
of an empty string).
A trailing separator (the compound name string ends with
a separator) denotes a trailing empty atomic component.
Adjacent separators denote an empty atomic component.

The string form of the compound name follows the syntax described above.
When the components of the compound name are turned into their
string representation, the reserved syntax rules described above are
applied (e.g. embedded separators are escaped or quoted)
so that when the same string is parsed, it will yield the same components
of the original compound name.

Multithreaded Access

A

CompoundName

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

CompoundName

should lock the object.

---

#### Compound Name Syntax

In a string without quotes or escapes, any instance of the
separator delimits two atomic names. Each atomic name is referred
to as a

component

.

A separator, quote or escape is escaped if preceded immediately
(on the left) by the escape.

If there are two sets of quotes, a specific begin-quote must be matched
by its corresponding end-quote.

A non-escaped begin-quote which precedes a component must be
matched by a non-escaped end-quote at the end of the component.
A component thus quoted is referred to as a

quoted component

. It is parsed by
removing the being- and end- quotes, and by treating the intervening
characters as ordinary characters unless one of the rules involving
quoted components listed below applies.

Quotes embedded in non-quoted components are treated as ordinary strings
and need not be matched.

A separator that is escaped or appears between non-escaped
quotes is treated as an ordinary string and not a separator.

An escape string within a quoted component acts as an escape only when
followed by the corresponding end-quote string.
This can be used to embed an escaped quote within a quoted component.

An escaped escape string is not treated as an escape string.

An escape string that does not precede a meta string (quotes or separator)
and is not at the end of a component is treated as an ordinary string.

A leading separator (the compound name string begins with
a separator) denotes a leading empty atomic component (consisting
of an empty string).
A trailing separator (the compound name string ends with
a separator) denotes a trailing empty atomic component.
Adjacent separators denote an empty atomic component.

The string form of the compound name follows the syntax described above.
When the components of the compound name are turned into their
string representation, the reserved syntax rules described above are
applied (e.g. embedded separators are escaped or quoted)
so that when the same string is parsed, it will yield the same components
of the original compound name.

Multithreaded Access

A

CompoundName

instance is not synchronized against concurrent
multithreaded access. Multiple threads trying to access and modify a

CompoundName

should lock the object.

---

#### Multithreaded Access

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Properties

mySyntax

Syntax properties for this compound name.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

CompoundName

​(

String

n,

Properties

syntax)

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

protected

CompoundName

​(

Enumeration

<

String

> comps,

Properties

syntax)

Constructs a new compound name instance using the components
specified in comps and syntax.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Name

add

​(int posn,

String

comp)

Adds a single component at a specified position within this
compound name.

Name

add

​(

String

comp)

Adds a single component to the end of this compound name.

Name

addAll

​(int posn,

Name

n)

Adds the components of a compound name -- in order -- at a specified
position within this compound name.

Name

addAll

​(

Name

suffix)

Adds the components of a compound name -- in order -- to the end of
this compound name.

Object

clone

()

Creates a copy of this compound name.

int

compareTo

​(

Object

obj)

Compares this CompoundName with the specified Object for order.

boolean

endsWith

​(

Name

n)

Determines whether a compound name is a suffix of this compound name.

boolean

equals

​(

Object

obj)

Determines whether obj is syntactically equal to this compound name.

String

get

​(int posn)

Retrieves a component of this compound name.

Enumeration

<

String

>

getAll

()

Retrieves the components of this compound name as an enumeration
of strings.

Name

getPrefix

​(int posn)

Creates a compound name whose components consist of a prefix of the
components in this compound name.

Name

getSuffix

​(int posn)

Creates a compound name whose components consist of a suffix of the
components in this compound name.

int

hashCode

()

Computes the hash code of this compound name.

boolean

isEmpty

()

Determines whether this compound name is empty.

Object

remove

​(int posn)

Deletes a component from this compound name.

int

size

()

Retrieves the number of components in this compound name.

boolean

startsWith

​(

Name

n)

Determines whether a compound name is a prefix of this compound name.

String

toString

()

Generates the string representation of this compound name, using
the syntax rules of the compound name.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

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

protected

Properties

mySyntax

Syntax properties for this compound name.

---

#### Field Summary

Syntax properties for this compound name.

Constructor Summary

Constructors

Modifier

Constructor

Description

CompoundName

​(

String

n,

Properties

syntax)

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

protected

CompoundName

​(

Enumeration

<

String

> comps,

Properties

syntax)

Constructs a new compound name instance using the components
specified in comps and syntax.

---

#### Constructor Summary

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

Constructs a new compound name instance using the components
specified in comps and syntax.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Name

add

​(int posn,

String

comp)

Adds a single component at a specified position within this
compound name.

Name

add

​(

String

comp)

Adds a single component to the end of this compound name.

Name

addAll

​(int posn,

Name

n)

Adds the components of a compound name -- in order -- at a specified
position within this compound name.

Name

addAll

​(

Name

suffix)

Adds the components of a compound name -- in order -- to the end of
this compound name.

Object

clone

()

Creates a copy of this compound name.

int

compareTo

​(

Object

obj)

Compares this CompoundName with the specified Object for order.

boolean

endsWith

​(

Name

n)

Determines whether a compound name is a suffix of this compound name.

boolean

equals

​(

Object

obj)

Determines whether obj is syntactically equal to this compound name.

String

get

​(int posn)

Retrieves a component of this compound name.

Enumeration

<

String

>

getAll

()

Retrieves the components of this compound name as an enumeration
of strings.

Name

getPrefix

​(int posn)

Creates a compound name whose components consist of a prefix of the
components in this compound name.

Name

getSuffix

​(int posn)

Creates a compound name whose components consist of a suffix of the
components in this compound name.

int

hashCode

()

Computes the hash code of this compound name.

boolean

isEmpty

()

Determines whether this compound name is empty.

Object

remove

​(int posn)

Deletes a component from this compound name.

int

size

()

Retrieves the number of components in this compound name.

boolean

startsWith

​(

Name

n)

Determines whether a compound name is a prefix of this compound name.

String

toString

()

Generates the string representation of this compound name, using
the syntax rules of the compound name.

- Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Adds a single component at a specified position within this
compound name.

Adds a single component to the end of this compound name.

Adds the components of a compound name -- in order -- at a specified
position within this compound name.

Adds the components of a compound name -- in order -- to the end of
this compound name.

Creates a copy of this compound name.

Compares this CompoundName with the specified Object for order.

Determines whether a compound name is a suffix of this compound name.

Determines whether obj is syntactically equal to this compound name.

Retrieves a component of this compound name.

Retrieves the components of this compound name as an enumeration
of strings.

Creates a compound name whose components consist of a prefix of the
components in this compound name.

Creates a compound name whose components consist of a suffix of the
components in this compound name.

Computes the hash code of this compound name.

Determines whether this compound name is empty.

Deletes a component from this compound name.

Retrieves the number of components in this compound name.

Determines whether a compound name is a prefix of this compound name.

Generates the string representation of this compound name, using
the syntax rules of the compound name.

Methods declared in class java.lang.

Object

finalize

,

getClass

,

notify

,

notifyAll

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

- mySyntax

```java
protected transient
Properties
mySyntax
```

Syntax properties for this compound name.
This field is initialized by the constructors and cannot be null.
It should be treated as a read-only variable by subclasses.
Any necessary changes to mySyntax should be made within constructors
and not after the compound name has been instantiated.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CompoundName

```java
protected CompoundName​(
Enumeration
<
String
> comps,

Properties
syntax)
```

Constructs a new compound name instance using the components
specified in comps and syntax. This protected method is intended
to be used by subclasses of CompoundName when they override
methods such as clone(), getPrefix(), getSuffix().

**Parameters:** comps

- A non-null enumeration of the components to add.
Each element of the enumeration is of class String.
The enumeration will be consumed to extract its
elements.
**Parameters:** syntax

- A non-null properties that specify the syntax of
this compound name. See class description for
contents of properties.

- CompoundName

```java
public CompoundName​(
String
n,

Properties
syntax)
throws
InvalidNameException
```

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

**Parameters:** n

- The non-null string to parse.
**Parameters:** syntax

- A non-null list of properties that specify the syntax of
this compound name. See class description for
contents of properties.
**Throws:** InvalidNameException

- If 'n' violates the syntax specified
by

syntax

.

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Generates the string representation of this compound name, using
the syntax rules of the compound name. The syntax rules
are described in the class description.
An empty component is represented by an empty string.

The string representation thus generated can be passed to
the CompoundName constructor with the same syntax properties
to create a new equivalent compound name.

**Overrides:** toString

in class

Object
**Returns:** A non-null string representation of this compound name.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is syntactically equal to this compound name.
If obj is null or not a CompoundName, false is returned.
Two compound names are equal if each component in one is "equal"
to the corresponding component in the other.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to compare against.
**Returns:** true if obj is equal to this compound name, false otherwise.
**See Also:** compareTo(java.lang.Object obj)

- hashCode

```java
public int hashCode()
```

Computes the hash code of this compound name.
The hash code is the sum of the hash codes of the "canonicalized"
forms of individual components of this compound name.
Each component is "canonicalized" according to the
compound name's syntax before its hash code is computed.
For a case-insensitive name, for example, the uppercased form of
a name has the same hash code as its lowercased equivalent.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Creates a copy of this compound name.
Changes to the components of this compound name won't
affect the new copy and vice versa.
The clone and this compound name share the same syntax.

**Specified by:** clone

in interface

Name
**Overrides:** clone

in class

Object
**Returns:** A non-null copy of this compound name.
**See Also:** Cloneable

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this CompoundName with the specified Object for order.
Returns a
negative integer, zero, or a positive integer as this Name is less
than, equal to, or greater than the given Object.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Specified by:** compareTo

in interface

Name
**Parameters:** obj

- The non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this Name
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is not a CompoundName.
**See Also:** equals(java.lang.Object)

- size

```java
public int size()
```

Retrieves the number of components in this compound name.

**Specified by:** size

in interface

Name
**Returns:** The nonnegative number of components in this compound name.

- isEmpty

```java
public boolean isEmpty()
```

Determines whether this compound name is empty.
A compound name is empty if it has zero components.

**Specified by:** isEmpty

in interface

Name
**Returns:** true if this compound name is empty, false otherwise.

- getAll

```java
public
Enumeration
<
String
> getAll()
```

Retrieves the components of this compound name as an enumeration
of strings.
The effects of updates to this compound name on this enumeration
is undefined.

**Specified by:** getAll

in interface

Name
**Returns:** A non-null enumeration of the components of this
compound name. Each element of the enumeration is of class String.

- get

```java
public
String
get​(int posn)
```

Retrieves a component of this compound name.

**Specified by:** get

in interface

Name
**Parameters:** posn

- The 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** The component at index posn.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the
specified range.

- getPrefix

```java
public
Name
getPrefix​(int posn)
```

Creates a compound name whose components consist of a prefix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned and
vice versa.

**Specified by:** getPrefix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

- getSuffix

```java
public
Name
getSuffix​(int posn)
```

Creates a compound name whose components consist of a suffix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned.

**Specified by:** getSuffix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty compound name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

- startsWith

```java
public boolean startsWith​(
Name
n)
```

Determines whether a compound name is a prefix of this compound name.
A compound name 'n' is a prefix if it is equal to
getPrefix(n.size())--in other words, this compound name
starts with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** startsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a prefix of this compound name, false otherwise.

- endsWith

```java
public boolean endsWith​(
Name
n)
```

Determines whether a compound name is a suffix of this compound name.
A compound name 'n' is a suffix if it is equal to
getSuffix(size()-n.size())--in other words, this
compound name ends with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** endsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a suffix of this compound name, false otherwise.

- addAll

```java
public
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- to the end of
this compound name.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** suffix

- The non-null components to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If suffix is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

- addAll

```java
public
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- at a specified
position within this compound name.
Components of this compound name at or after the index of the first
new component are shifted up (away from index 0)
to accommodate the new components.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** n

- The non-null components to add.
**Parameters:** posn

- The index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If n is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

- add

```java
public
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this compound name.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If adding comp at end of the name
would violate the compound name's syntax.

- add

```java
public
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this
compound name.
Components of this compound name at or after the index of the new
component are shifted up by one (away from index 0)
to accommodate the new component.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Parameters:** posn

- The index at which to add the new component.
Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If adding comp at the specified position
would violate the compound name's syntax.

- remove

```java
public
Object
remove​(int posn)
throws
InvalidNameException
```

Deletes a component from this compound name.
The component of this compound name at position 'posn' is removed,
and components at indices greater than 'posn'
are shifted down (towards index 0) by one.

**Specified by:** remove

in interface

Name
**Parameters:** posn

- The index of the component to delete.
Must be in the range [0,size()).
**Returns:** The component removed (a String).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range (includes case where
compound name is empty).
**Throws:** InvalidNameException

- If deleting the component
would violate the compound name's syntax.

Field Detail

- mySyntax

```java
protected transient
Properties
mySyntax
```

Syntax properties for this compound name.
This field is initialized by the constructors and cannot be null.
It should be treated as a read-only variable by subclasses.
Any necessary changes to mySyntax should be made within constructors
and not after the compound name has been instantiated.

---

#### Field Detail

mySyntax

```java
protected transient
Properties
mySyntax
```

Syntax properties for this compound name.
This field is initialized by the constructors and cannot be null.
It should be treated as a read-only variable by subclasses.
Any necessary changes to mySyntax should be made within constructors
and not after the compound name has been instantiated.

---

#### mySyntax

protected transient

Properties

mySyntax

Syntax properties for this compound name.
This field is initialized by the constructors and cannot be null.
It should be treated as a read-only variable by subclasses.
Any necessary changes to mySyntax should be made within constructors
and not after the compound name has been instantiated.

Constructor Detail

- CompoundName

```java
protected CompoundName​(
Enumeration
<
String
> comps,

Properties
syntax)
```

Constructs a new compound name instance using the components
specified in comps and syntax. This protected method is intended
to be used by subclasses of CompoundName when they override
methods such as clone(), getPrefix(), getSuffix().

**Parameters:** comps

- A non-null enumeration of the components to add.
Each element of the enumeration is of class String.
The enumeration will be consumed to extract its
elements.
**Parameters:** syntax

- A non-null properties that specify the syntax of
this compound name. See class description for
contents of properties.

- CompoundName

```java
public CompoundName​(
String
n,

Properties
syntax)
throws
InvalidNameException
```

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

**Parameters:** n

- The non-null string to parse.
**Parameters:** syntax

- A non-null list of properties that specify the syntax of
this compound name. See class description for
contents of properties.
**Throws:** InvalidNameException

- If 'n' violates the syntax specified
by

syntax

.

---

#### Constructor Detail

CompoundName

```java
protected CompoundName​(
Enumeration
<
String
> comps,

Properties
syntax)
```

Constructs a new compound name instance using the components
specified in comps and syntax. This protected method is intended
to be used by subclasses of CompoundName when they override
methods such as clone(), getPrefix(), getSuffix().

**Parameters:** comps

- A non-null enumeration of the components to add.
Each element of the enumeration is of class String.
The enumeration will be consumed to extract its
elements.
**Parameters:** syntax

- A non-null properties that specify the syntax of
this compound name. See class description for
contents of properties.

---

#### CompoundName

protected CompoundName​(

Enumeration

<

String

> comps,

Properties

syntax)

Constructs a new compound name instance using the components
specified in comps and syntax. This protected method is intended
to be used by subclasses of CompoundName when they override
methods such as clone(), getPrefix(), getSuffix().

CompoundName

```java
public CompoundName​(
String
n,

Properties
syntax)
throws
InvalidNameException
```

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

**Parameters:** n

- The non-null string to parse.
**Parameters:** syntax

- A non-null list of properties that specify the syntax of
this compound name. See class description for
contents of properties.
**Throws:** InvalidNameException

- If 'n' violates the syntax specified
by

syntax

.

---

#### CompoundName

public CompoundName​(

String

n,

Properties

syntax)
throws

InvalidNameException

Constructs a new compound name instance by parsing the string n
using the syntax specified by the syntax properties supplied.

Method Detail

- toString

```java
public
String
toString()
```

Generates the string representation of this compound name, using
the syntax rules of the compound name. The syntax rules
are described in the class description.
An empty component is represented by an empty string.

The string representation thus generated can be passed to
the CompoundName constructor with the same syntax properties
to create a new equivalent compound name.

**Overrides:** toString

in class

Object
**Returns:** A non-null string representation of this compound name.

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is syntactically equal to this compound name.
If obj is null or not a CompoundName, false is returned.
Two compound names are equal if each component in one is "equal"
to the corresponding component in the other.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to compare against.
**Returns:** true if obj is equal to this compound name, false otherwise.
**See Also:** compareTo(java.lang.Object obj)

- hashCode

```java
public int hashCode()
```

Computes the hash code of this compound name.
The hash code is the sum of the hash codes of the "canonicalized"
forms of individual components of this compound name.
Each component is "canonicalized" according to the
compound name's syntax before its hash code is computed.
For a case-insensitive name, for example, the uppercased form of
a name has the same hash code as its lowercased equivalent.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- clone

```java
public
Object
clone()
```

Creates a copy of this compound name.
Changes to the components of this compound name won't
affect the new copy and vice versa.
The clone and this compound name share the same syntax.

**Specified by:** clone

in interface

Name
**Overrides:** clone

in class

Object
**Returns:** A non-null copy of this compound name.
**See Also:** Cloneable

- compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this CompoundName with the specified Object for order.
Returns a
negative integer, zero, or a positive integer as this Name is less
than, equal to, or greater than the given Object.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Specified by:** compareTo

in interface

Name
**Parameters:** obj

- The non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this Name
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is not a CompoundName.
**See Also:** equals(java.lang.Object)

- size

```java
public int size()
```

Retrieves the number of components in this compound name.

**Specified by:** size

in interface

Name
**Returns:** The nonnegative number of components in this compound name.

- isEmpty

```java
public boolean isEmpty()
```

Determines whether this compound name is empty.
A compound name is empty if it has zero components.

**Specified by:** isEmpty

in interface

Name
**Returns:** true if this compound name is empty, false otherwise.

- getAll

```java
public
Enumeration
<
String
> getAll()
```

Retrieves the components of this compound name as an enumeration
of strings.
The effects of updates to this compound name on this enumeration
is undefined.

**Specified by:** getAll

in interface

Name
**Returns:** A non-null enumeration of the components of this
compound name. Each element of the enumeration is of class String.

- get

```java
public
String
get​(int posn)
```

Retrieves a component of this compound name.

**Specified by:** get

in interface

Name
**Parameters:** posn

- The 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** The component at index posn.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the
specified range.

- getPrefix

```java
public
Name
getPrefix​(int posn)
```

Creates a compound name whose components consist of a prefix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned and
vice versa.

**Specified by:** getPrefix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

- getSuffix

```java
public
Name
getSuffix​(int posn)
```

Creates a compound name whose components consist of a suffix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned.

**Specified by:** getSuffix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty compound name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

- startsWith

```java
public boolean startsWith​(
Name
n)
```

Determines whether a compound name is a prefix of this compound name.
A compound name 'n' is a prefix if it is equal to
getPrefix(n.size())--in other words, this compound name
starts with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** startsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a prefix of this compound name, false otherwise.

- endsWith

```java
public boolean endsWith​(
Name
n)
```

Determines whether a compound name is a suffix of this compound name.
A compound name 'n' is a suffix if it is equal to
getSuffix(size()-n.size())--in other words, this
compound name ends with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** endsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a suffix of this compound name, false otherwise.

- addAll

```java
public
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- to the end of
this compound name.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** suffix

- The non-null components to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If suffix is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

- addAll

```java
public
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- at a specified
position within this compound name.
Components of this compound name at or after the index of the first
new component are shifted up (away from index 0)
to accommodate the new components.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** n

- The non-null components to add.
**Parameters:** posn

- The index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If n is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

- add

```java
public
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this compound name.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If adding comp at end of the name
would violate the compound name's syntax.

- add

```java
public
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this
compound name.
Components of this compound name at or after the index of the new
component are shifted up by one (away from index 0)
to accommodate the new component.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Parameters:** posn

- The index at which to add the new component.
Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If adding comp at the specified position
would violate the compound name's syntax.

- remove

```java
public
Object
remove​(int posn)
throws
InvalidNameException
```

Deletes a component from this compound name.
The component of this compound name at position 'posn' is removed,
and components at indices greater than 'posn'
are shifted down (towards index 0) by one.

**Specified by:** remove

in interface

Name
**Parameters:** posn

- The index of the component to delete.
Must be in the range [0,size()).
**Returns:** The component removed (a String).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range (includes case where
compound name is empty).
**Throws:** InvalidNameException

- If deleting the component
would violate the compound name's syntax.

---

#### Method Detail

toString

```java
public
String
toString()
```

Generates the string representation of this compound name, using
the syntax rules of the compound name. The syntax rules
are described in the class description.
An empty component is represented by an empty string.

The string representation thus generated can be passed to
the CompoundName constructor with the same syntax properties
to create a new equivalent compound name.

**Overrides:** toString

in class

Object
**Returns:** A non-null string representation of this compound name.

---

#### toString

public

String

toString()

Generates the string representation of this compound name, using
the syntax rules of the compound name. The syntax rules
are described in the class description.
An empty component is represented by an empty string.

The string representation thus generated can be passed to
the CompoundName constructor with the same syntax properties
to create a new equivalent compound name.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether obj is syntactically equal to this compound name.
If obj is null or not a CompoundName, false is returned.
Two compound names are equal if each component in one is "equal"
to the corresponding component in the other.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The possibly null object to compare against.
**Returns:** true if obj is equal to this compound name, false otherwise.
**See Also:** compareTo(java.lang.Object obj)

---

#### equals

public boolean equals​(

Object

obj)

Determines whether obj is syntactically equal to this compound name.
If obj is null or not a CompoundName, false is returned.
Two compound names are equal if each component in one is "equal"
to the corresponding component in the other.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

Equality is also defined in terms of the syntax of this compound name.
The default implementation of CompoundName uses the syntax properties
jndi.syntax.ignorecase and jndi.syntax.trimblanks when comparing
two components for equality. If case is ignored, two strings
with the same sequence of characters but with different cases
are considered equal. If blanks are being trimmed, leading and trailing
blanks are ignored for the purpose of the comparison.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

Both compound names must have the same number of components.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

Implementation note: Currently the syntax properties of the two compound
names are not compared for equality. They might be in the future.

hashCode

```java
public int hashCode()
```

Computes the hash code of this compound name.
The hash code is the sum of the hash codes of the "canonicalized"
forms of individual components of this compound name.
Each component is "canonicalized" according to the
compound name's syntax before its hash code is computed.
For a case-insensitive name, for example, the uppercased form of
a name has the same hash code as its lowercased equivalent.

**Overrides:** hashCode

in class

Object
**Returns:** An int representing the hash code of this name.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Computes the hash code of this compound name.
The hash code is the sum of the hash codes of the "canonicalized"
forms of individual components of this compound name.
Each component is "canonicalized" according to the
compound name's syntax before its hash code is computed.
For a case-insensitive name, for example, the uppercased form of
a name has the same hash code as its lowercased equivalent.

clone

```java
public
Object
clone()
```

Creates a copy of this compound name.
Changes to the components of this compound name won't
affect the new copy and vice versa.
The clone and this compound name share the same syntax.

**Specified by:** clone

in interface

Name
**Overrides:** clone

in class

Object
**Returns:** A non-null copy of this compound name.
**See Also:** Cloneable

---

#### clone

public

Object

clone()

Creates a copy of this compound name.
Changes to the components of this compound name won't
affect the new copy and vice versa.
The clone and this compound name share the same syntax.

compareTo

```java
public int compareTo​(
Object
obj)
```

Compares this CompoundName with the specified Object for order.
Returns a
negative integer, zero, or a positive integer as this Name is less
than, equal to, or greater than the given Object.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

**Specified by:** compareTo

in interface

Comparable

<

Object

>
**Specified by:** compareTo

in interface

Name
**Parameters:** obj

- The non-null object to compare against.
**Returns:** a negative integer, zero, or a positive integer as this Name
is less than, equal to, or greater than the given Object.
**Throws:** ClassCastException

- if obj is not a CompoundName.
**See Also:** equals(java.lang.Object)

---

#### compareTo

public int compareTo​(

Object

obj)

Compares this CompoundName with the specified Object for order.
Returns a
negative integer, zero, or a positive integer as this Name is less
than, equal to, or greater than the given Object.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

If obj is null or not an instance of CompoundName, ClassCastException
is thrown.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

See equals() for what it means for two compound names to be equal.
If two compound names are equal, 0 is returned.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

Ordering of compound names depend on the syntax of the compound name.
By default, they follow lexicographical rules for string comparison
with the extension that this applies to all the components in the
compound name and that comparison of individual components is
affected by the jndi.syntax.ignorecase and jndi.syntax.trimblanks
properties, identical to how they affect equals().
If this compound name is "lexicographically" lesser than obj,
a negative number is returned.
If this compound name is "lexicographically" greater than obj,
a positive number is returned.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

Implementation note: Currently the syntax properties of the two compound
names are not compared when checking order. They might be in the future.

size

```java
public int size()
```

Retrieves the number of components in this compound name.

**Specified by:** size

in interface

Name
**Returns:** The nonnegative number of components in this compound name.

---

#### size

public int size()

Retrieves the number of components in this compound name.

isEmpty

```java
public boolean isEmpty()
```

Determines whether this compound name is empty.
A compound name is empty if it has zero components.

**Specified by:** isEmpty

in interface

Name
**Returns:** true if this compound name is empty, false otherwise.

---

#### isEmpty

public boolean isEmpty()

Determines whether this compound name is empty.
A compound name is empty if it has zero components.

getAll

```java
public
Enumeration
<
String
> getAll()
```

Retrieves the components of this compound name as an enumeration
of strings.
The effects of updates to this compound name on this enumeration
is undefined.

**Specified by:** getAll

in interface

Name
**Returns:** A non-null enumeration of the components of this
compound name. Each element of the enumeration is of class String.

---

#### getAll

public

Enumeration

<

String

> getAll()

Retrieves the components of this compound name as an enumeration
of strings.
The effects of updates to this compound name on this enumeration
is undefined.

get

```java
public
String
get​(int posn)
```

Retrieves a component of this compound name.

**Specified by:** get

in interface

Name
**Parameters:** posn

- The 0-based index of the component to retrieve.
Must be in the range [0,size()).
**Returns:** The component at index posn.
**Throws:** ArrayIndexOutOfBoundsException

- if posn is outside the
specified range.

---

#### get

public

String

get​(int posn)

Retrieves a component of this compound name.

getPrefix

```java
public
Name
getPrefix​(int posn)
```

Creates a compound name whose components consist of a prefix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned and
vice versa.

**Specified by:** getPrefix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to stop.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [0,posn).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

---

#### getPrefix

public

Name

getPrefix​(int posn)

Creates a compound name whose components consist of a prefix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned and
vice versa.

getSuffix

```java
public
Name
getSuffix​(int posn)
```

Creates a compound name whose components consist of a suffix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned.

**Specified by:** getSuffix

in interface

Name
**Parameters:** posn

- The 0-based index of the component at which to start.
Must be in the range [0,size()].
**Returns:** A compound name consisting of the components at indexes in
the range [posn,size()). If posn is equal to
size(), an empty compound name is returned.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.

---

#### getSuffix

public

Name

getSuffix​(int posn)

Creates a compound name whose components consist of a suffix of the
components in this compound name.
The result and this compound name share the same syntax.
Subsequent changes to
this compound name do not affect the name that is returned.

startsWith

```java
public boolean startsWith​(
Name
n)
```

Determines whether a compound name is a prefix of this compound name.
A compound name 'n' is a prefix if it is equal to
getPrefix(n.size())--in other words, this compound name
starts with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** startsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a prefix of this compound name, false otherwise.

---

#### startsWith

public boolean startsWith​(

Name

n)

Determines whether a compound name is a prefix of this compound name.
A compound name 'n' is a prefix if it is equal to
getPrefix(n.size())--in other words, this compound name
starts with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

endsWith

```java
public boolean endsWith​(
Name
n)
```

Determines whether a compound name is a suffix of this compound name.
A compound name 'n' is a suffix if it is equal to
getSuffix(size()-n.size())--in other words, this
compound name ends with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

**Specified by:** endsWith

in interface

Name
**Parameters:** n

- The possibly null compound name to check.
**Returns:** true if n is a CompoundName and
is a suffix of this compound name, false otherwise.

---

#### endsWith

public boolean endsWith​(

Name

n)

Determines whether a compound name is a suffix of this compound name.
A compound name 'n' is a suffix if it is equal to
getSuffix(size()-n.size())--in other words, this
compound name ends with 'n'.
If n is null or not a compound name, false is returned.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

Implementation note: Currently the syntax properties of n
are not used when doing the comparison. They might be in the future.

addAll

```java
public
Name
addAll​(
Name
suffix)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- to the end of
this compound name.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** suffix

- The non-null components to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If suffix is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

---

#### addAll

public

Name

addAll​(

Name

suffix)
throws

InvalidNameException

Adds the components of a compound name -- in order -- to the end of
this compound name.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

addAll

```java
public
Name
addAll​(int posn,

Name
n)
throws
InvalidNameException
```

Adds the components of a compound name -- in order -- at a specified
position within this compound name.
Components of this compound name at or after the index of the first
new component are shifted up (away from index 0)
to accommodate the new components.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

**Specified by:** addAll

in interface

Name
**Parameters:** n

- The non-null components to add.
**Parameters:** posn

- The index in this name at which to add the new
components. Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If n is not a compound name,
or if the addition of the components violates the syntax
of this compound name (e.g. exceeding number of components).

---

#### addAll

public

Name

addAll​(int posn,

Name

n)
throws

InvalidNameException

Adds the components of a compound name -- in order -- at a specified
position within this compound name.
Components of this compound name at or after the index of the first
new component are shifted up (away from index 0)
to accommodate the new components.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

Implementation note: Currently the syntax properties of suffix
is not used or checked. They might be in the future.

add

```java
public
Name
add​(
String
comp)
throws
InvalidNameException
```

Adds a single component to the end of this compound name.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** InvalidNameException

- If adding comp at end of the name
would violate the compound name's syntax.

---

#### add

public

Name

add​(

String

comp)
throws

InvalidNameException

Adds a single component to the end of this compound name.

add

```java
public
Name
add​(int posn,

String
comp)
throws
InvalidNameException
```

Adds a single component at a specified position within this
compound name.
Components of this compound name at or after the index of the new
component are shifted up by one (away from index 0)
to accommodate the new component.

**Specified by:** add

in interface

Name
**Parameters:** comp

- The non-null component to add.
**Parameters:** posn

- The index at which to add the new component.
Must be in the range [0,size()].
**Returns:** The updated CompoundName, not a new one. Cannot be null.
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range.
**Throws:** InvalidNameException

- If adding comp at the specified position
would violate the compound name's syntax.

---

#### add

public

Name

add​(int posn,

String

comp)
throws

InvalidNameException

Adds a single component at a specified position within this
compound name.
Components of this compound name at or after the index of the new
component are shifted up by one (away from index 0)
to accommodate the new component.

remove

```java
public
Object
remove​(int posn)
throws
InvalidNameException
```

Deletes a component from this compound name.
The component of this compound name at position 'posn' is removed,
and components at indices greater than 'posn'
are shifted down (towards index 0) by one.

**Specified by:** remove

in interface

Name
**Parameters:** posn

- The index of the component to delete.
Must be in the range [0,size()).
**Returns:** The component removed (a String).
**Throws:** ArrayIndexOutOfBoundsException

- If posn is outside the specified range (includes case where
compound name is empty).
**Throws:** InvalidNameException

- If deleting the component
would violate the compound name's syntax.

---

#### remove

public

Object

remove​(int posn)
throws

InvalidNameException

Deletes a component from this compound name.
The component of this compound name at position 'posn' is removed,
and components at indices greater than 'posn'
are shifted down (towards index 0) by one.

---

