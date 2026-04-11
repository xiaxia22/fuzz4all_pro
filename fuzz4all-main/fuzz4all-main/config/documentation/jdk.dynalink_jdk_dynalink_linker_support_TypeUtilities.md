# Class TypeUtilities

**Source:** `jdk.dynalink\jdk\dynalink\linker\support\TypeUtilities.html`

### Class Description

```java
public final class
TypeUtilities

extends
Object
```

Various static utility methods for working with Java types.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static boolean isMethodInvocationConvertible​(
Class
<?> sourceType,

Class
<?> targetType)

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion". This is basically all conversions allowed by subtyping (see

isSubtype(Class, Class)

) as well as boxing conversion (JLS 5.1.7) optionally followed by widening
reference conversion, and unboxing conversion (JLS 5.1.8) optionally followed by widening primitive conversion.

**Parameters:**
- sourceType

- the type being converted from (call site type for parameter types, method type for return types)
- targetType

- the parameter type being converted to (method type for parameter types, call site type for return types)

**Returns:**
- true if source type is method invocation convertible to target type.

---

#### public static boolean isConvertibleWithoutLoss​(
Class
<?> sourceType,

Class
<?> targetType)

Determines whether a type can be converted to another without losing any
precision. As a special case, void is considered convertible only to void
and

Object

(either as

null

or as a custom value set in

DynamicLinkerFactory.setAutoConversionStrategy(MethodTypeConversionStrategy)

).
Somewhat unintuitively, we consider anything to be convertible to void
even though converting to void causes the ultimate loss of data. On the
other hand, conversion to void essentially means that the value is of no
interest and should be discarded, thus there's no expectation of
preserving any precision.

**Parameters:**
- sourceType

- the source type
- targetType

- the target type

**Returns:**
- true if lossless conversion is possible

---

#### public static boolean isSubtype​(
Class
<?> subType,

Class
<?> superType)

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping". Note: this is not strict or proper subtype, therefore
true is also returned for identical types; to be completely precise, it
allows identity conversion (JLS 5.1.1), widening primitive conversion
(JLS 5.1.2) and widening reference conversion (JLS 5.1.5).

**Parameters:**
- subType

- the supposed subtype
- superType

- the supposed supertype of the subtype

**Returns:**
- true if subType can be converted by identity conversion, widening primitive conversion, or widening
reference conversion to superType.

---

#### public static
Class
<?> getPrimitiveTypeByName​(
String
name)

Given a name of a primitive type returns the class representing it. I.e.
when invoked with "int", returns

Integer.TYPE

.

**Parameters:**
- name

- the name of the primitive type

**Returns:**
- the class representing the primitive type, or null if the name
does not correspond to a primitive type.

---

#### public static
Class
<?> getPrimitiveType​(
Class
<?> wrapperType)

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type. I.e. calling it
with

Integer.class

will return

Integer.TYPE

. If passed a
class that is not a wrapper for primitive type, returns null.

**Parameters:**
- wrapperType

- the class object representing a wrapper for a
primitive type.

**Returns:**
- the class object representing the primitive type, or null if the
passed class is not a primitive wrapper.

---

#### public static
Class
<?> getWrapperType​(
Class
<?> primitiveType)

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type. I.e. calling it with

int.class

will return

Integer.class

. If passed a class
that is not a primitive type, returns null.

**Parameters:**
- primitiveType

- the class object representing a primitive type

**Returns:**
- the class object representing the wrapper type, or null if the passed class is not a primitive.

---

#### public static boolean isWrapperType​(
Class
<?> type)

Returns true if the passed type is a wrapper for a primitive type.

**Parameters:**
- type

- the examined type

**Returns:**
- true if the passed type is a wrapper for a primitive type.

---

### Additional Sections

#### Class TypeUtilities

java.lang.Object

- jdk.dynalink.linker.support.TypeUtilities

jdk.dynalink.linker.support.TypeUtilities

```java
public final class
TypeUtilities

extends
Object
```

Various static utility methods for working with Java types.

public final class

TypeUtilities

extends

Object

Various static utility methods for working with Java types.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Class

<?>

getPrimitiveType

​(

Class

<?> wrapperType)

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type.

static

Class

<?>

getPrimitiveTypeByName

​(

String

name)

Given a name of a primitive type returns the class representing it.

static

Class

<?>

getWrapperType

​(

Class

<?> primitiveType)

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type.

static boolean

isConvertibleWithoutLoss

​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether a type can be converted to another without losing any
precision.

static boolean

isMethodInvocationConvertible

​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion".

static boolean

isSubtype

​(

Class

<?> subType,

Class

<?> superType)

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping".

static boolean

isWrapperType

​(

Class

<?> type)

Returns true if the passed type is a wrapper for a primitive type.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Class

<?>

getPrimitiveType

​(

Class

<?> wrapperType)

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type.

static

Class

<?>

getPrimitiveTypeByName

​(

String

name)

Given a name of a primitive type returns the class representing it.

static

Class

<?>

getWrapperType

​(

Class

<?> primitiveType)

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type.

static boolean

isConvertibleWithoutLoss

​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether a type can be converted to another without losing any
precision.

static boolean

isMethodInvocationConvertible

​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion".

static boolean

isSubtype

​(

Class

<?> subType,

Class

<?> superType)

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping".

static boolean

isWrapperType

​(

Class

<?> type)

Returns true if the passed type is a wrapper for a primitive type.

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

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type.

Given a name of a primitive type returns the class representing it.

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type.

Determines whether a type can be converted to another without losing any
precision.

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion".

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping".

Returns true if the passed type is a wrapper for a primitive type.

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

- isMethodInvocationConvertible

```java
public static boolean isMethodInvocationConvertible​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion". This is basically all conversions allowed by subtyping (see

isSubtype(Class, Class)

) as well as boxing conversion (JLS 5.1.7) optionally followed by widening
reference conversion, and unboxing conversion (JLS 5.1.8) optionally followed by widening primitive conversion.

**Parameters:** sourceType

- the type being converted from (call site type for parameter types, method type for return types)
**Parameters:** targetType

- the parameter type being converted to (method type for parameter types, call site type for return types)
**Returns:** true if source type is method invocation convertible to target type.

- isConvertibleWithoutLoss

```java
public static boolean isConvertibleWithoutLoss​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether a type can be converted to another without losing any
precision. As a special case, void is considered convertible only to void
and

Object

(either as

null

or as a custom value set in

DynamicLinkerFactory.setAutoConversionStrategy(MethodTypeConversionStrategy)

).
Somewhat unintuitively, we consider anything to be convertible to void
even though converting to void causes the ultimate loss of data. On the
other hand, conversion to void essentially means that the value is of no
interest and should be discarded, thus there's no expectation of
preserving any precision.

**Parameters:** sourceType

- the source type
**Parameters:** targetType

- the target type
**Returns:** true if lossless conversion is possible

- isSubtype

```java
public static boolean isSubtype​(
Class
<?> subType,

Class
<?> superType)
```

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping". Note: this is not strict or proper subtype, therefore
true is also returned for identical types; to be completely precise, it
allows identity conversion (JLS 5.1.1), widening primitive conversion
(JLS 5.1.2) and widening reference conversion (JLS 5.1.5).

**Parameters:** subType

- the supposed subtype
**Parameters:** superType

- the supposed supertype of the subtype
**Returns:** true if subType can be converted by identity conversion, widening primitive conversion, or widening
reference conversion to superType.

- getPrimitiveTypeByName

```java
public static
Class
<?> getPrimitiveTypeByName​(
String
name)
```

Given a name of a primitive type returns the class representing it. I.e.
when invoked with "int", returns

Integer.TYPE

.

**Parameters:** name

- the name of the primitive type
**Returns:** the class representing the primitive type, or null if the name
does not correspond to a primitive type.

- getPrimitiveType

```java
public static
Class
<?> getPrimitiveType​(
Class
<?> wrapperType)
```

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type. I.e. calling it
with

Integer.class

will return

Integer.TYPE

. If passed a
class that is not a wrapper for primitive type, returns null.

**Parameters:** wrapperType

- the class object representing a wrapper for a
primitive type.
**Returns:** the class object representing the primitive type, or null if the
passed class is not a primitive wrapper.

- getWrapperType

```java
public static
Class
<?> getWrapperType​(
Class
<?> primitiveType)
```

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type. I.e. calling it with

int.class

will return

Integer.class

. If passed a class
that is not a primitive type, returns null.

**Parameters:** primitiveType

- the class object representing a primitive type
**Returns:** the class object representing the wrapper type, or null if the passed class is not a primitive.

- isWrapperType

```java
public static boolean isWrapperType​(
Class
<?> type)
```

Returns true if the passed type is a wrapper for a primitive type.

**Parameters:** type

- the examined type
**Returns:** true if the passed type is a wrapper for a primitive type.

Method Detail

- isMethodInvocationConvertible

```java
public static boolean isMethodInvocationConvertible​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion". This is basically all conversions allowed by subtyping (see

isSubtype(Class, Class)

) as well as boxing conversion (JLS 5.1.7) optionally followed by widening
reference conversion, and unboxing conversion (JLS 5.1.8) optionally followed by widening primitive conversion.

**Parameters:** sourceType

- the type being converted from (call site type for parameter types, method type for return types)
**Parameters:** targetType

- the parameter type being converted to (method type for parameter types, call site type for return types)
**Returns:** true if source type is method invocation convertible to target type.

- isConvertibleWithoutLoss

```java
public static boolean isConvertibleWithoutLoss​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether a type can be converted to another without losing any
precision. As a special case, void is considered convertible only to void
and

Object

(either as

null

or as a custom value set in

DynamicLinkerFactory.setAutoConversionStrategy(MethodTypeConversionStrategy)

).
Somewhat unintuitively, we consider anything to be convertible to void
even though converting to void causes the ultimate loss of data. On the
other hand, conversion to void essentially means that the value is of no
interest and should be discarded, thus there's no expectation of
preserving any precision.

**Parameters:** sourceType

- the source type
**Parameters:** targetType

- the target type
**Returns:** true if lossless conversion is possible

- isSubtype

```java
public static boolean isSubtype​(
Class
<?> subType,

Class
<?> superType)
```

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping". Note: this is not strict or proper subtype, therefore
true is also returned for identical types; to be completely precise, it
allows identity conversion (JLS 5.1.1), widening primitive conversion
(JLS 5.1.2) and widening reference conversion (JLS 5.1.5).

**Parameters:** subType

- the supposed subtype
**Parameters:** superType

- the supposed supertype of the subtype
**Returns:** true if subType can be converted by identity conversion, widening primitive conversion, or widening
reference conversion to superType.

- getPrimitiveTypeByName

```java
public static
Class
<?> getPrimitiveTypeByName​(
String
name)
```

Given a name of a primitive type returns the class representing it. I.e.
when invoked with "int", returns

Integer.TYPE

.

**Parameters:** name

- the name of the primitive type
**Returns:** the class representing the primitive type, or null if the name
does not correspond to a primitive type.

- getPrimitiveType

```java
public static
Class
<?> getPrimitiveType​(
Class
<?> wrapperType)
```

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type. I.e. calling it
with

Integer.class

will return

Integer.TYPE

. If passed a
class that is not a wrapper for primitive type, returns null.

**Parameters:** wrapperType

- the class object representing a wrapper for a
primitive type.
**Returns:** the class object representing the primitive type, or null if the
passed class is not a primitive wrapper.

- getWrapperType

```java
public static
Class
<?> getWrapperType​(
Class
<?> primitiveType)
```

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type. I.e. calling it with

int.class

will return

Integer.class

. If passed a class
that is not a primitive type, returns null.

**Parameters:** primitiveType

- the class object representing a primitive type
**Returns:** the class object representing the wrapper type, or null if the passed class is not a primitive.

- isWrapperType

```java
public static boolean isWrapperType​(
Class
<?> type)
```

Returns true if the passed type is a wrapper for a primitive type.

**Parameters:** type

- the examined type
**Returns:** true if the passed type is a wrapper for a primitive type.

---

#### Method Detail

isMethodInvocationConvertible

```java
public static boolean isMethodInvocationConvertible​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion". This is basically all conversions allowed by subtyping (see

isSubtype(Class, Class)

) as well as boxing conversion (JLS 5.1.7) optionally followed by widening
reference conversion, and unboxing conversion (JLS 5.1.8) optionally followed by widening primitive conversion.

**Parameters:** sourceType

- the type being converted from (call site type for parameter types, method type for return types)
**Parameters:** targetType

- the parameter type being converted to (method type for parameter types, call site type for return types)
**Returns:** true if source type is method invocation convertible to target type.

---

#### isMethodInvocationConvertible

public static boolean isMethodInvocationConvertible​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether one type can be converted to another type using a method invocation conversion, as per JLS 5.3
"Method Invocation Conversion". This is basically all conversions allowed by subtyping (see

isSubtype(Class, Class)

) as well as boxing conversion (JLS 5.1.7) optionally followed by widening
reference conversion, and unboxing conversion (JLS 5.1.8) optionally followed by widening primitive conversion.

isConvertibleWithoutLoss

```java
public static boolean isConvertibleWithoutLoss​(
Class
<?> sourceType,

Class
<?> targetType)
```

Determines whether a type can be converted to another without losing any
precision. As a special case, void is considered convertible only to void
and

Object

(either as

null

or as a custom value set in

DynamicLinkerFactory.setAutoConversionStrategy(MethodTypeConversionStrategy)

).
Somewhat unintuitively, we consider anything to be convertible to void
even though converting to void causes the ultimate loss of data. On the
other hand, conversion to void essentially means that the value is of no
interest and should be discarded, thus there's no expectation of
preserving any precision.

**Parameters:** sourceType

- the source type
**Parameters:** targetType

- the target type
**Returns:** true if lossless conversion is possible

---

#### isConvertibleWithoutLoss

public static boolean isConvertibleWithoutLoss​(

Class

<?> sourceType,

Class

<?> targetType)

Determines whether a type can be converted to another without losing any
precision. As a special case, void is considered convertible only to void
and

Object

(either as

null

or as a custom value set in

DynamicLinkerFactory.setAutoConversionStrategy(MethodTypeConversionStrategy)

).
Somewhat unintuitively, we consider anything to be convertible to void
even though converting to void causes the ultimate loss of data. On the
other hand, conversion to void essentially means that the value is of no
interest and should be discarded, thus there's no expectation of
preserving any precision.

isSubtype

```java
public static boolean isSubtype​(
Class
<?> subType,

Class
<?> superType)
```

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping". Note: this is not strict or proper subtype, therefore
true is also returned for identical types; to be completely precise, it
allows identity conversion (JLS 5.1.1), widening primitive conversion
(JLS 5.1.2) and widening reference conversion (JLS 5.1.5).

**Parameters:** subType

- the supposed subtype
**Parameters:** superType

- the supposed supertype of the subtype
**Returns:** true if subType can be converted by identity conversion, widening primitive conversion, or widening
reference conversion to superType.

---

#### isSubtype

public static boolean isSubtype​(

Class

<?> subType,

Class

<?> superType)

Determines whether one type is a subtype of another type, as per JLS
4.10 "Subtyping". Note: this is not strict or proper subtype, therefore
true is also returned for identical types; to be completely precise, it
allows identity conversion (JLS 5.1.1), widening primitive conversion
(JLS 5.1.2) and widening reference conversion (JLS 5.1.5).

getPrimitiveTypeByName

```java
public static
Class
<?> getPrimitiveTypeByName​(
String
name)
```

Given a name of a primitive type returns the class representing it. I.e.
when invoked with "int", returns

Integer.TYPE

.

**Parameters:** name

- the name of the primitive type
**Returns:** the class representing the primitive type, or null if the name
does not correspond to a primitive type.

---

#### getPrimitiveTypeByName

public static

Class

<?> getPrimitiveTypeByName​(

String

name)

Given a name of a primitive type returns the class representing it. I.e.
when invoked with "int", returns

Integer.TYPE

.

getPrimitiveType

```java
public static
Class
<?> getPrimitiveType​(
Class
<?> wrapperType)
```

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type. I.e. calling it
with

Integer.class

will return

Integer.TYPE

. If passed a
class that is not a wrapper for primitive type, returns null.

**Parameters:** wrapperType

- the class object representing a wrapper for a
primitive type.
**Returns:** the class object representing the primitive type, or null if the
passed class is not a primitive wrapper.

---

#### getPrimitiveType

public static

Class

<?> getPrimitiveType​(

Class

<?> wrapperType)

When passed a class representing a wrapper for a primitive type, returns
the class representing the corresponding primitive type. I.e. calling it
with

Integer.class

will return

Integer.TYPE

. If passed a
class that is not a wrapper for primitive type, returns null.

getWrapperType

```java
public static
Class
<?> getWrapperType​(
Class
<?> primitiveType)
```

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type. I.e. calling it with

int.class

will return

Integer.class

. If passed a class
that is not a primitive type, returns null.

**Parameters:** primitiveType

- the class object representing a primitive type
**Returns:** the class object representing the wrapper type, or null if the passed class is not a primitive.

---

#### getWrapperType

public static

Class

<?> getWrapperType​(

Class

<?> primitiveType)

When passed a class representing a primitive type, returns the class representing the corresponding
wrapper type. I.e. calling it with

int.class

will return

Integer.class

. If passed a class
that is not a primitive type, returns null.

isWrapperType

```java
public static boolean isWrapperType​(
Class
<?> type)
```

Returns true if the passed type is a wrapper for a primitive type.

**Parameters:** type

- the examined type
**Returns:** true if the passed type is a wrapper for a primitive type.

---

#### isWrapperType

public static boolean isWrapperType​(

Class

<?> type)

Returns true if the passed type is a wrapper for a primitive type.

---

