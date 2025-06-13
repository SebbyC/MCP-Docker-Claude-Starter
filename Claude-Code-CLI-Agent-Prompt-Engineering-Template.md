# Claude Code CLI Agent Prompt Engineering Template

## 🎯 Purpose
This template provides structured prompts for leveraging Claude Code CLI agents to efficiently develop, test, and document software projects.

---

## 📋 Pre-Development Checklist Prompts

### Initial Project Analysis
```
Analyze the current project structure and provide:
1. Directory tree overview (max 3 levels deep)
2. Key configuration files present
3. Detected frameworks/languages
4. Missing essential files (if any)
```

### Dependency Check
```
Check and list all project dependencies:
- Package managers detected (npm, pip, cargo, etc.)
- Version conflicts or missing dependencies
- Security vulnerabilities in dependencies
- Suggested updates (with breaking change warnings)
```

---

## 🔍 Log Viewing & Analysis Prompts

### Basic Log Inspection
```
Show me the last [N] lines of logs from [service/file]:
- Highlight any ERROR or WARN level messages
- Summarize patterns in the logs
- Identify potential issues
```

### Docker/Container Logs
```
For the running containers:
1. List all active containers with their status
2. Show logs for [container_name] with timestamps
3. Filter logs for errors in the last [time_period]
4. Identify any container restart loops
```

### Structured Log Analysis
```
Analyze [log_file/service] logs and:
- Extract and count unique error types
- Show time distribution of errors
- Identify correlated events
- Suggest root causes based on patterns
```

### Real-time Log Monitoring
```
Monitor logs for [service] and:
- Alert on specific patterns: [pattern1, pattern2]
- Summarize activity every [N] seconds
- Track performance metrics if present
- Stop monitoring after [condition/time]
```

---

## 🧪 Testing & Validation Prompts

### Unit Test Execution
```
Run unit tests and provide:
1. Total pass/fail count
2. Failed test details with stack traces
3. Code coverage percentage
4. Slowest tests (top 5)
5. Suggestions for improving failing tests
```

### Integration Testing
```
Execute integration tests for [component/service]:
- Set up required test environment
- Run tests with verbose output
- Capture network requests/responses
- Clean up test data after completion
- Summarize integration points tested
```

### API Testing
```
Test the API endpoints:
1. List all available endpoints
2. Test each endpoint with sample data
3. Validate response schemas
4. Check error handling (400, 401, 404, 500)
5. Measure response times
6. Generate a test report
```

### Performance Testing
```
Run performance benchmarks:
- Baseline metrics (CPU, memory, response time)
- Load test with [N] concurrent requests
- Identify bottlenecks
- Compare with previous benchmarks (if available)
- Suggest optimizations
```

---

## 🔄 Change Management Prompts

### Pre-Change Analysis
```
Before making changes to [component]:
1. Create a backup/snapshot of current state
2. Analyze dependencies that might be affected
3. Estimate risk level (low/medium/high)
4. Suggest a rollback strategy
```

### Change Implementation
```
Implement [specific change] and:
- Show diff of all modified files
- Run relevant tests automatically
- Verify no regressions introduced
- Update related documentation
- Commit with descriptive message
```

### Post-Change Verification
```
After implementing changes:
1. Run full test suite
2. Check application still builds successfully
3. Verify key functionality works
4. Monitor logs for new errors (5 min)
5. Generate change summary report
```

---

## 📝 Documentation Prompts

### Code Documentation
```
Document the codebase:
1. Add missing docstrings to functions/classes
2. Update README with current setup instructions
3. Generate API documentation
4. Create sequence diagrams for complex flows
5. Document environment variables and configs
```

### Project Documentation
```
Create/update project documentation:
- Architecture overview with diagrams
- Development setup guide
- Deployment instructions
- Troubleshooting guide
- Contributing guidelines
```

### Change Documentation
```
Document recent changes:
1. Generate CHANGELOG entry
2. Update relevant wiki/docs
3. Create migration guide (if breaking changes)
4. Document new features with examples
5. Update API documentation
```

---

## ✅ Post-Development Checklist Prompts

### Code Quality Check
```
Perform final code quality checks:
- Run linter and fix issues
- Check code formatting
- Identify code smells
- Ensure consistent naming conventions
- Remove commented-out code
- Check for hardcoded values
```

### Security Audit
```
Run security checks:
1. Scan for known vulnerabilities
2. Check for exposed secrets/credentials
3. Validate input sanitization
4. Review authentication/authorization
5. Generate security report
```

### Final Validation
```
Complete final validation:
- All tests passing
- Documentation up to date
- No console.log/debug statements
- Dependencies locked to specific versions
- Build artifacts generated successfully
```

---

## 📋 To-Do Generation Prompts

### Smart To-Do List
```
Generate a prioritized to-do list based on:
1. Failed tests that need fixing
2. TODO/FIXME comments in code
3. Deprecated dependencies to update
4. Performance optimizations identified
5. Security issues to address
6. Documentation gaps to fill

Format: 
- Priority: [High/Medium/Low]
- Category: [Bug/Feature/Optimization/Documentation]
- Estimated effort: [time]
- Dependencies: [what needs to be done first]
```

### Technical Debt Assessment
```
Analyze technical debt and create tasks:
- Code that needs refactoring
- Missing test coverage areas
- Outdated patterns/practices
- Performance bottlenecks
- Accessibility improvements needed
```

### Future Improvements
```
Suggest future enhancements:
1. Features mentioned in comments
2. Optimization opportunities
3. Better error handling locations
4. Areas for better abstraction
5. Monitoring/observability gaps
```

---

## 🚀 Complete Workflow Example

### Full Development Cycle Prompt
```
Execute complete development workflow for [feature/fix]:

1. **Pre-Development**
   - Analyze current state
   - Create feature branch
   - Set up test environment

2. **Development**
   - Implement changes with TDD approach
   - View logs during development
   - Run tests after each significant change

3. **Testing**
   - Unit tests
   - Integration tests
   - Manual testing checklist

4. **Documentation**
   - Update code comments
   - Update README/docs
   - Create examples

5. **Review Preparation**
   - Run all quality checks
   - Generate change summary
   - Create pull request description

6. **Post-Implementation**
   - Generate to-do list for remaining work
   - Document lessons learned
   - Update project roadmap
```

---

## 💡 Best Practices

### Effective Prompting Tips
1. **Be Specific**: Include file names, service names, and exact requirements
2. **Set Boundaries**: Specify time limits, file limits, or scope constraints
3. **Request Formats**: Ask for output in specific formats (JSON, Markdown tables, etc.)
4. **Chain Commands**: Use "then" to sequence multiple actions
5. **Error Handling**: Always ask for error handling and edge cases

### Example Power Prompts

**Comprehensive Debug Session**
```
Debug the failing [service_name]:
1. Check if service is running (docker ps or ps aux)
2. Tail last 100 lines of logs
3. Look for ERROR patterns
4. Check resource usage (CPU/Memory)
5. Verify network connectivity
6. Test with minimal reproduction case
7. Suggest fixes with confidence levels
```

**Automated Deployment Verification**
```
Verify deployment of [version] to [environment]:
- Check all services are healthy
- Run smoke tests
- Compare configs with previous version
- Monitor error rates for 10 minutes
- Generate deployment report
- Create rollback plan if needed
```

---

## 📊 Reporting Templates

### Daily Development Report
```
Generate daily development report including:
- Commits made today with summaries
- Tests added/modified
- Issues resolved
- New issues discovered
- Time spent per task (from git commits)
- Tomorrow's priorities
```

### Sprint Summary
```
Create sprint summary:
- Features completed
- Bugs fixed
- Test coverage delta
- Performance improvements
- Technical debt addressed
- Remaining work estimation
```

---

## 🔧 Troubleshooting Prompts

### When Things Go Wrong
```
System is not working as expected:
1. Identify what changed recently (git log)
2. Check system resources
3. Verify all services are running
4. Look for configuration mismatches
5. Test each component in isolation
6. Provide step-by-step debugging plan
```

### Recovery Procedures
```
Recover from [error/failure]:
- Assess current system state
- Identify corrupted/missing data
- Create recovery plan
- Execute recovery with verification
- Document incident and prevention steps
```

---

## 📚 Additional Resources

### Custom Prompt Templates
Create your own templates following this pattern:
```
[Action] [Target] with requirements:
- Constraint 1
- Constraint 2
- Expected output format
- Success criteria
```

### Prompt Chaining
Link multiple prompts for complex workflows:
```
First: [Setup action]
Then: [Main action]
Finally: [Cleanup and report]
If error: [Error handling action]
```

---

## 🎯 Quick Reference Card

| Task | Quick Prompt |
|------|--------------|
| View logs | `Show last 50 lines of [service] logs with errors highlighted` |
| Run tests | `Run all tests and show only failures with details` |
| Check changes | `Show git diff with explanation of changes` |
| Document | `Add docstrings to all public functions in [file]` |
| Create TODOs | `Scan codebase for TODO/FIXME and create prioritized list` |

---

*Remember: The more context and constraints you provide, the better Claude Code can assist you. Be specific about what you want to see, how you want it formatted, and what success looks like.*