# Class Runtime.Version

**Source:** `java.base\java\lang\Runtime.Version.html`

### Class Description

```java
public static final class
Runtime.Version

extends
Object

implements
Comparable
<
Runtime.Version
>
```

A representation of a version string for an implementation of the
Java SE Platform. A version string consists of a version number
optionally followed by pre-release and build information.

Version numbers

A

version number

,

$VNUM

, is a non-empty sequence of
elements separated by period characters (U+002E). An element is either
zero, or an unsigned integer numeral without leading zeros. The final
element in a version number must not be zero. When an element is
incremented, all subsequent elements are removed. The format is:

```java
[1-9][0-9]*((\.0)*\.[1-9][0-9]*)*
```

The sequence may be of arbitrary length but the first four elements
are assigned specific meanings, as follows:

```java
$FEATURE.$INTERIM.$UPDATE.$PATCH
```

- $FEATURE

— The
feature-release counter, incremented for every feature release
regardless of release content. Features may be added in a feature
release; they may also be removed, if advance notice was given at least
one feature release ahead of time. Incompatible changes may be made
when justified.
- $INTERIM

— The
interim-release counter, incremented for non-feature releases that
contain compatible bug fixes and enhancements but no incompatible
changes, no feature removals, and no changes to standard APIs.
- $UPDATE

— The update-release
counter, incremented for compatible update releases that fix security
issues, regressions, and bugs in newer features.
- $PATCH

— The emergency
patch-release counter, incremented only when it's necessary to produce
an emergency release to fix a critical issue.

The fifth and later elements of a version number are free for use by
platform implementors, to identify implementor-specific patch
releases.

A version number never has trailing zero elements. If an element
and all those that follow it logically have the value zero then all of
them are omitted.

The sequence of numerals in a version number is compared to another
such sequence in numerical, pointwise fashion;

e.g.

,

10.0.4

is less than

10.1.2

. If one sequence is shorter than
another then the missing elements of the shorter sequence are considered
to be less than the corresponding elements of the longer sequence;

e.g.

,

10.0.2

is less than

10.0.2.1

.

Version strings

A

version string

,

$VSTR

, is a version number

$VNUM

, as described above, optionally followed by pre-release and build
information, in one of the following formats:

```java
$VNUM(-$PRE)?\+$BUILD(-$OPT)?
$VNUM-$PRE(-$OPT)?
$VNUM(+-$OPT)?
```

where:

- $PRE

, matching

([a-zA-Z0-9]+)

— A pre-release identifier. Typically

ea

, for a
potentially unstable early-access release under active development, or

internal

, for an internal developer build.
- $BUILD

, matching

(0|[1-9][0-9]*)

— The build number, incremented for each promoted
build.

$BUILD

is reset to

1

when any portion of

$VNUM

is incremented.
- $OPT

, matching

([-a-zA-Z0-9.]+)

— Additional build information, if desired. In the case of an

internal

build this will often contain the date and time of the
build.

A version string

10-ea

matches

$VNUM = "10"

and

$PRE = "ea"

. The version string

10+-ea

matches

$VNUM = "10"

and

$OPT = "ea"

.

When comparing two version strings, the value of

$OPT

, if
present, may or may not be significant depending on the chosen
comparison method. The comparison methods

compareTo()

and

compareToIgnoreOptional()

should be used consistently with the
corresponding methods

equals()

and

equalsIgnoreOptional()

.

A

short version string

,

$SVSTR

, often useful in
less formal contexts, is a version number optionally followed by a
pre-release identifier:

```java
$VNUM(-$PRE)?
```

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

Version

may have unpredictable results and should be avoided.

**All Implemented Interfaces:** Comparable

<

Runtime.Version

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Runtime.Version
parse​(
String
s)

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

**Parameters:**
- s

- A string to interpret as a version

**Returns:**
- The Version of the given string

**Throws:**
- IllegalArgumentException

- If the given string cannot be interpreted as a valid
version
- NullPointerException

- If the given string is

null
- NumberFormatException

- If an element of the version number or the build number
cannot be represented as an

Integer

---

#### public int feature()

Returns the value of the

feature

element of
the version number.

**Returns:**
- The value of the feature element

**Since:**
- 10

---

#### public int interim()

Returns the value of the

interim

element of
the version number, or zero if it is absent.

**Returns:**
- The value of the interim element, or zero

**Since:**
- 10

---

#### public int update()

Returns the value of the

update

element of the
version number, or zero if it is absent.

**Returns:**
- The value of the update element, or zero

**Since:**
- 10

---

#### public int patch()

Returns the value of the

patch

element of the
version number, or zero if it is absent.

**Returns:**
- The value of the patch element, or zero

**Since:**
- 10

---

#### @Deprecated
(
since
="10")
public int major()

Returns the value of the major element of the version number.

**Returns:**
- The value of the feature element

---

#### @Deprecated
(
since
="10")
public int minor()

Returns the value of the minor element of the version number, or
zero if it is absent.

**Returns:**
- The value of the interim element, or zero

---

#### @Deprecated
(
since
="10")
public int security()

Returns the value of the security element of the version number, or
zero if it is absent.

**Returns:**
- The value of the update element, or zero

---

#### public
List
<
Integer
> version()

Returns an unmodifiable

List

of the integers
represented in the

version number

.
The

List

always contains at least one element corresponding to
the

feature version number

.

**Returns:**
- An unmodifiable list of the integers
represented in the version number

---

#### public
Optional
<
String
> pre()

Returns the optional

pre-release

information.

**Returns:**
- The optional pre-release information as a String

---

#### public
Optional
<
Integer
> build()

Returns the

build number

.

**Returns:**
- The optional build number.

---

#### public
Optional
<
String
> optional()

Returns

optional

additional identifying build
information.

**Returns:**
- Additional build information as a String

---

#### public int compareTo​(
Runtime.Version
obj)

Compares this version to another.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

**Specified by:**
- compareTo

in interface

Comparable

<

Runtime.Version

>

**Parameters:**
- obj

- The object to be compared

**Returns:**
- A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version

**Throws:**
- NullPointerException

- If the given object is

null

---

#### public int compareToIgnoreOptional​(
Runtime.Version
obj)

Compares this version to another disregarding optional build
information.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

**Parameters:**
- obj

- The object to be compared

**Returns:**
- A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version

**Throws:**
- NullPointerException

- If the given object is

null

---

#### public
String
toString()

Returns a string representation of this version.

**Overrides:**
- toString

in class

Object

**Returns:**
- The version string

---

#### public boolean equals​(
Object
obj)

Determines whether this

Version

is equal to another object.

Two

Version

s are equal if and only if they represent the
same version string.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- The object to which this

Version

is to be compared

**Returns:**
- true

if, and only if, the given object is a

Version

that is identical to this

Version

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public boolean equalsIgnoreOptional​(
Object
obj)

Determines whether this

Version

is equal to another
disregarding optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

**Parameters:**
- obj

- The object to which this

Version

is to be compared

**Returns:**
- true

if, and only if, the given object is a

Version

that is identical to this

Version

ignoring the optional build information

---

#### public int hashCode()

Returns the hash code of this version.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- The hashcode of this version

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

### Additional Sections

#### Class Runtime.Version

java.lang.Object

- java.lang.Runtime.Version

java.lang.Runtime.Version

**All Implemented Interfaces:** Comparable

<

Runtime.Version

>

**Enclosing class:** Runtime

```java
public static final class
Runtime.Version

extends
Object

implements
Comparable
<
Runtime.Version
>
```

A representation of a version string for an implementation of the
Java SE Platform. A version string consists of a version number
optionally followed by pre-release and build information.

Version numbers

A

version number

,

$VNUM

, is a non-empty sequence of
elements separated by period characters (U+002E). An element is either
zero, or an unsigned integer numeral without leading zeros. The final
element in a version number must not be zero. When an element is
incremented, all subsequent elements are removed. The format is:

```java
[1-9][0-9]*((\.0)*\.[1-9][0-9]*)*
```

The sequence may be of arbitrary length but the first four elements
are assigned specific meanings, as follows:

```java
$FEATURE.$INTERIM.$UPDATE.$PATCH
```

- $FEATURE

— The
feature-release counter, incremented for every feature release
regardless of release content. Features may be added in a feature
release; they may also be removed, if advance notice was given at least
one feature release ahead of time. Incompatible changes may be made
when justified.
- $INTERIM

— The
interim-release counter, incremented for non-feature releases that
contain compatible bug fixes and enhancements but no incompatible
changes, no feature removals, and no changes to standard APIs.
- $UPDATE

— The update-release
counter, incremented for compatible update releases that fix security
issues, regressions, and bugs in newer features.
- $PATCH

— The emergency
patch-release counter, incremented only when it's necessary to produce
an emergency release to fix a critical issue.

The fifth and later elements of a version number are free for use by
platform implementors, to identify implementor-specific patch
releases.

A version number never has trailing zero elements. If an element
and all those that follow it logically have the value zero then all of
them are omitted.

The sequence of numerals in a version number is compared to another
such sequence in numerical, pointwise fashion;

e.g.

,

10.0.4

is less than

10.1.2

. If one sequence is shorter than
another then the missing elements of the shorter sequence are considered
to be less than the corresponding elements of the longer sequence;

e.g.

,

10.0.2

is less than

10.0.2.1

.

Version strings

A

version string

,

$VSTR

, is a version number

$VNUM

, as described above, optionally followed by pre-release and build
information, in one of the following formats:

```java
$VNUM(-$PRE)?\+$BUILD(-$OPT)?
$VNUM-$PRE(-$OPT)?
$VNUM(+-$OPT)?
```

where:

- $PRE

, matching

([a-zA-Z0-9]+)

— A pre-release identifier. Typically

ea

, for a
potentially unstable early-access release under active development, or

internal

, for an internal developer build.
- $BUILD

, matching

(0|[1-9][0-9]*)

— The build number, incremented for each promoted
build.

$BUILD

is reset to

1

when any portion of

$VNUM

is incremented.
- $OPT

, matching

([-a-zA-Z0-9.]+)

— Additional build information, if desired. In the case of an

internal

build this will often contain the date and time of the
build.

A version string

10-ea

matches

$VNUM = "10"

and

$PRE = "ea"

. The version string

10+-ea

matches

$VNUM = "10"

and

$OPT = "ea"

.

When comparing two version strings, the value of

$OPT

, if
present, may or may not be significant depending on the chosen
comparison method. The comparison methods

compareTo()

and

compareToIgnoreOptional()

should be used consistently with the
corresponding methods

equals()

and

equalsIgnoreOptional()

.

A

short version string

,

$SVSTR

, often useful in
less formal contexts, is a version number optionally followed by a
pre-release identifier:

```java
$VNUM(-$PRE)?
```

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

Version

may have unpredictable results and should be avoided.

**Since:** 9

public static final class

Runtime.Version

extends

Object

implements

Comparable

<

Runtime.Version

>

A representation of a version string for an implementation of the
Java SE Platform. A version string consists of a version number
optionally followed by pre-release and build information.

Version numbers

A

version number

,

$VNUM

, is a non-empty sequence of
elements separated by period characters (U+002E). An element is either
zero, or an unsigned integer numeral without leading zeros. The final
element in a version number must not be zero. When an element is
incremented, all subsequent elements are removed. The format is:

```java
[1-9][0-9]*((\.0)*\.[1-9][0-9]*)*
```

The sequence may be of arbitrary length but the first four elements
are assigned specific meanings, as follows:

```java
$FEATURE.$INTERIM.$UPDATE.$PATCH
```

- $FEATURE

— The
feature-release counter, incremented for every feature release
regardless of release content. Features may be added in a feature
release; they may also be removed, if advance notice was given at least
one feature release ahead of time. Incompatible changes may be made
when justified.
- $INTERIM

— The
interim-release counter, incremented for non-feature releases that
contain compatible bug fixes and enhancements but no incompatible
changes, no feature removals, and no changes to standard APIs.
- $UPDATE

— The update-release
counter, incremented for compatible update releases that fix security
issues, regressions, and bugs in newer features.
- $PATCH

— The emergency
patch-release counter, incremented only when it's necessary to produce
an emergency release to fix a critical issue.

The fifth and later elements of a version number are free for use by
platform implementors, to identify implementor-specific patch
releases.

A version number never has trailing zero elements. If an element
and all those that follow it logically have the value zero then all of
them are omitted.

The sequence of numerals in a version number is compared to another
such sequence in numerical, pointwise fashion;

e.g.

,

10.0.4

is less than

10.1.2

. If one sequence is shorter than
another then the missing elements of the shorter sequence are considered
to be less than the corresponding elements of the longer sequence;

e.g.

,

10.0.2

is less than

10.0.2.1

.

Version strings

A

version string

,

$VSTR

, is a version number

$VNUM

, as described above, optionally followed by pre-release and build
information, in one of the following formats:

```java
$VNUM(-$PRE)?\+$BUILD(-$OPT)?
$VNUM-$PRE(-$OPT)?
$VNUM(+-$OPT)?
```

where:

- $PRE

, matching

([a-zA-Z0-9]+)

— A pre-release identifier. Typically

ea

, for a
potentially unstable early-access release under active development, or

internal

, for an internal developer build.
- $BUILD

, matching

(0|[1-9][0-9]*)

— The build number, incremented for each promoted
build.

$BUILD

is reset to

1

when any portion of

$VNUM

is incremented.
- $OPT

, matching

([-a-zA-Z0-9.]+)

— Additional build information, if desired. In the case of an

internal

build this will often contain the date and time of the
build.

A version string

10-ea

matches

$VNUM = "10"

and

$PRE = "ea"

. The version string

10+-ea

matches

$VNUM = "10"

and

$OPT = "ea"

.

When comparing two version strings, the value of

$OPT

, if
present, may or may not be significant depending on the chosen
comparison method. The comparison methods

compareTo()

and

compareToIgnoreOptional()

should be used consistently with the
corresponding methods

equals()

and

equalsIgnoreOptional()

.

A

short version string

,

$SVSTR

, often useful in
less formal contexts, is a version number optionally followed by a
pre-release identifier:

```java
$VNUM(-$PRE)?
```

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

Version

may have unpredictable results and should be avoided.

---

#### Version numbers

A

version number

,

$VNUM

, is a non-empty sequence of
elements separated by period characters (U+002E). An element is either
zero, or an unsigned integer numeral without leading zeros. The final
element in a version number must not be zero. When an element is
incremented, all subsequent elements are removed. The format is:

[1-9][0-9]*((\.0)*\.[1-9][0-9]*)*

The sequence may be of arbitrary length but the first four elements
are assigned specific meanings, as follows:

$FEATURE.$INTERIM.$UPDATE.$PATCH

$FEATURE

— The
feature-release counter, incremented for every feature release
regardless of release content. Features may be added in a feature
release; they may also be removed, if advance notice was given at least
one feature release ahead of time. Incompatible changes may be made
when justified.

$INTERIM

— The
interim-release counter, incremented for non-feature releases that
contain compatible bug fixes and enhancements but no incompatible
changes, no feature removals, and no changes to standard APIs.

$UPDATE

— The update-release
counter, incremented for compatible update releases that fix security
issues, regressions, and bugs in newer features.

$PATCH

— The emergency
patch-release counter, incremented only when it's necessary to produce
an emergency release to fix a critical issue.

$FEATURE

— The
feature-release counter, incremented for every feature release
regardless of release content. Features may be added in a feature
release; they may also be removed, if advance notice was given at least
one feature release ahead of time. Incompatible changes may be made
when justified.

$INTERIM

— The
interim-release counter, incremented for non-feature releases that
contain compatible bug fixes and enhancements but no incompatible
changes, no feature removals, and no changes to standard APIs.

$UPDATE

— The update-release
counter, incremented for compatible update releases that fix security
issues, regressions, and bugs in newer features.

$PATCH

— The emergency
patch-release counter, incremented only when it's necessary to produce
an emergency release to fix a critical issue.

The fifth and later elements of a version number are free for use by
platform implementors, to identify implementor-specific patch
releases.

A version number never has trailing zero elements. If an element
and all those that follow it logically have the value zero then all of
them are omitted.

The sequence of numerals in a version number is compared to another
such sequence in numerical, pointwise fashion;

e.g.

,

10.0.4

is less than

10.1.2

. If one sequence is shorter than
another then the missing elements of the shorter sequence are considered
to be less than the corresponding elements of the longer sequence;

e.g.

,

10.0.2

is less than

10.0.2.1

.

---

#### Version strings

A

version string

,

$VSTR

, is a version number

$VNUM

, as described above, optionally followed by pre-release and build
information, in one of the following formats:

$VNUM(-$PRE)?\+$BUILD(-$OPT)?
$VNUM-$PRE(-$OPT)?
$VNUM(+-$OPT)?

where:

$PRE

, matching

([a-zA-Z0-9]+)

— A pre-release identifier. Typically

ea

, for a
potentially unstable early-access release under active development, or

internal

, for an internal developer build.

$BUILD

, matching

(0|[1-9][0-9]*)

— The build number, incremented for each promoted
build.

$BUILD

is reset to

1

when any portion of

$VNUM

is incremented.

$OPT

, matching

([-a-zA-Z0-9.]+)

— Additional build information, if desired. In the case of an

internal

build this will often contain the date and time of the
build.

$PRE

, matching

([a-zA-Z0-9]+)

— A pre-release identifier. Typically

ea

, for a
potentially unstable early-access release under active development, or

internal

, for an internal developer build.

$BUILD

, matching

(0|[1-9][0-9]*)

— The build number, incremented for each promoted
build.

$BUILD

is reset to

1

when any portion of

$VNUM

is incremented.

$OPT

, matching

([-a-zA-Z0-9.]+)

— Additional build information, if desired. In the case of an

internal

build this will often contain the date and time of the
build.

A version string

10-ea

matches

$VNUM = "10"

and

$PRE = "ea"

. The version string

10+-ea

matches

$VNUM = "10"

and

$OPT = "ea"

.

When comparing two version strings, the value of

$OPT

, if
present, may or may not be significant depending on the chosen
comparison method. The comparison methods

compareTo()

and

compareToIgnoreOptional()

should be used consistently with the
corresponding methods

equals()

and

equalsIgnoreOptional()

.

A

short version string

,

$SVSTR

, often useful in
less formal contexts, is a version number optionally followed by a
pre-release identifier:

$VNUM(-$PRE)?

This is a

value-based

class; use of identity-sensitive operations (including reference equality
(

==

), identity hash code, or synchronization) on instances of

Version

may have unpredictable results and should be avoided.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Optional

<

Integer

>

build

()

Returns the

build number

.

int

compareTo

​(

Runtime.Version

obj)

Compares this version to another.

int

compareToIgnoreOptional

​(

Runtime.Version

obj)

Compares this version to another disregarding optional build
information.

boolean

equals

​(

Object

obj)

Determines whether this

Version

is equal to another object.

boolean

equalsIgnoreOptional

​(

Object

obj)

Determines whether this

Version

is equal to another
disregarding optional build information.

int

feature

()

Returns the value of the

feature

element of
the version number.

int

hashCode

()

Returns the hash code of this version.

int

interim

()

Returns the value of the

interim

element of
the version number, or zero if it is absent.

int

major

()

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release.

int

minor

()

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release.

Optional

<

String

>

optional

()

Returns

optional

additional identifying build
information.

static

Runtime.Version

parse

​(

String

s)

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

int

patch

()

Returns the value of the

patch

element of the
version number, or zero if it is absent.

Optional

<

String

>

pre

()

Returns the optional

pre-release

information.

int

security

()

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release.

String

toString

()

Returns a string representation of this version.

int

update

()

Returns the value of the

update

element of the
version number, or zero if it is absent.

List

<

Integer

>

version

()

Returns an unmodifiable

List

of the integers
represented in the

version number

.

- Methods declared in class java.lang.

Object

clone

,

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

Optional

<

Integer

>

build

()

Returns the

build number

.

int

compareTo

​(

Runtime.Version

obj)

Compares this version to another.

int

compareToIgnoreOptional

​(

Runtime.Version

obj)

Compares this version to another disregarding optional build
information.

boolean

equals

​(

Object

obj)

Determines whether this

Version

is equal to another object.

boolean

equalsIgnoreOptional

​(

Object

obj)

Determines whether this

Version

is equal to another
disregarding optional build information.

int

feature

()

Returns the value of the

feature

element of
the version number.

int

hashCode

()

Returns the hash code of this version.

int

interim

()

Returns the value of the

interim

element of
the version number, or zero if it is absent.

int

major

()

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release.

int

minor

()

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release.

Optional

<

String

>

optional

()

Returns

optional

additional identifying build
information.

static

Runtime.Version

parse

​(

String

s)

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

int

patch

()

Returns the value of the

patch

element of the
version number, or zero if it is absent.

Optional

<

String

>

pre

()

Returns the optional

pre-release

information.

int

security

()

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release.

String

toString

()

Returns a string representation of this version.

int

update

()

Returns the value of the

update

element of the
version number, or zero if it is absent.

List

<

Integer

>

version

()

Returns an unmodifiable

List

of the integers
represented in the

version number

.

- Methods declared in class java.lang.

Object

clone

,

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

Returns the

build number

.

Compares this version to another.

Compares this version to another disregarding optional build
information.

Determines whether this

Version

is equal to another object.

Determines whether this

Version

is equal to another
disregarding optional build information.

Returns the value of the

feature

element of
the version number.

Returns the hash code of this version.

Returns the value of the

interim

element of
the version number, or zero if it is absent.

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release.

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release.

Returns

optional

additional identifying build
information.

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

Returns the value of the

patch

element of the
version number, or zero if it is absent.

Returns the optional

pre-release

information.

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release.

Returns a string representation of this version.

Returns the value of the

update

element of the
version number, or zero if it is absent.

Returns an unmodifiable

List

of the integers
represented in the

version number

.

Methods declared in class java.lang.

Object

clone

,

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

============ METHOD DETAIL ==========

- Method Detail

- parse

```java
public static
Runtime.Version
parse​(
String
s)
```

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

**Parameters:** s

- A string to interpret as a version
**Returns:** The Version of the given string
**Throws:** IllegalArgumentException

- If the given string cannot be interpreted as a valid
version
**Throws:** NullPointerException

- If the given string is

null
**Throws:** NumberFormatException

- If an element of the version number or the build number
cannot be represented as an

Integer

- feature

```java
public int feature()
```

Returns the value of the

feature

element of
the version number.

**Returns:** The value of the feature element
**Since:** 10

- interim

```java
public int interim()
```

Returns the value of the

interim

element of
the version number, or zero if it is absent.

**Returns:** The value of the interim element, or zero
**Since:** 10

- update

```java
public int update()
```

Returns the value of the

update

element of the
version number, or zero if it is absent.

**Returns:** The value of the update element, or zero
**Since:** 10

- patch

```java
public int patch()
```

Returns the value of the

patch

element of the
version number, or zero if it is absent.

**Returns:** The value of the patch element, or zero
**Since:** 10

- major

```java
@Deprecated
(
since
="10")
public int major()
```

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release. Use the

feature()

method in preference to this method. For compatibility,
this method returns the value of the

feature

element.

Returns the value of the major element of the version number.

**Returns:** The value of the feature element

- minor

```java
@Deprecated
(
since
="10")
public int minor()
```

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release. Use the

interim()

method in preference to this method. For compatibility,
this method returns the value of the

interim

element, or zero if it is absent.

Returns the value of the minor element of the version number, or
zero if it is absent.

**Returns:** The value of the interim element, or zero

- security

```java
@Deprecated
(
since
="10")
public int security()
```

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release. Use the

update()

method in preference to this method. For compatibility, this method
returns the value of the

update

element, or
zero if it is absent.

Returns the value of the security element of the version number, or
zero if it is absent.

**Returns:** The value of the update element, or zero

- version

```java
public
List
<
Integer
> version()
```

Returns an unmodifiable

List

of the integers
represented in the

version number

.
The

List

always contains at least one element corresponding to
the

feature version number

.

**Returns:** An unmodifiable list of the integers
represented in the version number

- pre

```java
public
Optional
<
String
> pre()
```

Returns the optional

pre-release

information.

**Returns:** The optional pre-release information as a String

- build

```java
public
Optional
<
Integer
> build()
```

Returns the

build number

.

**Returns:** The optional build number.

- optional

```java
public
Optional
<
String
> optional()
```

Returns

optional

additional identifying build
information.

**Returns:** Additional build information as a String

- compareTo

```java
public int compareTo​(
Runtime.Version
obj)
```

Compares this version to another.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

**Specified by:** compareTo

in interface

Comparable

<

Runtime.Version

>
**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

- compareToIgnoreOptional

```java
public int compareToIgnoreOptional​(
Runtime.Version
obj)
```

Compares this version to another disregarding optional build
information.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

- toString

```java
public
String
toString()
```

Returns a string representation of this version.

**Overrides:** toString

in class

Object
**Returns:** The version string

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

Version

is equal to another object.

Two

Version

s are equal if and only if they represent the
same version string.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version
**See Also:** Object.hashCode()

,

HashMap

- equalsIgnoreOptional

```java
public boolean equalsIgnoreOptional​(
Object
obj)
```

Determines whether this

Version

is equal to another
disregarding optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version

ignoring the optional build information

- hashCode

```java
public int hashCode()
```

Returns the hash code of this version.

**Overrides:** hashCode

in class

Object
**Returns:** The hashcode of this version
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

Method Detail

- parse

```java
public static
Runtime.Version
parse​(
String
s)
```

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

**Parameters:** s

- A string to interpret as a version
**Returns:** The Version of the given string
**Throws:** IllegalArgumentException

- If the given string cannot be interpreted as a valid
version
**Throws:** NullPointerException

- If the given string is

null
**Throws:** NumberFormatException

- If an element of the version number or the build number
cannot be represented as an

Integer

- feature

```java
public int feature()
```

Returns the value of the

feature

element of
the version number.

**Returns:** The value of the feature element
**Since:** 10

- interim

```java
public int interim()
```

Returns the value of the

interim

element of
the version number, or zero if it is absent.

**Returns:** The value of the interim element, or zero
**Since:** 10

- update

```java
public int update()
```

Returns the value of the

update

element of the
version number, or zero if it is absent.

**Returns:** The value of the update element, or zero
**Since:** 10

- patch

```java
public int patch()
```

Returns the value of the

patch

element of the
version number, or zero if it is absent.

**Returns:** The value of the patch element, or zero
**Since:** 10

- major

```java
@Deprecated
(
since
="10")
public int major()
```

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release. Use the

feature()

method in preference to this method. For compatibility,
this method returns the value of the

feature

element.

Returns the value of the major element of the version number.

**Returns:** The value of the feature element

- minor

```java
@Deprecated
(
since
="10")
public int minor()
```

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release. Use the

interim()

method in preference to this method. For compatibility,
this method returns the value of the

interim

element, or zero if it is absent.

Returns the value of the minor element of the version number, or
zero if it is absent.

**Returns:** The value of the interim element, or zero

- security

```java
@Deprecated
(
since
="10")
public int security()
```

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release. Use the

update()

method in preference to this method. For compatibility, this method
returns the value of the

update

element, or
zero if it is absent.

Returns the value of the security element of the version number, or
zero if it is absent.

**Returns:** The value of the update element, or zero

- version

```java
public
List
<
Integer
> version()
```

Returns an unmodifiable

List

of the integers
represented in the

version number

.
The

List

always contains at least one element corresponding to
the

feature version number

.

**Returns:** An unmodifiable list of the integers
represented in the version number

- pre

```java
public
Optional
<
String
> pre()
```

Returns the optional

pre-release

information.

**Returns:** The optional pre-release information as a String

- build

```java
public
Optional
<
Integer
> build()
```

Returns the

build number

.

**Returns:** The optional build number.

- optional

```java
public
Optional
<
String
> optional()
```

Returns

optional

additional identifying build
information.

**Returns:** Additional build information as a String

- compareTo

```java
public int compareTo​(
Runtime.Version
obj)
```

Compares this version to another.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

**Specified by:** compareTo

in interface

Comparable

<

Runtime.Version

>
**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

- compareToIgnoreOptional

```java
public int compareToIgnoreOptional​(
Runtime.Version
obj)
```

Compares this version to another disregarding optional build
information.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

- toString

```java
public
String
toString()
```

Returns a string representation of this version.

**Overrides:** toString

in class

Object
**Returns:** The version string

- equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

Version

is equal to another object.

Two

Version

s are equal if and only if they represent the
same version string.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version
**See Also:** Object.hashCode()

,

HashMap

- equalsIgnoreOptional

```java
public boolean equalsIgnoreOptional​(
Object
obj)
```

Determines whether this

Version

is equal to another
disregarding optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version

ignoring the optional build information

- hashCode

```java
public int hashCode()
```

Returns the hash code of this version.

**Overrides:** hashCode

in class

Object
**Returns:** The hashcode of this version
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### Method Detail

parse

```java
public static
Runtime.Version
parse​(
String
s)
```

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

**Parameters:** s

- A string to interpret as a version
**Returns:** The Version of the given string
**Throws:** IllegalArgumentException

- If the given string cannot be interpreted as a valid
version
**Throws:** NullPointerException

- If the given string is

null
**Throws:** NumberFormatException

- If an element of the version number or the build number
cannot be represented as an

Integer

---

#### parse

public static

Runtime.Version

parse​(

String

s)

Parses the given string as a valid

version string

containing a

version number

followed by pre-release and
build information.

feature

```java
public int feature()
```

Returns the value of the

feature

element of
the version number.

**Returns:** The value of the feature element
**Since:** 10

---

#### feature

public int feature()

Returns the value of the

feature

element of
the version number.

interim

```java
public int interim()
```

Returns the value of the

interim

element of
the version number, or zero if it is absent.

**Returns:** The value of the interim element, or zero
**Since:** 10

---

#### interim

public int interim()

Returns the value of the

interim

element of
the version number, or zero if it is absent.

update

```java
public int update()
```

Returns the value of the

update

element of the
version number, or zero if it is absent.

**Returns:** The value of the update element, or zero
**Since:** 10

---

#### update

public int update()

Returns the value of the

update

element of the
version number, or zero if it is absent.

patch

```java
public int patch()
```

Returns the value of the

patch

element of the
version number, or zero if it is absent.

**Returns:** The value of the patch element, or zero
**Since:** 10

---

#### patch

public int patch()

Returns the value of the

patch

element of the
version number, or zero if it is absent.

major

```java
@Deprecated
(
since
="10")
public int major()
```

Deprecated.

As of Java SE 10, the first element of a version
number is not the major-release number but the feature-release
counter, incremented for every time-based release. Use the

feature()

method in preference to this method. For compatibility,
this method returns the value of the

feature

element.

Returns the value of the major element of the version number.

**Returns:** The value of the feature element

---

#### major

@Deprecated

(

since

="10")
public int major()

Returns the value of the major element of the version number.

minor

```java
@Deprecated
(
since
="10")
public int minor()
```

Deprecated.

As of Java SE 10, the second element of a version
number is not the minor-release number but the interim-release
counter, incremented for every interim release. Use the

interim()

method in preference to this method. For compatibility,
this method returns the value of the

interim

element, or zero if it is absent.

Returns the value of the minor element of the version number, or
zero if it is absent.

**Returns:** The value of the interim element, or zero

---

#### minor

@Deprecated

(

since

="10")
public int minor()

Returns the value of the minor element of the version number, or
zero if it is absent.

security

```java
@Deprecated
(
since
="10")
public int security()
```

Deprecated.

As of Java SE 10, the third element of a version
number is not the security level but the update-release counter,
incremented for every update release. Use the

update()

method in preference to this method. For compatibility, this method
returns the value of the

update

element, or
zero if it is absent.

Returns the value of the security element of the version number, or
zero if it is absent.

**Returns:** The value of the update element, or zero

---

#### security

@Deprecated

(

since

="10")
public int security()

Returns the value of the security element of the version number, or
zero if it is absent.

version

```java
public
List
<
Integer
> version()
```

Returns an unmodifiable

List

of the integers
represented in the

version number

.
The

List

always contains at least one element corresponding to
the

feature version number

.

**Returns:** An unmodifiable list of the integers
represented in the version number

---

#### version

public

List

<

Integer

> version()

Returns an unmodifiable

List

of the integers
represented in the

version number

.
The

List

always contains at least one element corresponding to
the

feature version number

.

pre

```java
public
Optional
<
String
> pre()
```

Returns the optional

pre-release

information.

**Returns:** The optional pre-release information as a String

---

#### pre

public

Optional

<

String

> pre()

Returns the optional

pre-release

information.

build

```java
public
Optional
<
Integer
> build()
```

Returns the

build number

.

**Returns:** The optional build number.

---

#### build

public

Optional

<

Integer

> build()

Returns the

build number

.

optional

```java
public
Optional
<
String
> optional()
```

Returns

optional

additional identifying build
information.

**Returns:** Additional build information as a String

---

#### optional

public

Optional

<

String

> optional()

Returns

optional

additional identifying build
information.

compareTo

```java
public int compareTo​(
Runtime.Version
obj)
```

Compares this version to another.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

**Specified by:** compareTo

in interface

Comparable

<

Runtime.Version

>
**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

---

#### compareTo

public int compareTo​(

Runtime.Version

obj)

Compares this version to another.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

Each of the components in the

version

is
compared in the following order of precedence: version numbers,
pre-release identifiers, build numbers, optional build information.

Comparison begins by examining the sequence of version numbers.
If one sequence is shorter than another, then the missing elements
of the shorter sequence are considered to be less than the
corresponding elements of the longer sequence.

A version with a pre-release identifier is always considered to
be less than a version without one. Pre-release identifiers are
compared numerically when they consist only of digits, and
lexicographically otherwise. Numeric identifiers are considered to
be less than non-numeric identifiers.

A version without a build number is always less than one with a
build number; otherwise build numbers are compared numerically.

The optional build information is compared lexicographically.
During this comparison, a version with optional build information is
considered to be greater than a version without one.

compareToIgnoreOptional

```java
public int compareToIgnoreOptional​(
Runtime.Version
obj)
```

Compares this version to another disregarding optional build
information.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

**Parameters:** obj

- The object to be compared
**Returns:** A negative integer, zero, or a positive integer if this

Version

is less than, equal to, or greater than the
given

Version
**Throws:** NullPointerException

- If the given object is

null

---

#### compareToIgnoreOptional

public int compareToIgnoreOptional​(

Runtime.Version

obj)

Compares this version to another disregarding optional build
information.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

Two versions are compared by examining the version string as
described in

compareTo(Version)

with the exception that the
optional build information is always ignored.

This method provides ordering which is consistent with

equalsIgnoreOptional()

.

toString

```java
public
String
toString()
```

Returns a string representation of this version.

**Overrides:** toString

in class

Object
**Returns:** The version string

---

#### toString

public

String

toString()

Returns a string representation of this version.

equals

```java
public boolean equals​(
Object
obj)
```

Determines whether this

Version

is equal to another object.

Two

Version

s are equal if and only if they represent the
same version string.

**Overrides:** equals

in class

Object
**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Determines whether this

Version

is equal to another object.

Two

Version

s are equal if and only if they represent the
same version string.

Two

Version

s are equal if and only if they represent the
same version string.

equalsIgnoreOptional

```java
public boolean equalsIgnoreOptional​(
Object
obj)
```

Determines whether this

Version

is equal to another
disregarding optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

**Parameters:** obj

- The object to which this

Version

is to be compared
**Returns:** true

if, and only if, the given object is a

Version

that is identical to this

Version

ignoring the optional build information

---

#### equalsIgnoreOptional

public boolean equalsIgnoreOptional​(

Object

obj)

Determines whether this

Version

is equal to another
disregarding optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

Two

Version

s are equal if and only if they represent the
same version string disregarding the optional build information.

hashCode

```java
public int hashCode()
```

Returns the hash code of this version.

**Overrides:** hashCode

in class

Object
**Returns:** The hashcode of this version
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of this version.

---

