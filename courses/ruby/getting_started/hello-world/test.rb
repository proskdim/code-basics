result = hello()
expected = 'Hello, World!'
if result != expected
  puts "Получено: #{result}, ожидалось: #{expected}"
  exit 1
end
puts 'OK'
