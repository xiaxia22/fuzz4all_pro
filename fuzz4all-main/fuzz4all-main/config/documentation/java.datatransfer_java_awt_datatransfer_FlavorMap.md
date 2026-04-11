# Interface FlavorMap

**Source:** `java.datatransfer\java\awt\datatransfer\FlavorMap.html`

### Class Description

```java
public interface
FlavorMap
```

A two-way Map between "natives" (Strings), which correspond to
platform-specific data formats, and "flavors" (DataFlavors), which correspond
to platform-independent MIME types. FlavorMaps need not be symmetric, but
typically are.

**All Known Subinterfaces:** FlavorTable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Map
<
DataFlavor
,​
String
> getNativesForFlavors​(
DataFlavor
[] flavors)

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:**
- flavors

- an array of

DataFlavor

s which will be the key set
of the returned

Map

. If

null

is specified, a
mapping of all

DataFlavor

s currently known to this

FlavorMap

to their corresponding

String

natives
will be returned.

**Returns:**
- a

java.util.Map

of

DataFlavor

s to

String

natives

---

#### Map
<
String
,​
DataFlavor
> getFlavorsForNatives​(
String
[] natives)

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:**
- natives

- an array of

String

s which will be the key set of
the returned

Map

. If

null

is specified, a mapping
of all

String

natives currently known to this

FlavorMap

to their corresponding

DataFlavor

s will
be returned.

**Returns:**
- a

java.util.Map

of

String

natives to

DataFlavor

s

---

### Additional Sections

#### Interface FlavorMap

**All Known Subinterfaces:** FlavorTable

**All Known Implementing Classes:** SystemFlavorMap

```java
public interface
FlavorMap
```

A two-way Map between "natives" (Strings), which correspond to
platform-specific data formats, and "flavors" (DataFlavors), which correspond
to platform-independent MIME types. FlavorMaps need not be symmetric, but
typically are.

**Since:** 1.2

public interface

FlavorMap

A two-way Map between "natives" (Strings), which correspond to
platform-specific data formats, and "flavors" (DataFlavors), which correspond
to platform-independent MIME types. FlavorMaps need not be symmetric, but
typically are.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map

<

String

,​

DataFlavor

>

getFlavorsForNatives

​(

String

[] natives)

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

.

Map

<

DataFlavor

,​

String

>

getNativesForFlavors

​(

DataFlavor

[] flavors)

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Map

<

String

,​

DataFlavor

>

getFlavorsForNatives

​(

String

[] natives)

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

.

Map

<

DataFlavor

,​

String

>

getNativesForFlavors

​(

DataFlavor

[] flavors)

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native.

---

#### Method Summary

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

.

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native.

============ METHOD DETAIL ==========

- Method Detail

- getNativesForFlavors

```java
Map
<
DataFlavor
,​
String
> getNativesForFlavors​(
DataFlavor
[] flavors)
```

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** flavors

- an array of

DataFlavor

s which will be the key set
of the returned

Map

. If

null

is specified, a
mapping of all

DataFlavor

s currently known to this

FlavorMap

to their corresponding

String

natives
will be returned.
**Returns:** a

java.util.Map

of

DataFlavor

s to

String

natives

- getFlavorsForNatives

```java
Map
<
String
,​
DataFlavor
> getFlavorsForNatives​(
String
[] natives)
```

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** natives

- an array of

String

s which will be the key set of
the returned

Map

. If

null

is specified, a mapping
of all

String

natives currently known to this

FlavorMap

to their corresponding

DataFlavor

s will
be returned.
**Returns:** a

java.util.Map

of

String

natives to

DataFlavor

s

Method Detail

- getNativesForFlavors

```java
Map
<
DataFlavor
,​
String
> getNativesForFlavors​(
DataFlavor
[] flavors)
```

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** flavors

- an array of

DataFlavor

s which will be the key set
of the returned

Map

. If

null

is specified, a
mapping of all

DataFlavor

s currently known to this

FlavorMap

to their corresponding

String

natives
will be returned.
**Returns:** a

java.util.Map

of

DataFlavor

s to

String

natives

- getFlavorsForNatives

```java
Map
<
String
,​
DataFlavor
> getFlavorsForNatives​(
String
[] natives)
```

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** natives

- an array of

String

s which will be the key set of
the returned

Map

. If

null

is specified, a mapping
of all

String

natives currently known to this

FlavorMap

to their corresponding

DataFlavor

s will
be returned.
**Returns:** a

java.util.Map

of

String

natives to

DataFlavor

s

---

#### Method Detail

getNativesForFlavors

```java
Map
<
DataFlavor
,​
String
> getNativesForFlavors​(
DataFlavor
[] flavors)
```

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** flavors

- an array of

DataFlavor

s which will be the key set
of the returned

Map

. If

null

is specified, a
mapping of all

DataFlavor

s currently known to this

FlavorMap

to their corresponding

String

natives
will be returned.
**Returns:** a

java.util.Map

of

DataFlavor

s to

String

natives

---

#### getNativesForFlavors

Map

<

DataFlavor

,​

String

> getNativesForFlavors​(

DataFlavor

[] flavors)

Returns a

Map

of the specified

DataFlavor

s to their
corresponding

String

native. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

getFlavorsForNatives

```java
Map
<
String
,​
DataFlavor
> getFlavorsForNatives​(
String
[] natives)
```

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

**Parameters:** natives

- an array of

String

s which will be the key set of
the returned

Map

. If

null

is specified, a mapping
of all

String

natives currently known to this

FlavorMap

to their corresponding

DataFlavor

s will
be returned.
**Returns:** a

java.util.Map

of

String

natives to

DataFlavor

s

---

#### getFlavorsForNatives

Map

<

String

,​

DataFlavor

> getFlavorsForNatives​(

String

[] natives)

Returns a

Map

of the specified

String

natives to their
corresponding

DataFlavor

. The returned

Map

is a
modifiable copy of this

FlavorMap

's internal data. Client code is
free to modify the

Map

without affecting this object.

---

