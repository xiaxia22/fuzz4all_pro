# Interface XPathVariableResolver

**Source:** `java.xml\javax\xml\xpath\XPathVariableResolver.html`

### Class Description

```java
public interface
XPathVariableResolver
```

XPathVariableResolver

provides access to the set of user defined XPath variables.

The

XPathVariableResolver

and the XPath evaluator must adhere to a contract that
cannot be directly enforced by the API. Although variables may be mutable,
that is, an application may wish to evaluate the same XPath expression more
than once with different variable values, in the course of evaluating any
single XPath expression, a variable's value

must

not change.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Object
resolveVariable​(
QName
variableName)

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

**Parameters:**
- variableName

- The

QName

of the variable name.

**Returns:**
- The variables value, or

null

if no variable named

variableName

exists. The value returned must be of a type appropriate for the underlying object model.

**Throws:**
- NullPointerException

- If

variableName

is

null

.

---

### Additional Sections

#### Interface XPathVariableResolver

```java
public interface
XPathVariableResolver
```

XPathVariableResolver

provides access to the set of user defined XPath variables.

The

XPathVariableResolver

and the XPath evaluator must adhere to a contract that
cannot be directly enforced by the API. Although variables may be mutable,
that is, an application may wish to evaluate the same XPath expression more
than once with different variable values, in the course of evaluating any
single XPath expression, a variable's value

must

not change.

**Since:** 1.5

public interface

XPathVariableResolver

XPathVariableResolver

provides access to the set of user defined XPath variables.

The

XPathVariableResolver

and the XPath evaluator must adhere to a contract that
cannot be directly enforced by the API. Although variables may be mutable,
that is, an application may wish to evaluate the same XPath expression more
than once with different variable values, in the course of evaluating any
single XPath expression, a variable's value

must

not change.

XPathVariableResolver

provides access to the set of user defined XPath variables.

The

XPathVariableResolver

and the XPath evaluator must adhere to a contract that
cannot be directly enforced by the API. Although variables may be mutable,
that is, an application may wish to evaluate the same XPath expression more
than once with different variable values, in the course of evaluating any
single XPath expression, a variable's value

must

not change.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

resolveVariable

​(

QName

variableName)

Find a variable in the set of available variables.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Object

resolveVariable

​(

QName

variableName)

Find a variable in the set of available variables.

---

#### Method Summary

Find a variable in the set of available variables.

============ METHOD DETAIL ==========

- Method Detail

- resolveVariable

```java
Object
resolveVariable​(
QName
variableName)
```

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

**Parameters:** variableName

- The

QName

of the variable name.
**Returns:** The variables value, or

null

if no variable named

variableName

exists. The value returned must be of a type appropriate for the underlying object model.
**Throws:** NullPointerException

- If

variableName

is

null

.

Method Detail

- resolveVariable

```java
Object
resolveVariable​(
QName
variableName)
```

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

**Parameters:** variableName

- The

QName

of the variable name.
**Returns:** The variables value, or

null

if no variable named

variableName

exists. The value returned must be of a type appropriate for the underlying object model.
**Throws:** NullPointerException

- If

variableName

is

null

.

---

#### Method Detail

resolveVariable

```java
Object
resolveVariable​(
QName
variableName)
```

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

**Parameters:** variableName

- The

QName

of the variable name.
**Returns:** The variables value, or

null

if no variable named

variableName

exists. The value returned must be of a type appropriate for the underlying object model.
**Throws:** NullPointerException

- If

variableName

is

null

.

---

#### resolveVariable

Object

resolveVariable​(

QName

variableName)

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

Find a variable in the set of available variables.

If

variableName

is

null

, then a

NullPointerException

is thrown.

---

