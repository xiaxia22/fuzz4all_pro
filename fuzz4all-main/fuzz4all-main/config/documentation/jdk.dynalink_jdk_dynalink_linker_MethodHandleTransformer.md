# Interface MethodHandleTransformer

**Source:** `jdk.dynalink\jdk\dynalink\linker\MethodHandleTransformer.html`

### Class Description

```java
@FunctionalInterface

public interface
MethodHandleTransformer
```

A generic interface describing operations that transform method handles.
Typical usage is for implementing

internal objects filters

.

**All Known Implementing Classes:** DefaultInternalObjectFilter

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### MethodHandle
transform​(
MethodHandle
target)

Transforms a method handle.

**Parameters:**
- target

- the method handle being transformed.

**Returns:**
- transformed method handle.

---

### Additional Sections

#### Interface MethodHandleTransformer

**All Known Implementing Classes:** DefaultInternalObjectFilter

**Functional Interface:** This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

```java
@FunctionalInterface

public interface
MethodHandleTransformer
```

A generic interface describing operations that transform method handles.
Typical usage is for implementing

internal objects filters

.

@FunctionalInterface

public interface

MethodHandleTransformer

A generic interface describing operations that transform method handles.
Typical usage is for implementing

internal objects filters

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

transform

​(

MethodHandle

target)

Transforms a method handle.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

MethodHandle

transform

​(

MethodHandle

target)

Transforms a method handle.

---

#### Method Summary

Transforms a method handle.

============ METHOD DETAIL ==========

- Method Detail

- transform

```java
MethodHandle
transform​(
MethodHandle
target)
```

Transforms a method handle.

**Parameters:** target

- the method handle being transformed.
**Returns:** transformed method handle.

Method Detail

- transform

```java
MethodHandle
transform​(
MethodHandle
target)
```

Transforms a method handle.

**Parameters:** target

- the method handle being transformed.
**Returns:** transformed method handle.

---

#### Method Detail

transform

```java
MethodHandle
transform​(
MethodHandle
target)
```

Transforms a method handle.

**Parameters:** target

- the method handle being transformed.
**Returns:** transformed method handle.

---

#### transform

MethodHandle

transform​(

MethodHandle

target)

Transforms a method handle.

---

