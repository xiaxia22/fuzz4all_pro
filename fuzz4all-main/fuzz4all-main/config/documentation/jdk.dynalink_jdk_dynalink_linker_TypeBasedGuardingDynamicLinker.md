# Interface TypeBasedGuardingDynamicLinker

**Source:** `jdk.dynalink\jdk\dynalink\linker\TypeBasedGuardingDynamicLinker.html`

### Class Description

```java
public interface
TypeBasedGuardingDynamicLinker

extends
GuardingDynamicLinker
```

A guarding dynamic linker that can determine whether it can link the call site solely based on the type of the first
argument at linking invocation time. (The first argument is usually the receiver). Most language-specific
linkers will fall into this category, as they recognize their native objects as Java objects of classes implementing
a specific language-native interface or superclass. The linker mechanism can optimize the dispatch for these linkers,
see

CompositeTypeBasedGuardingDynamicLinker

.

**All Superinterfaces:** GuardingDynamicLinker

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean canLinkType​(
Class
<?> type)

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

**Parameters:**
- type

- the type to link

**Returns:**
- true if the linker can link calls for the receiver type, or false otherwise.

---

### Additional Sections

#### Interface TypeBasedGuardingDynamicLinker

**All Superinterfaces:** GuardingDynamicLinker

**All Known Implementing Classes:** CompositeTypeBasedGuardingDynamicLinker

```java
public interface
TypeBasedGuardingDynamicLinker

extends
GuardingDynamicLinker
```

A guarding dynamic linker that can determine whether it can link the call site solely based on the type of the first
argument at linking invocation time. (The first argument is usually the receiver). Most language-specific
linkers will fall into this category, as they recognize their native objects as Java objects of classes implementing
a specific language-native interface or superclass. The linker mechanism can optimize the dispatch for these linkers,
see

CompositeTypeBasedGuardingDynamicLinker

.

public interface

TypeBasedGuardingDynamicLinker

extends

GuardingDynamicLinker

A guarding dynamic linker that can determine whether it can link the call site solely based on the type of the first
argument at linking invocation time. (The first argument is usually the receiver). Most language-specific
linkers will fall into this category, as they recognize their native objects as Java objects of classes implementing
a specific language-native interface or superclass. The linker mechanism can optimize the dispatch for these linkers,
see

CompositeTypeBasedGuardingDynamicLinker

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

canLinkType

​(

Class

<?> type)

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

- Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

canLinkType

​(

Class

<?> type)

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

- Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

---

#### Method Summary

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

Methods declared in interface jdk.dynalink.linker.

GuardingDynamicLinker

getGuardedInvocation

---

#### Methods declared in interface jdk.dynalink.linker. GuardingDynamicLinker

============ METHOD DETAIL ==========

- Method Detail

- canLinkType

```java
boolean canLinkType​(
Class
<?> type)
```

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

**Parameters:** type

- the type to link
**Returns:** true if the linker can link calls for the receiver type, or false otherwise.

Method Detail

- canLinkType

```java
boolean canLinkType​(
Class
<?> type)
```

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

**Parameters:** type

- the type to link
**Returns:** true if the linker can link calls for the receiver type, or false otherwise.

---

#### Method Detail

canLinkType

```java
boolean canLinkType​(
Class
<?> type)
```

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

**Parameters:** type

- the type to link
**Returns:** true if the linker can link calls for the receiver type, or false otherwise.

---

#### canLinkType

boolean canLinkType​(

Class

<?> type)

Returns true if the linker can link an invocation where the first argument (receiver) is of the specified type.

---

