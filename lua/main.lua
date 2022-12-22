local invoices = io.open('invoices.txt', 'r')

--[[
	Lua does not have regex. Lua is a scripting language
	meant to be embedded in other systems. It's very unlikely
	that paypal uses Lua for their backend, but it had to
	be done for the sake of saying it can be done. PAYAL, FIX IT!
	
	This example is not very sophisticated, but it explores
	use of some string manipulation that would probably be
	used in a more advanced system with access to a maintained
	database of common things to look for in a scam invoice.
--]]

local phone_no_min_length = 8
local phone_no_max_length = 15

-- could add official paypal numbers
local whitelisted_numbers = {
	-- example entry
	['1234567890'] = true
}

-- use lowercase!
local flagged_words = {
	['call'] = 1,
	['refund'] = 1,
	['cancel'] = 1,
	['contact'] = 1,
	['btc'] = 1,
	['illegal'] = 1,
	['illegally'] = 1,
	['fraud'] = 1,
	['detected'] = 1,
	['unauthorized'] = 1,
	['fraudulently'] = 1,
	['authorized'] = 0.5,
	['usd'] = 0.5
}

local flagged_phrases = {
	['help desk'] = 0.5,
	['24 hours'] = 0.25,
}

local function evaluate(text)
	-- remove extra whitespace and symbols for easier evaluation
	text = text:lower()
		:gsub('  +', ' ')
		:gsub('[^%w $]+', '')
		:gsub('(%d) (%d)', '%1%2')

	local sus_score = 0
	local numbers = {}

	for word in text:gmatch('%w+') do
		if flagged_words[word] then
			sus_score = sus_score + flagged_words[word]
		elseif word:match('%d+') == word and not whitelisted_numbers[word] then
			table.insert(numbers, word)
		end
	end

	for phrase, score in pairs(flagged_phrases) do
		local _, count = text:gsub(phrase, phrase)
		if count > 0 then
			sus_score = sus_score + (score * count)
		end
	end

	for _, number in ipairs(numbers) do
		if #number >= phone_no_min_length and #number <= phone_no_max_length then
			sus_score = sus_score + 2
		end
	end

	if sus_score >= 3.5 then
		print(string.format('invoice starting with "%s" is SUS, with a score of %g', text:sub(1, 10), sus_score))
	end
end

for line in invoices:lines() do
	evaluate(line)
end

invoices:close()
