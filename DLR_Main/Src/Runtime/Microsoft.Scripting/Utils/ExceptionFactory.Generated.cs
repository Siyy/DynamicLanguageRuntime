/* ****************************************************************************
 *
 * Copyright (c) Microsoft Corporation. 
 *
 * This source code is subject to terms and conditions of the Microsoft Public License. A 
 * copy of the license can be found in the License.html file at the root of this distribution. If 
 * you cannot locate the  Microsoft Public License, please send an email to 
 * dlr@microsoft.com. By using this source code in any fashion, you are agreeing to be bound 
 * by the terms of the Microsoft Public License.
 *
 * You must not remove this notice, or any other, from this software.
 *
 *
 * ***************************************************************************/

#if CODEPLEX_40
using System;
#else
using System; using Microsoft;
#endif

namespace Microsoft.Scripting {

    internal static partial class Strings {
        private static string FormatString(string format, params object[] args) {
            return string.Format(System.Globalization.CultureInfo.CurrentCulture, format, args);
        }
    }

    #region Generated Microsoft.Scripting Exception Factory

    // *** BEGIN GENERATED CODE ***
    // generated by function: gen_expr_factory_scripting from: generate_exception_factory.py

    /// <summary>
    ///    Strongly-typed and parameterized string factory.
    /// </summary>

    internal static partial class Strings {
        /// <summary>
        /// A string like  "Cannot access member {1} declared on type {0} because the type contains generic parameters."
        /// </summary>
        internal static string InvalidOperation_ContainsGenericParameters(object p0, object p1) {
            return FormatString("Cannot access member {1} declared on type {0} because the type contains generic parameters.", p0, p1);
        }

        /// <summary>
        /// A string like  "Type '{0}' is missing or cannot be loaded."
        /// </summary>
        internal static string MissingType(object p0) {
            return FormatString("Type '{0}' is missing or cannot be loaded.", p0);
        }

        /// <summary>
        /// A string like  "static property "{0}" of "{1}" can only be read through a type, not an instance"
        /// </summary>
        internal static string StaticAccessFromInstanceError(object p0, object p1) {
            return FormatString("static property \"{0}\" of \"{1}\" can only be read through a type, not an instance", p0, p1);
        }

        /// <summary>
        /// A string like  "static property "{0}" of "{1}" can only be assigned to through a type, not an instance"
        /// </summary>
        internal static string StaticAssignmentFromInstanceError(object p0, object p1) {
            return FormatString("static property \"{0}\" of \"{1}\" can only be assigned to through a type, not an instance", p0, p1);
        }

        /// <summary>
        /// A string like  "Method precondition violated"
        /// </summary>
        internal static string MethodPreconditionViolated {
            get {
                return "Method precondition violated";
            }
        }

        /// <summary>
        /// A string like  "Invalid argument value"
        /// </summary>
        internal static string InvalidArgumentValue {
            get {
                return "Invalid argument value";
            }
        }

        /// <summary>
        /// A string like  "Non-empty string required"
        /// </summary>
        internal static string NonEmptyStringRequired {
            get {
                return "Non-empty string required";
            }
        }

        /// <summary>
        /// A string like  "Non-empty collection required"
        /// </summary>
        internal static string NonEmptyCollectionRequired {
            get {
                return "Non-empty collection required";
            }
        }

        /// <summary>
        /// A string like  "must by an Exception instance"
        /// </summary>
        internal static string MustBeExceptionInstance {
            get {
                return "must by an Exception instance";
            }
        }

        /// <summary>
        /// A string like  "Type of test must be bool"
        /// </summary>
        internal static string TypeOfTestMustBeBool {
            get {
                return "Type of test must be bool";
            }
        }

        /// <summary>
        /// A string like  "Type of the expression must be bool"
        /// </summary>
        internal static string TypeOfExpressionMustBeBool {
            get {
                return "Type of the expression must be bool";
            }
        }

        /// <summary>
        /// A string like  "Empty string is not a valid path."
        /// </summary>
        internal static string EmptyStringIsInvalidPath {
            get {
                return "Empty string is not a valid path.";
            }
        }

        /// <summary>
        /// A string like  "Invalid delegate type (Invoke method not found)."
        /// </summary>
        internal static string InvalidDelegate {
            get {
                return "Invalid delegate type (Invoke method not found).";
            }
        }

        /// <summary>
        /// A string like  "expected only static property"
        /// </summary>
        internal static string ExpectedStaticProperty {
            get {
                return "expected only static property";
            }
        }

        /// <summary>
        /// A string like  "Property doesn't exist on the provided type"
        /// </summary>
        internal static string PropertyDoesNotExist {
            get {
                return "Property doesn't exist on the provided type";
            }
        }

        /// <summary>
        /// A string like  "Field doesn't exist on provided type"
        /// </summary>
        internal static string FieldDoesNotExist {
            get {
                return "Field doesn't exist on provided type";
            }
        }

        /// <summary>
        /// A string like  "Type doesn't have constructor with a given signature"
        /// </summary>
        internal static string TypeDoesNotHaveConstructorForTheSignature {
            get {
                return "Type doesn't have constructor with a given signature";
            }
        }

        /// <summary>
        /// A string like  "Type doesn't have a method with a given name."
        /// </summary>
        internal static string TypeDoesNotHaveMethodForName {
            get {
                return "Type doesn't have a method with a given name.";
            }
        }

        /// <summary>
        /// A string like  "Type doesn't have a method with a given name and signature."
        /// </summary>
        internal static string TypeDoesNotHaveMethodForNameSignature {
            get {
                return "Type doesn't have a method with a given name and signature.";
            }
        }

        /// <summary>
        /// A string like  "Count must be non-negative."
        /// </summary>
        internal static string CountCannotBeNegative {
            get {
                return "Count must be non-negative.";
            }
        }

        /// <summary>
        /// A string like  "arrayType must be an array type"
        /// </summary>
        internal static string ArrayTypeMustBeArray {
            get {
                return "arrayType must be an array type";
            }
        }

        /// <summary>
        /// A string like  "Either code or target must be specified."
        /// </summary>
        internal static string MustHaveCodeOrTarget {
            get {
                return "Either code or target must be specified.";
            }
        }

        /// <summary>
        /// A string like  "Type parameter is {0}. Expected a delegate."
        /// </summary>
        internal static string TypeParameterIsNotDelegate(object p0) {
            return FormatString("Type parameter is {0}. Expected a delegate.", p0);
        }

        /// <summary>
        /// A string like  "Cannot cast from type '{0}' to type '{1}"
        /// </summary>
        internal static string InvalidCast(object p0, object p1) {
            return FormatString("Cannot cast from type '{0}' to type '{1}", p0, p1);
        }

        /// <summary>
        /// A string like  "unknown member type: '{0}'. "
        /// </summary>
        internal static string UnknownMemberType(object p0) {
            return FormatString("unknown member type: '{0}'. ", p0);
        }

        /// <summary>
        /// A string like  "RuleBuilder can only be used with delegates whose first argument is CallSite."
        /// </summary>
        internal static string FirstArgumentMustBeCallSite {
            get {
                return "RuleBuilder can only be used with delegates whose first argument is CallSite.";
            }
        }

        /// <summary>
        /// A string like  "no instance for call."
        /// </summary>
        internal static string NoInstanceForCall {
            get {
                return "no instance for call.";
            }
        }

        /// <summary>
        /// A string like  "Missing Test."
        /// </summary>
        internal static string MissingTest {
            get {
                return "Missing Test.";
            }
        }

        /// <summary>
        /// A string like  "Missing Target."
        /// </summary>
        internal static string MissingTarget {
            get {
                return "Missing Target.";
            }
        }

        /// <summary>
        /// A string like  "The operation requires a non-generic type for {0}, but this represents generic types only"
        /// </summary>
        internal static string NonGenericWithGenericGroup(object p0) {
            return FormatString("The operation requires a non-generic type for {0}, but this represents generic types only", p0);
        }

        /// <summary>
        /// A string like  "Invalid operation: '{0}'"
        /// </summary>
        internal static string InvalidOperation(object p0) {
            return FormatString("Invalid operation: '{0}'", p0);
        }

        /// <summary>
        /// A string like  "Finally already defined."
        /// </summary>
        internal static string FinallyAlreadyDefined {
            get {
                return "Finally already defined.";
            }
        }

        /// <summary>
        /// A string like  "Can not have fault and finally."
        /// </summary>
        internal static string CannotHaveFaultAndFinally {
            get {
                return "Can not have fault and finally.";
            }
        }

        /// <summary>
        /// A string like  "Fault already defined."
        /// </summary>
        internal static string FaultAlreadyDefined {
            get {
                return "Fault already defined.";
            }
        }

        /// <summary>
        /// A string like  "Cannot create default value for type {0}."
        /// </summary>
        internal static string CantCreateDefaultTypeFor(object p0) {
            return FormatString("Cannot create default value for type {0}.", p0);
        }

        /// <summary>
        /// A string like  "Unhandled convert: {0}"
        /// </summary>
        internal static string UnhandledConvert(object p0) {
            return FormatString("Unhandled convert: {0}", p0);
        }

        /// <summary>
        /// A string like  "{0}.{1} has no publiclly visible method."
        /// </summary>
        internal static string NoCallableMethods(object p0, object p1) {
            return FormatString("{0}.{1} has no publiclly visible method.", p0, p1);
        }

        /// <summary>
        /// A string like  "Global/top-level local variable names must be unique."
        /// </summary>
        internal static string GlobalsMustBeUnique {
            get {
                return "Global/top-level local variable names must be unique.";
            }
        }

        /// <summary>
        /// A string like  "Generating code from non-serializable CallSiteBinder."
        /// </summary>
        internal static string GenNonSerializableBinder {
            get {
                return "Generating code from non-serializable CallSiteBinder.";
            }
        }

        /// <summary>
        /// A string like  "pecified path is invalid."
        /// </summary>
        internal static string InvalidPath {
            get {
                return "pecified path is invalid.";
            }
        }

        /// <summary>
        /// A string like  "Dictionaries are not hashable."
        /// </summary>
        internal static string DictionaryNotHashable {
            get {
                return "Dictionaries are not hashable.";
            }
        }

        /// <summary>
        /// A string like  "language already registered."
        /// </summary>
        internal static string LanguageRegistered {
            get {
                return "language already registered.";
            }
        }

        /// <summary>
        /// A string like  "The method or operation is not implemented."
        /// </summary>
        internal static string MethodOrOperatorNotImplemented {
            get {
                return "The method or operation is not implemented.";
            }
        }

        /// <summary>
        /// A string like  "No exception."
        /// </summary>
        internal static string NoException {
            get {
                return "No exception.";
            }
        }

        /// <summary>
        /// A string like  "Extension type {0} must be public."
        /// </summary>
        internal static string ExtensionMustBePublic(object p0) {
            return FormatString("Extension type {0} must be public.", p0);
        }

        /// <summary>
        /// A string like  "Already initialized."
        /// </summary>
        internal static string AlreadyInitialized {
            get {
                return "Already initialized.";
            }
        }

        /// <summary>
        /// A string like  "CreateScopeExtension must return a scope extension."
        /// </summary>
        internal static string MustReturnScopeExtension {
            get {
                return "CreateScopeExtension must return a scope extension.";
            }
        }

        /// <summary>
        /// A string like  "Invalid number of parameters for the service."
        /// </summary>
        internal static string InvalidParamNumForService {
            get {
                return "Invalid number of parameters for the service.";
            }
        }

        /// <summary>
        /// A string like  "Invalid type of argument {0}; expecting {1}."
        /// </summary>
        internal static string InvalidArgumentType(object p0, object p1) {
            return FormatString("Invalid type of argument {0}; expecting {1}.", p0, p1);
        }

        /// <summary>
        /// A string like  "Cannot change non-caching value."
        /// </summary>
        internal static string CannotChangeNonCachingValue {
            get {
                return "Cannot change non-caching value.";
            }
        }

        /// <summary>
        /// A string like  "Local variable '{0}' referenced before assignment."
        /// </summary>
        internal static string ReferencedBeforeAssignment(object p0) {
            return FormatString("Local variable '{0}' referenced before assignment.", p0);
        }

        /// <summary>
        /// A string like  "Field {0} is read-only"
        /// </summary>
        internal static string FieldReadonly(object p0) {
            return FormatString("Field {0} is read-only", p0);
        }

        /// <summary>
        /// A string like  "Property {0} is read-only"
        /// </summary>
        internal static string PropertyReadonly(object p0) {
            return FormatString("Property {0} is read-only", p0);
        }

        /// <summary>
        /// A string like  "Expected event from {0}.{1}, got event from {2}.{3}."
        /// </summary>
        internal static string UnexpectedEvent(object p0, object p1, object p2, object p3) {
            return FormatString("Expected event from {0}.{1}, got event from {2}.{3}.", p0, p1, p2, p3);
        }

        /// <summary>
        /// A string like  "expected bound event, got {0}."
        /// </summary>
        internal static string ExpectedBoundEvent(object p0) {
            return FormatString("expected bound event, got {0}.", p0);
        }

        /// <summary>
        /// A string like  "Expected type {0}, got {1}."
        /// </summary>
        internal static string UnexpectedType(object p0, object p1) {
            return FormatString("Expected type {0}, got {1}.", p0, p1);
        }

        /// <summary>
        /// A string like  "can only write to member {0}."
        /// </summary>
        internal static string MemberWriteOnly(object p0) {
            return FormatString("can only write to member {0}.", p0);
        }

        /// <summary>
        /// A string like  "No code to compile."
        /// </summary>
        internal static string NoCodeToCompile {
            get {
                return "No code to compile.";
            }
        }

        /// <summary>
        /// A string like  "Invalid stream type: {0}."
        /// </summary>
        internal static string InvalidStreamType(object p0) {
            return FormatString("Invalid stream type: {0}.", p0);
        }

        /// <summary>
        /// A string like  "Queue empty."
        /// </summary>
        internal static string QueueEmpty {
            get {
                return "Queue empty.";
            }
        }

        /// <summary>
        /// A string like  "Enumeration has not started. Call MoveNext."
        /// </summary>
        internal static string EnumerationNotStarted {
            get {
                return "Enumeration has not started. Call MoveNext.";
            }
        }

        /// <summary>
        /// A string like  "Enumeration already finished."
        /// </summary>
        internal static string EnumerationFinished {
            get {
                return "Enumeration already finished.";
            }
        }

        /// <summary>
        /// A string like  "can't add another casing for identifier {0}"
        /// </summary>
        internal static string CantAddCasing(object p0) {
            return FormatString("can't add another casing for identifier {0}", p0);
        }

        /// <summary>
        /// A string like  "can't add new identifier {0}"
        /// </summary>
        internal static string CantAddIdentifier(object p0) {
            return FormatString("can't add new identifier {0}", p0);
        }

        /// <summary>
        /// A string like  "Type '{0}' doesn't provide a suitable public constructor or its implementation is faulty: {1}"
        /// </summary>
        internal static string InvalidCtorImplementation(object p0, object p1) {
            return FormatString("Type '{0}' doesn't provide a suitable public constructor or its implementation is faulty: {1}", p0, p1);
        }

        /// <summary>
        /// A string like  "Invalid output directory."
        /// </summary>
        internal static string InvalidOutputDir {
            get {
                return "Invalid output directory.";
            }
        }

        /// <summary>
        /// A string like  "Invalid assembly name or file extension."
        /// </summary>
        internal static string InvalidAsmNameOrExtension {
            get {
                return "Invalid assembly name or file extension.";
            }
        }

        /// <summary>
        /// A string like  "Cannot emit constant {0} ({1})"
        /// </summary>
        internal static string CanotEmitConstant(object p0, object p1) {
            return FormatString("Cannot emit constant {0} ({1})", p0, p1);
        }

        /// <summary>
        /// A string like  "No implicit cast from {0} to {1}"
        /// </summary>
        internal static string NoImplicitCast(object p0, object p1) {
            return FormatString("No implicit cast from {0} to {1}", p0, p1);
        }

        /// <summary>
        /// A string like  "No explicit cast from {0} to {1}"
        /// </summary>
        internal static string NoExplicitCast(object p0, object p1) {
            return FormatString("No explicit cast from {0} to {1}", p0, p1);
        }

        /// <summary>
        /// A string like  "name '{0}' not defined"
        /// </summary>
        internal static string NameNotDefined(object p0) {
            return FormatString("name '{0}' not defined", p0);
        }

        /// <summary>
        /// A string like  "No default value for a given type."
        /// </summary>
        internal static string NoDefaultValue {
            get {
                return "No default value for a given type.";
            }
        }

        /// <summary>
        /// A string like  "Specified language provider type is not registered."
        /// </summary>
        internal static string UnknownLanguageProviderType {
            get {
                return "Specified language provider type is not registered.";
            }
        }

        /// <summary>
        /// A string like  "can't read from property"
        /// </summary>
        internal static string CantReadProperty {
            get {
                return "can't read from property";
            }
        }

        /// <summary>
        /// A string like  "can't write to property"
        /// </summary>
        internal static string CantWriteProperty {
            get {
                return "can't write to property";
            }
        }

        /// <summary>
        /// A string like  "Cannot create instance of {0} because it contains generic parameters"
        /// </summary>
        internal static string IllegalNew_GenericParams(object p0) {
            return FormatString("Cannot create instance of {0} because it contains generic parameters", p0);
        }

        /// <summary>
        /// A string like  "Non-verifiable assembly generated: {0}:\nAssembly preserved as {1}\nError text:\n{2}\n"
        /// </summary>
        internal static string VerificationException(object p0, object p1, object p2) {
            return FormatString("Non-verifiable assembly generated: {0}:\nAssembly preserved as {1}\nError text:\n{2}\n", p0, p1, p2);
        }

    }
    /// <summary>
    ///    Strongly-typed and parameterized exception factory.
    /// </summary>

    internal static partial class Error {
        /// <summary>
        /// ArgumentException with message like "Either code or target must be specified."
        /// </summary>
        internal static Exception MustHaveCodeOrTarget() {
            return new ArgumentException(Strings.MustHaveCodeOrTarget);
        }

        /// <summary>
        /// InvalidOperationException with message like "Type parameter is {0}. Expected a delegate."
        /// </summary>
        internal static Exception TypeParameterIsNotDelegate(object p0) {
            return new InvalidOperationException(Strings.TypeParameterIsNotDelegate(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "Cannot cast from type '{0}' to type '{1}"
        /// </summary>
        internal static Exception InvalidCast(object p0, object p1) {
            return new InvalidOperationException(Strings.InvalidCast(p0, p1));
        }

        /// <summary>
        /// InvalidOperationException with message like "unknown member type: '{0}'. "
        /// </summary>
        internal static Exception UnknownMemberType(object p0) {
            return new InvalidOperationException(Strings.UnknownMemberType(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "RuleBuilder can only be used with delegates whose first argument is CallSite."
        /// </summary>
        internal static Exception FirstArgumentMustBeCallSite() {
            return new InvalidOperationException(Strings.FirstArgumentMustBeCallSite);
        }

        /// <summary>
        /// InvalidOperationException with message like "no instance for call."
        /// </summary>
        internal static Exception NoInstanceForCall() {
            return new InvalidOperationException(Strings.NoInstanceForCall);
        }

        /// <summary>
        /// InvalidOperationException with message like "Missing Test."
        /// </summary>
        internal static Exception MissingTest() {
            return new InvalidOperationException(Strings.MissingTest);
        }

        /// <summary>
        /// InvalidOperationException with message like "Missing Target."
        /// </summary>
        internal static Exception MissingTarget() {
            return new InvalidOperationException(Strings.MissingTarget);
        }

        /// <summary>
        /// TypeLoadException with message like "The operation requires a non-generic type for {0}, but this represents generic types only"
        /// </summary>
        internal static Exception NonGenericWithGenericGroup(object p0) {
            return new TypeLoadException(Strings.NonGenericWithGenericGroup(p0));
        }

        /// <summary>
        /// ArgumentException with message like "Invalid operation: '{0}'"
        /// </summary>
        internal static Exception InvalidOperation(object p0) {
            return new ArgumentException(Strings.InvalidOperation(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "Finally already defined."
        /// </summary>
        internal static Exception FinallyAlreadyDefined() {
            return new InvalidOperationException(Strings.FinallyAlreadyDefined);
        }

        /// <summary>
        /// InvalidOperationException with message like "Can not have fault and finally."
        /// </summary>
        internal static Exception CannotHaveFaultAndFinally() {
            return new InvalidOperationException(Strings.CannotHaveFaultAndFinally);
        }

        /// <summary>
        /// InvalidOperationException with message like "Fault already defined."
        /// </summary>
        internal static Exception FaultAlreadyDefined() {
            return new InvalidOperationException(Strings.FaultAlreadyDefined);
        }

        /// <summary>
        /// ArgumentException with message like "Cannot create default value for type {0}."
        /// </summary>
        internal static Exception CantCreateDefaultTypeFor(object p0) {
            return new ArgumentException(Strings.CantCreateDefaultTypeFor(p0));
        }

        /// <summary>
        /// ArgumentException with message like "Unhandled convert: {0}"
        /// </summary>
        internal static Exception UnhandledConvert(object p0) {
            return new ArgumentException(Strings.UnhandledConvert(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "{0}.{1} has no publiclly visible method."
        /// </summary>
        internal static Exception NoCallableMethods(object p0, object p1) {
            return new InvalidOperationException(Strings.NoCallableMethods(p0, p1));
        }

        /// <summary>
        /// ArgumentException with message like "Global/top-level local variable names must be unique."
        /// </summary>
        internal static Exception GlobalsMustBeUnique() {
            return new ArgumentException(Strings.GlobalsMustBeUnique);
        }

        /// <summary>
        /// ArgumentException with message like "Generating code from non-serializable CallSiteBinder."
        /// </summary>
        internal static Exception GenNonSerializableBinder() {
            return new ArgumentException(Strings.GenNonSerializableBinder);
        }

        /// <summary>
        /// ArgumentException with message like "pecified path is invalid."
        /// </summary>
        internal static Exception InvalidPath() {
            return new ArgumentException(Strings.InvalidPath);
        }

        /// <summary>
        /// ArgumentTypeException with message like "Dictionaries are not hashable."
        /// </summary>
        internal static Exception DictionaryNotHashable() {
            return new ArgumentTypeException(Strings.DictionaryNotHashable);
        }

        /// <summary>
        /// InvalidOperationException with message like "language already registered."
        /// </summary>
        internal static Exception LanguageRegistered() {
            return new InvalidOperationException(Strings.LanguageRegistered);
        }

        /// <summary>
        /// NotImplementedException with message like "The method or operation is not implemented."
        /// </summary>
        internal static Exception MethodOrOperatorNotImplemented() {
            return new NotImplementedException(Strings.MethodOrOperatorNotImplemented);
        }

        /// <summary>
        /// InvalidOperationException with message like "No exception."
        /// </summary>
        internal static Exception NoException() {
            return new InvalidOperationException(Strings.NoException);
        }

        /// <summary>
        /// ArgumentException with message like "Extension type {0} must be public."
        /// </summary>
        internal static Exception ExtensionMustBePublic(object p0) {
            return new ArgumentException(Strings.ExtensionMustBePublic(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "Already initialized."
        /// </summary>
        internal static Exception AlreadyInitialized() {
            return new InvalidOperationException(Strings.AlreadyInitialized);
        }

        /// <summary>
        /// InvalidImplementationException with message like "CreateScopeExtension must return a scope extension."
        /// </summary>
        internal static Exception MustReturnScopeExtension() {
            return new InvalidImplementationException(Strings.MustReturnScopeExtension);
        }

        /// <summary>
        /// ArgumentException with message like "Invalid number of parameters for the service."
        /// </summary>
        internal static Exception InvalidParamNumForService() {
            return new ArgumentException(Strings.InvalidParamNumForService);
        }

        /// <summary>
        /// ArgumentException with message like "Invalid type of argument {0}; expecting {1}."
        /// </summary>
        internal static Exception InvalidArgumentType(object p0, object p1) {
            return new ArgumentException(Strings.InvalidArgumentType(p0, p1));
        }

        /// <summary>
        /// ArgumentException with message like "Cannot change non-caching value."
        /// </summary>
        internal static Exception CannotChangeNonCachingValue() {
            return new ArgumentException(Strings.CannotChangeNonCachingValue);
        }

        /// <summary>
        /// Microsoft.Scripting.Runtime.UnboundLocalException with message like "Local variable '{0}' referenced before assignment."
        /// </summary>
        internal static Exception ReferencedBeforeAssignment(object p0) {
            return new Microsoft.Scripting.Runtime.UnboundLocalException(Strings.ReferencedBeforeAssignment(p0));
        }

        /// <summary>
        /// MissingMemberException with message like "Field {0} is read-only"
        /// </summary>
        internal static Exception FieldReadonly(object p0) {
            return new MissingMemberException(Strings.FieldReadonly(p0));
        }

        /// <summary>
        /// MissingMemberException with message like "Property {0} is read-only"
        /// </summary>
        internal static Exception PropertyReadonly(object p0) {
            return new MissingMemberException(Strings.PropertyReadonly(p0));
        }

        /// <summary>
        /// ArgumentException with message like "Expected event from {0}.{1}, got event from {2}.{3}."
        /// </summary>
        internal static Exception UnexpectedEvent(object p0, object p1, object p2, object p3) {
            return new ArgumentException(Strings.UnexpectedEvent(p0, p1, p2, p3));
        }

        /// <summary>
        /// ArgumentTypeException with message like "expected bound event, got {0}."
        /// </summary>
        internal static Exception ExpectedBoundEvent(object p0) {
            return new ArgumentTypeException(Strings.ExpectedBoundEvent(p0));
        }

        /// <summary>
        /// ArgumentTypeException with message like "Expected type {0}, got {1}."
        /// </summary>
        internal static Exception UnexpectedType(object p0, object p1) {
            return new ArgumentTypeException(Strings.UnexpectedType(p0, p1));
        }

        /// <summary>
        /// MemberAccessException with message like "can only write to member {0}."
        /// </summary>
        internal static Exception MemberWriteOnly(object p0) {
            return new MemberAccessException(Strings.MemberWriteOnly(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "No code to compile."
        /// </summary>
        internal static Exception NoCodeToCompile() {
            return new InvalidOperationException(Strings.NoCodeToCompile);
        }

        /// <summary>
        /// ArgumentException with message like "Invalid stream type: {0}."
        /// </summary>
        internal static Exception InvalidStreamType(object p0) {
            return new ArgumentException(Strings.InvalidStreamType(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "Queue empty."
        /// </summary>
        internal static Exception QueueEmpty() {
            return new InvalidOperationException(Strings.QueueEmpty);
        }

        /// <summary>
        /// InvalidOperationException with message like "Enumeration has not started. Call MoveNext."
        /// </summary>
        internal static Exception EnumerationNotStarted() {
            return new InvalidOperationException(Strings.EnumerationNotStarted);
        }

        /// <summary>
        /// InvalidOperationException with message like "Enumeration already finished."
        /// </summary>
        internal static Exception EnumerationFinished() {
            return new InvalidOperationException(Strings.EnumerationFinished);
        }

        /// <summary>
        /// InvalidOperationException with message like "can't add another casing for identifier {0}"
        /// </summary>
        internal static Exception CantAddCasing(object p0) {
            return new InvalidOperationException(Strings.CantAddCasing(p0));
        }

        /// <summary>
        /// InvalidOperationException with message like "can't add new identifier {0}"
        /// </summary>
        internal static Exception CantAddIdentifier(object p0) {
            return new InvalidOperationException(Strings.CantAddIdentifier(p0));
        }

        /// <summary>
        /// ArgumentException with message like "Invalid output directory."
        /// </summary>
        internal static Exception InvalidOutputDir() {
            return new ArgumentException(Strings.InvalidOutputDir);
        }

        /// <summary>
        /// ArgumentException with message like "Invalid assembly name or file extension."
        /// </summary>
        internal static Exception InvalidAsmNameOrExtension() {
            return new ArgumentException(Strings.InvalidAsmNameOrExtension);
        }

        /// <summary>
        /// ArgumentException with message like "Cannot emit constant {0} ({1})"
        /// </summary>
        internal static Exception CanotEmitConstant(object p0, object p1) {
            return new ArgumentException(Strings.CanotEmitConstant(p0, p1));
        }

        /// <summary>
        /// ArgumentException with message like "No implicit cast from {0} to {1}"
        /// </summary>
        internal static Exception NoImplicitCast(object p0, object p1) {
            return new ArgumentException(Strings.NoImplicitCast(p0, p1));
        }

        /// <summary>
        /// ArgumentException with message like "No explicit cast from {0} to {1}"
        /// </summary>
        internal static Exception NoExplicitCast(object p0, object p1) {
            return new ArgumentException(Strings.NoExplicitCast(p0, p1));
        }

        /// <summary>
        /// MissingMemberException with message like "name '{0}' not defined"
        /// </summary>
        internal static Exception NameNotDefined(object p0) {
            return new MissingMemberException(Strings.NameNotDefined(p0));
        }

        /// <summary>
        /// ArgumentException with message like "No default value for a given type."
        /// </summary>
        internal static Exception NoDefaultValue() {
            return new ArgumentException(Strings.NoDefaultValue);
        }

        /// <summary>
        /// ArgumentException with message like "Specified language provider type is not registered."
        /// </summary>
        internal static Exception UnknownLanguageProviderType() {
            return new ArgumentException(Strings.UnknownLanguageProviderType);
        }

        /// <summary>
        /// InvalidOperationException with message like "can't read from property"
        /// </summary>
        internal static Exception CantReadProperty() {
            return new InvalidOperationException(Strings.CantReadProperty);
        }

        /// <summary>
        /// InvalidOperationException with message like "can't write to property"
        /// </summary>
        internal static Exception CantWriteProperty() {
            return new InvalidOperationException(Strings.CantWriteProperty);
        }

        /// <summary>
        /// ArgumentException with message like "Cannot create instance of {0} because it contains generic parameters"
        /// </summary>
        internal static Exception IllegalNew_GenericParams(object p0) {
            return new ArgumentException(Strings.IllegalNew_GenericParams(p0));
        }

        /// <summary>
        /// System.Security.VerificationException with message like "Non-verifiable assembly generated: {0}:\nAssembly preserved as {1}\nError text:\n{2}\n"
        /// </summary>
        internal static Exception VerificationException(object p0, object p1, object p2) {
            return new System.Security.VerificationException(Strings.VerificationException(p0, p1, p2));
        }

    }

    // *** END GENERATED CODE ***

    #endregion

}
