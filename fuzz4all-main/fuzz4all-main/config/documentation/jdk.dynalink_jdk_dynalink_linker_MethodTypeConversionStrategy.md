# Interface MethodTypeConversionStrategy

**Source:** `jdk.dynalink\jdk\dynalink\linker\MethodTypeConversionStrategy.html`

### Class Description

```java
@FunctionalInterface

public interface
MethodTypeConversionStrategy
```

Interface for objects representing a strategy for converting a method handle
to a new type. Typical usage is for customizing a language runtime's handling
of

method invocation conversions

.

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MethodHandle
asType​(
MethodHandle
target,

MethodType
newType)

Converts a method handle to a new type.

**Parameters:**
- target

- target method handle
- newType

- new type

**Returns:**
- target converted to the new type.

---

### Additional Sections

#### Interface MethodTypeConversionStrategy

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
MethodTypeConversionStrategy
```

Interface for objects representing a strategy for converting a method handle
to a new type. Typical usage is for customizing a language runtime's handling
of

method invocation conversions

.

@FunctionalInterface

public interface

MethodTypeConversionStrategy

Interface for objects representing a strategy for converting a method handle
to a new type. Typical usage is for customizing a language runtime's handling
of

method invocation conversions

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MethodHandle

asType

​(

MethodHandle

target,

MethodType

newType)

Converts a method handle to a new type.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MethodHandle

asType

​(

MethodHandle

target,

MethodType

newType)

Converts a method handle to a new type.

---

#### Method Summary

Converts a method handle to a new type.

============ METHOD DETAIL ==========

- Method Detail

- asType

```java
MethodHandle
asType​(
MethodHandle
target,

MethodType
newType)
```

Converts a method handle to a new type.

**Parameters:** target

- target method handle
**Parameters:** newType

- new type
**Returns:** target converted to the new type.

Method Detail

- asType

```java
MethodHandle
asType​(
MethodHandle
target,

MethodType
newType)
```

Converts a method handle to a new type.

**Parameters:** target

- target method handle
**Parameters:** newType

- new type
**Returns:** target converted to the new type.

---

#### Method Detail

asType

```java
MethodHandle
asType​(
MethodHandle
target,

MethodType
newType)
```

Converts a method handle to a new type.

**Parameters:** target

- target method handle
**Parameters:** newType

- new type
**Returns:** target converted to the new type.

---

#### asType

MethodHandle

asType​(

MethodHandle

target,

MethodType

newType)

Converts a method handle to a new type.

---

