# Interface FlavorTable

**Source:** `java.datatransfer\java\awt\datatransfer\FlavorTable.html`

### Class Description

```java
public interface
FlavorTable

extends
FlavorMap
```

A FlavorMap which relaxes the traditional 1-to-1 restriction of a Map. A
flavor is permitted to map to any number of natives, and likewise a native is
permitted to map to any number of flavors. FlavorTables need not be
symmetric, but typically are.

**All Superinterfaces:** FlavorMap

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
String
> getNativesForFlavor​(
DataFlavor
flav)

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds. The

List

will be sorted from best
native to worst. That is, the first native will best reflect data in the
specified flavor to the underlying native platform. The returned

List

is a modifiable copy of this

FlavorTable

's internal
data. Client code is free to modify the

List

without affecting
this object.

**Parameters:**
- flav

- the

DataFlavor

whose corresponding natives should be
returned. If

null

is specified, all natives currently
known to this

FlavorTable

are returned in a
non-deterministic order.

**Returns:**
- a

java.util.List

of

java.lang.String

objects
which are platform-specific representations of platform-specific
data formats

---

#### List
<
DataFlavor
> getFlavorsForNative​(
String
nat)

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds. The

List

will be sorted from best

DataFlavor

to worst. That is, the first

DataFlavor

will
best reflect data in the specified native to a Java application. The
returned

List

is a modifiable copy of this

FlavorTable

's
internal data. Client code is free to modify the

List

without
affecting this object.

**Parameters:**
- nat

- the native whose corresponding

DataFlavor

s should be
returned. If

null

is specified, all

DataFlavor

s
currently known to this

FlavorTable

are returned in a
non-deterministic order.

**Returns:**
- a

java.util.List

of

DataFlavor

objects into which
platform-specific data in the specified, platform-specific native
can be translated

---

### Additional Sections

#### Interface FlavorTable

**All Superinterfaces:** FlavorMap

**All Known Implementing Classes:** SystemFlavorMap

```java
public interface
FlavorTable

extends
FlavorMap
```

A FlavorMap which relaxes the traditional 1-to-1 restriction of a Map. A
flavor is permitted to map to any number of natives, and likewise a native is
permitted to map to any number of flavors. FlavorTables need not be
symmetric, but typically are.

**Since:** 1.4

public interface

FlavorTable

extends

FlavorMap

A FlavorMap which relaxes the traditional 1-to-1 restriction of a Map. A
flavor is permitted to map to any number of natives, and likewise a native is
permitted to map to any number of flavors. FlavorTables need not be
symmetric, but typically are.

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

DataFlavor

>

getFlavorsForNative

​(

String

nat)

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds.

List

<

String

>

getNativesForFlavor

​(

DataFlavor

flav)

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds.

- Methods declared in interface java.awt.datatransfer.

FlavorMap

getFlavorsForNatives

,

getNativesForFlavors

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

DataFlavor

>

getFlavorsForNative

​(

String

nat)

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds.

List

<

String

>

getNativesForFlavor

​(

DataFlavor

flav)

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds.

- Methods declared in interface java.awt.datatransfer.

FlavorMap

getFlavorsForNatives

,

getNativesForFlavors

---

#### Method Summary

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds.

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds.

Methods declared in interface java.awt.datatransfer.

FlavorMap

getFlavorsForNatives

,

getNativesForFlavors

---

#### Methods declared in interface java.awt.datatransfer. FlavorMap

============ METHOD DETAIL ==========

- Method Detail

- getNativesForFlavor

```java
List
<
String
> getNativesForFlavor​(
DataFlavor
flav)
```

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds. The

List

will be sorted from best
native to worst. That is, the first native will best reflect data in the
specified flavor to the underlying native platform. The returned

List

is a modifiable copy of this

FlavorTable

's internal
data. Client code is free to modify the

List

without affecting
this object.

**Parameters:** flav

- the

DataFlavor

whose corresponding natives should be
returned. If

null

is specified, all natives currently
known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

java.lang.String

objects
which are platform-specific representations of platform-specific
data formats

- getFlavorsForNative

```java
List
<
DataFlavor
> getFlavorsForNative​(
String
nat)
```

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds. The

List

will be sorted from best

DataFlavor

to worst. That is, the first

DataFlavor

will
best reflect data in the specified native to a Java application. The
returned

List

is a modifiable copy of this

FlavorTable

's
internal data. Client code is free to modify the

List

without
affecting this object.

**Parameters:** nat

- the native whose corresponding

DataFlavor

s should be
returned. If

null

is specified, all

DataFlavor

s
currently known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

DataFlavor

objects into which
platform-specific data in the specified, platform-specific native
can be translated

Method Detail

- getNativesForFlavor

```java
List
<
String
> getNativesForFlavor​(
DataFlavor
flav)
```

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds. The

List

will be sorted from best
native to worst. That is, the first native will best reflect data in the
specified flavor to the underlying native platform. The returned

List

is a modifiable copy of this

FlavorTable

's internal
data. Client code is free to modify the

List

without affecting
this object.

**Parameters:** flav

- the

DataFlavor

whose corresponding natives should be
returned. If

null

is specified, all natives currently
known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

java.lang.String

objects
which are platform-specific representations of platform-specific
data formats

- getFlavorsForNative

```java
List
<
DataFlavor
> getFlavorsForNative​(
String
nat)
```

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds. The

List

will be sorted from best

DataFlavor

to worst. That is, the first

DataFlavor

will
best reflect data in the specified native to a Java application. The
returned

List

is a modifiable copy of this

FlavorTable

's
internal data. Client code is free to modify the

List

without
affecting this object.

**Parameters:** nat

- the native whose corresponding

DataFlavor

s should be
returned. If

null

is specified, all

DataFlavor

s
currently known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

DataFlavor

objects into which
platform-specific data in the specified, platform-specific native
can be translated

---

#### Method Detail

getNativesForFlavor

```java
List
<
String
> getNativesForFlavor​(
DataFlavor
flav)
```

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds. The

List

will be sorted from best
native to worst. That is, the first native will best reflect data in the
specified flavor to the underlying native platform. The returned

List

is a modifiable copy of this

FlavorTable

's internal
data. Client code is free to modify the

List

without affecting
this object.

**Parameters:** flav

- the

DataFlavor

whose corresponding natives should be
returned. If

null

is specified, all natives currently
known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

java.lang.String

objects
which are platform-specific representations of platform-specific
data formats

---

#### getNativesForFlavor

List

<

String

> getNativesForFlavor​(

DataFlavor

flav)

Returns a

List

of

String

natives to which the specified

DataFlavor

corresponds. The

List

will be sorted from best
native to worst. That is, the first native will best reflect data in the
specified flavor to the underlying native platform. The returned

List

is a modifiable copy of this

FlavorTable

's internal
data. Client code is free to modify the

List

without affecting
this object.

getFlavorsForNative

```java
List
<
DataFlavor
> getFlavorsForNative​(
String
nat)
```

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds. The

List

will be sorted from best

DataFlavor

to worst. That is, the first

DataFlavor

will
best reflect data in the specified native to a Java application. The
returned

List

is a modifiable copy of this

FlavorTable

's
internal data. Client code is free to modify the

List

without
affecting this object.

**Parameters:** nat

- the native whose corresponding

DataFlavor

s should be
returned. If

null

is specified, all

DataFlavor

s
currently known to this

FlavorTable

are returned in a
non-deterministic order.
**Returns:** a

java.util.List

of

DataFlavor

objects into which
platform-specific data in the specified, platform-specific native
can be translated

---

#### getFlavorsForNative

List

<

DataFlavor

> getFlavorsForNative​(

String

nat)

Returns a

List

of

DataFlavor

s to which the specified

String

corresponds. The

List

will be sorted from best

DataFlavor

to worst. That is, the first

DataFlavor

will
best reflect data in the specified native to a Java application. The
returned

List

is a modifiable copy of this

FlavorTable

's
internal data. Client code is free to modify the

List

without
affecting this object.

---

